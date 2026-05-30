# Caso Práctico

## Contexto

Solución al caso práctico de PySpark Streaming trabajando con datos de mercados financieros (NYSE y NASDAQ), obteniendo medias de precios de apertura y cierre procesadas como streams.

**Dataset:** `stocks_data_streaming` — archivos JSON con los campos `Company_Name`, `Date`, `Open` y `Close`.

## Solución

### Paso 1 — Importar tipos de datos

```python
from pyspark.sql.types import TimestampType, StringType, StructType, StructField, DoubleType
```

### Paso 2 — Definir ruta de entrada y esquema

```python
datos_entrada = "/FileStore/stocks_data_streaming"

schema = StructType([
    StructField("Company_Name", StringType(), True),
    StructField("Date", TimestampType(), True),
    StructField("Open", DoubleType(), True),
    StructField("Close", DoubleType(), True)
])
```

### Paso 3 — Lectura estática y visualización inicial

```python
SparkDF = (
    spark
        .read
        .schema(schema)
        .json(datos_entrada)
)

display(SparkDF)
```

**Resultado (muestra):**

| Company_Name | Date | Open | Close |
|---|---|---|---|
| NYSE | 2021-11-15T07:54:35 | 141664.09 | 201135.65 |
| NASDAQ | 2021-11-15T06:03:08 | 43915.34 | 96019.01 |
| NYSE | 2021-11-15T10:49:05 | 63261.66 | 53307.69 |
| ... | ... | ... | ... |

> Se muestran los primeros 1000 registros. Algunos tienen valores nulos en las primeras filas.

### Paso 4 — Limpieza de nulos

```python
SparkDF = SparkDF.dropna()

display(SparkDF)
```

### Paso 5 — Agrupación estática (referencia batch)

Se agrupa por `Company_Name` y se calculan las medias de `Open` y `Close`:

```python
stocks_DF_dos = (
    SparkDF
        .groupBy(SparkDF.Company_Name)
        .mean()
)

stocks_DF_dos.cache()
stocks_DF_dos.createOrReplaceTempView("stocks_table")

display(stocks_DF_dos)
```

**Resultado:**

| Company_Name | avg(Open) | avg(Close) |
|---|---|---|
| NYSE | 74734.29 | 124670.89 |
| NASDAQ | 76445.83 | 123166.18 |

### Paso 6 — Lectura en modo Streaming

Se sustituye `spark.read` por `spark.readStream`, simulando la llegada de un archivo JSON por trigger:

```python
streamingDF = (
    spark
        .readStream
        .schema(schema)
        .option("maxFilesPerTrigger", 1)
        .json(datos_entrada)
)
```

### Paso 7 — Transformación sobre el stream

```python
streamingStocksDF = (
    streamingDF
        .groupBy(streamingDF.Company_Name)
        .mean()
)

spark.conf.set("spark.sql.shuffle.partitions", "2")
```

### Paso 8 — Escritura del stream en memoria

```python
query = (
    streamingStocksDF
        .writeStream
        .format("memory")
        .queryName("stocks")
        .outputMode("complete")
        .start()
)
```

Los resultados quedan disponibles como vista SQL temporal `stocks`, actualizándose en tiempo real con cada microbatch.

## Notas adicionales

```python
# Para detener el stream manualmente:
# query.stop()

# Para eliminar los datos de DBFS si fuera necesario:
# dbutils.fs.rm("/FileStore/stocks_data_streaming", True)
```

## Resumen de parámetros de `writeStream`

| Parámetro | Valor | Descripción |
|---|---|---|
| `format` | `memory` | Persiste resultados en memoria, consultables como vista SQL |
| `queryName` | `stocks` | Nombre de la vista SQL temporal |
| `outputMode` | `complete` | Envía todos los resultados completos en cada trigger |

> **`outputMode` opciones disponibles:**
> - `append` — agrega nuevas filas al resultado
> - `complete` — envía todos los resultados completos
> - `update` — envía solo las filas actualizadas
