# Caso práctico de Analítica Escalable — Ejercicios (con solución)

Basado en el notebook `AnaliticaEscalablePySparkEjercicios`, sobre el dataset `Hotel_Reviews.csv`.

Contexto previo cargado en el notebook (necesario para entender las soluciones):

```python
df_spark_sql = spark.read.format("csv") \
  .option("header", "true") \
  .option("inferSchema", "true") \
  .load("/databricks/driver/Hotel_Reviews.csv")

# UDFs para transformar Average_Score en categorías y viceversa
def score_to_string(score):
  if score < 5:
    return "Bad"
  elif score < 7:
    return "Normal"
  elif score < 9:
    return "Good"
  elif score < 10:
    return "Excellent"
  else:
    return "Perfect"

def score_to_evaluation(score_string):
  score_dict = {"Bad": 0, "Normal": 1, "Good": 2, "Excellent": 3, "Perfect": 4}
  return score_dict.get(score_string, None)

# Se añaden las columnas score_string, score_evaluation y se limpia days_since_review
# Se hace un split Train/Test (67% / 33%)
splits = df_spark_sql.randomSplit([0.67, 0.33])
df_spark_sql_train = splits[0].dropna()
df_spark_sql_test  = splits[1].dropna()
```

## Bloque 1: DataFrames en Spark / SparkSQL

### Ejercicio 1
**Enunciado:** Crear un bucle que muestre todas las columnas del DataFrame, junto con sus tipos. También puedes pintar el esquema del DataFrame.

**Solución:**
```python
for nombre_columna, tipo_columna in df_spark_sql.dtypes:
    print(f"{nombre_columna}: {tipo_columna}")

# Alternativa / complemento: pintar el esquema completo
df_spark_sql.printSchema()
```

### Ejercicio 2
**Enunciado:** Realizar un muestreo de 10 valores únicos de nombres de hoteles. Ordénalos alfanuméricamente de forma ascendente (primero los números 0-9, después A-Z).

**Solución:**
```python
df_spark_sql.select("Hotel_Name") \
    .distinct() \
    .orderBy("Hotel_Name", ascending=True) \
    .show(10, truncate=False)
```

---

### Ejercicio 3
**Enunciado:** Transforma las columnas `lat` y `lng` al tipo Float.

**Solución:**
```python
from pyspark.sql.types import FloatType

# Transformación de las columnas sin utilizar UDF (usando cast)
df_spark_sql = df_spark_sql.withColumn("lat", df_spark_sql["lat"].cast(FloatType()))
df_spark_sql = df_spark_sql.withColumn("lng", df_spark_sql["lng"].cast(FloatType()))

df_spark_sql.printSchema()
```

### Ejercicio 4
**Enunciado:** ¿Cuántos hoteles tienen una puntuación de 'Perfect'? ¿Y 'Good'? ¿Y 'Normal' junto a 'Good'? (Utilizar el dataset de Train).

**Solución:**
```python
num_perfect = df_spark_sql_train.filter(df_spark_sql_train.score_string == "Perfect").count()
num_good = df_spark_sql_train.filter(df_spark_sql_train.score_string == "Good").count()
num_normal_good = df_spark_sql_train.filter(
    (df_spark_sql_train.score_string == "Normal") | (df_spark_sql_train.score_string == "Good")
).count()

print("Perfect:", num_perfect)
print("Good:", num_good)
print("Normal + Good:", num_normal_good)
```

### Ejercicio 5
**Enunciado:** Obtener los hoteles con mayor puntuación media, descartando todos los que tengan una puntuación por encima de Good. (Utilizar el dataset de Train).

**Solución:**
```python
from pyspark.sql import functions as F

df_spark_sql_train.filter(~df_spark_sql_train.score_string.isin(["Excellent", "Perfect"])) \
    .groupBy("Hotel_Name") \
    .agg(F.avg("Average_Score").alias("puntuacion_media")) \
    .orderBy(F.desc("puntuacion_media")) \
    .show(truncate=False)
```

## Bloque 2: Machine Learning con Spark MLlib / Spark ML — Árboles de decisión

### Ejercicio 6.1
**Enunciado:** Volver a observar todas las columnas del DataFrame, para identificar las que sean categóricas.

