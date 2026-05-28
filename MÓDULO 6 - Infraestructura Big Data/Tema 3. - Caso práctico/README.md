# Caso práctico

## Objetivo

Poner en práctica los conocimientos adquiridos sobre la herramienta Spark para resolver el ejercicio.

## Se Pide

### Datos

Discografía de Pink Floyd en formato JSON:

```json
{"year":1967,"Title":"The Piper at the Gates of Dawn","USA_Ranking":131,"Uk_Ranking":6}
{"year":1968,"Title":"A Saucerful of Secrets","USA_Ranking":999,"Uk_Ranking":9}
{"year":1969,"Title":"Music from the Film More","USA_Ranking":153,"Uk_Ranking":9}
{"year":1969,"Title":"Ummagumma","USA_Ranking":74,"Uk_Ranking":5}
{"year":1970,"Title":"Atom Heart Mother","USA_Ranking":55,"Uk_Ranking":1}
{"year":1972,"Title":"Obscured by Clouds","USA_Ranking":46,"Uk_Ranking":6}
{"year":1973,"Title":"The Dark Side of the Moon","USA_Ranking":1,"Uk_Ranking":1}
{"year":1975,"Title":"Wish you Were Here","USA_Ranking":1,"Uk_Ranking":1}
{"year":1977,"Title":"Animals","USA_Ranking":3,"Uk_Ranking":2}
{"year":1979,"Title":"The Wall","USA_Ranking":1,"Uk_Ranking":3}
{"year":1983,"Title":"The Final Cut","USA_Ranking":6,"Uk_Ranking":1}
{"year":1987,"Title":"A Momentary Lapse of Reason","USA_Ranking":3,"Uk_Ranking":3}
{"year":1994,"Title":"The Division Bell","USA_Ranking":1,"Uk_Ranking":1}
{"year":2014,"Title":"The Endless River","USA_Ranking":3,"Uk_Ranking":1}
```

Indicar los comandos empleados para resolver las siguientes cuestiones:

1. Crear un archivo con los JSON anteriores.
2. Cargar este archivo en HDFS.
3. Generar un dataframe desde el archivo subido a HDFS.
4. Recuperar el esquema del dataframe.
5. Crear una vista temporal con el comando `createOrReplaceTempView`.
6. Calcular los discos que ocuparon a la vez posiciones entre las cinco primeras en ambos rankings.
7. Obtener la máxima y mínima posición que ocuparon los discos de Pink Floyd en EE. UU. y en el Reino Unido.
8. Obtener los títulos de los discos en mayúsculas.

## Solución

### 1. Crear el archivo JSON

```bash
sudo mkdir /home/bigdata/ejercicioSpark
sudo nano /home/bigdata/ejercicioSpark/PinkFloyd.json
```

### 2. Cargar el archivo en HDFS

```bash
hdfs dfs -mkdir /ejercicioSpark
hdfs dfs -put /home/bigdata/ejercicioSpark/PinkFloyd.json /ejercicioSpark
hdfs dfs -ls /ejercicioSpark
```

### 3. Generar un dataframe desde HDFS

```scala
spark-shell
scala> val df = spark.read.json("/ejercicioSpark/PinkFloyd.json")
df.show()
```

### 4. Recuperar el esquema del dataframe

```scala
scala> df.printSchema()
```

### 5. Crear una vista temporal

```scala
df.createOrReplaceTempView("PinkFloyd")
```

### 6. Discos en el top 5 simultáneamente en EE. UU. y Reino Unido

```scala
val res = spark.sql("SELECT * FROM PinkFloyd WHERE USA_Ranking < 5 AND Uk_Ranking < 5")
res.show()
```

### 7. Máxima y mínima posición en EE. UU. y Reino Unido

```scala
val max_USA = spark.sql("SELECT Max(USA_Ranking) FROM PinkFloyd")
max_USA.show()

val max_UK = spark.sql("SELECT Max(Uk_Ranking) FROM PinkFloyd")
max_UK.show()

val min_USA = spark.sql("SELECT Min(USA_Ranking) FROM PinkFloyd")
min_USA.show()

val min_UK = spark.sql("SELECT Min(Uk_Ranking) FROM PinkFloyd")
min_UK.show()
```

### 8. Títulos de los discos en mayúsculas

```scala
df.select(upper(df("Title"))).show()
```