**Solución:**
```python
df_spark_sql.printSchema()

columnas_categoricas = [nombre for nombre, tipo in df_spark_sql.dtypes if tipo == "string"]
print("Columnas categóricas (string):", columnas_categoricas)
```

### Ejercicio 6.2
**Enunciado:** Eliminar, de los DataFrames `df_spark_sql_train` y `df_spark_sql_test`, las variables `Hotel_Address`, `Hotel_Name`, `Tags`, `Positive_Review`, `Negative_Review` y `score_string`. Llamarlos: `df_DT_train` y `df_DT_test`.

**Solución:**
```python
columnas_a_eliminar = ["Hotel_Address", "Hotel_Name", "Tags",
                        "Positive_Review", "Negative_Review", "score_string"]

df_DT_train = df_spark_sql_train.drop(*columnas_a_eliminar)
df_DT_test = df_spark_sql_test.drop(*columnas_a_eliminar)
```

### Ejercicio 7
**Enunciado:** Para cada columna restante que sea String (`Review_Date` y `Review_Nationality`), aplicar un `StringIndexer()`, devolviendo como resultado la misma columna, pero con su nombre acabando en `_index`. Sobreescribir ambos DataFrames.

**Solución:**
```python
from pyspark.ml.feature import StringIndexer

for columna in ["Review_Date", "Review_Nationality"]:
    indexer = StringIndexer(inputCol=columna, outputCol=columna + "_index")
    df_DT_train = indexer.fit(df_DT_train).transform(df_DT_train)
    df_DT_test = indexer.fit(df_DT_test).transform(df_DT_test)
```

### Ejercicio 8
**Enunciado:** Aplicar `VectorAssembler()` sobre las columnas que no son ni las dos anteriores (`Review_Date`, `Review_Nationality`), ni la columna `score_evaluation`, devolviendo una columna llamada `features`. Llamar al resultado `DT_vector_assembler`.

**Solución:**
```python
from pyspark.ml.feature import VectorAssembler

columnas_excluir = ["Review_Date", "Review_Nationality", "score_evaluation"]
columnas_features = [c for c in df_DT_train.columns if c not in columnas_excluir]

DT_vector_assembler = VectorAssembler(inputCols=columnas_features, outputCol="features")
```

### Ejercicio 9
**Enunciado:** Aplicar el transformador sobre ambos DataFrames.

**Solución:**
```python
df_DT_train = DT_vector_assembler.transform(df_DT_train)
df_DT_test = DT_vector_assembler.transform(df_DT_test)
```

### Ejercicio 10
**Enunciado:** Inicializar el modelo de árbol de decisión, entrenarlo y aplicarlo sobre los datos de test.
- Modelo: `DecisionTreeClassifier`
  - Label: `score_evaluation`
  - Features: `features`
  - `maxBins`: 1000
  - `maxDepth`: 1

**Solución:**
```python
from pyspark.ml.classification import DecisionTreeClassifier

dt = DecisionTreeClassifier(
    labelCol="score_evaluation",
    featuresCol="features",
    maxBins=1000,
    maxDepth=1
)

dt_model = dt.fit(df_DT_train)
dt_predictions = dt_model.transform(df_DT_test)
```

### Ejercicio 11
**Enunciado:** Evaluar el modelo aplicándole un clasificador multiclase. Calcular la métrica `accuracy`, y conseguir el complementario para calcular el error.
- Evaluador: `MulticlassClassificationEvaluator`
  - Label: `score_evaluation`
  - Prediction: `prediction`
  - MetricName: `accuracy`

**Solución:**
```python
from pyspark.ml.evaluation import MulticlassClassificationEvaluator

evaluator = MulticlassClassificationEvaluator(
    labelCol="score_evaluation",
    predictionCol="prediction",
    metricName="accuracy"
)

accuracy = evaluator.evaluate(dt_predictions)
error = 1 - accuracy

print("Accuracy:", accuracy)
print("Error:", error)
```

## Bloque 3: Spark ML — Pipelines (Árboles de Decisión)

> Flujo del pipeline: `StringIndexer → VectorAssembler → DecisionTree (inicialización) → DecisionTree (entrenamiento) → Modelo entrenado`

### Ejercicio 12
**Enunciado:** Eliminar, de los DataFrames `df_spark_sql_train` y `df_spark_sql_test`, las variables `Hotel_Address`, `Hotel_Name`, `Tags`, `Positive_Review`, `Negative_Review` y `score_string`. Llamarlos: `df_DT_train` y `df_DT_test`.

**Solución:**
```python
columnas_a_eliminar = ["Hotel_Address", "Hotel_Name", "Tags",
                        "Positive_Review", "Negative_Review", "score_string"]

df_DT_train = df_spark_sql_train.drop(*columnas_a_eliminar)
df_DT_test = df_spark_sql_test.drop(*columnas_a_eliminar)
```

### Ejercicio 13
**Enunciado:** Recoger una lista con todos los `StringIndexer` a aplicar, y llamarla `DT_string_indexers`. En lugar de sobreescribir cada vez el DataFrame, crear una lista, y con el método `append`, se irán añadiendo todos los `StringIndexer()`.

**Solución:**
```python
from pyspark.ml.feature import StringIndexer

DT_string_indexers = []

for columna in ["Review_Date", "Review_Nationality"]:
    indexer = StringIndexer(inputCol=columna, outputCol=columna + "_index")
    DT_string_indexers.append(indexer)
```

### Ejercicio 14
**Enunciado:** Guardar en la variable `DT_vector_assembler` la aplicación del mismo `VectorAssembler()` del ejercicio 8.

**Solución:**
```python
from pyspark.ml.feature import VectorAssembler

columnas_excluir = ["Review_Date", "Review_Nationality", "score_evaluation"]
columnas_features = [c for c in df_DT_train.columns if c not in columnas_excluir] \
                     + ["Review_Date_index", "Review_Nationality_index"]

DT_vector_assembler = VectorAssembler(inputCols=columnas_features, outputCol="features")
```
> Nota: a diferencia del ejercicio 8, aquí las columnas `_index` todavía no existen en `df_DT_train`/`df_DT_test`, ya que serán generadas por los `StringIndexer` al ejecutarse el pipeline. `VectorAssembler` solo necesita conocer los **nombres** de las columnas que existirán llegado su turno en el pipeline.

### Ejercicio 15
**Enunciado:** Crear una lista con el nombre `DT_pipeline_stages`, y añadirle la lista de `StringIndexer` y el `VectorAssembler` (en este orden).

**Solución:**
```python
DT_pipeline_stages = []
DT_pipeline_stages += DT_string_indexers
DT_pipeline_stages.append(DT_vector_assembler)
```

### Ejercicio 16
**Enunciado:** Inicializar el modelo de árbol de decisión (mismas especificaciones que en el ej. 10), y añadirlo a la lista de pasos `DT_pipeline_stages`.

**Solución:**
```python
from pyspark.ml.classification import DecisionTreeClassifier

dt = DecisionTreeClassifier(
    labelCol="score_evaluation",
    featuresCol="features",
    maxBins=1000,
    maxDepth=1
)

DT_pipeline_stages.append(dt)
```

### Ejercicio 17
**Enunciado:** Diseñar el Pipeline y aplicarlo sobre los datos de Train, llamándolo `DT_pipeline_model`.

**Solución:**
```python
from pyspark.ml import Pipeline

DT_pipeline = Pipeline(stages=DT_pipeline_stages)
DT_pipeline_model = DT_pipeline.fit(df_DT_train)
```

### Ejercicio 18
**Enunciado:** Aplicar el modelo resultante sobre los datos de test y evaluarlo al igual que se hizo en el ej. 11.

**Solución:**
```python
from pyspark.ml.evaluation import MulticlassClassificationEvaluator

DT_pipeline_predictions = DT_pipeline_model.transform(df_DT_test)

evaluator = MulticlassClassificationEvaluator(
    labelCol="score_evaluation",
    predictionCol="prediction",
    metricName="accuracy"
)

accuracy = evaluator.evaluate(DT_pipeline_predictions)
error = 1 - accuracy

print("Accuracy:", accuracy)
print("Error:", error)
```
