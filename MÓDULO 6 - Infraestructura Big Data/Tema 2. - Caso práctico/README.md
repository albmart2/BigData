# Caso Práctico con Solución

## PARTE 1: PIG

### Objetivo

Poner en práctica los conocimientos adquiridos sobre la herramienta Pig para resolver el ejercicio.

### Datos

Discografía de Pink Floyd (año, nombre del disco, ranking EE. UU., ranking Reino Unido):

| Año  | Disco                          | EE. UU. | Reino Unido |
|------|--------------------------------|---------|-------------|
| 1967 | The Piper at the Gates of Dawn | 131     | 6           |
| 1968 | A Saucerful of Secrets         | 999     | 9           |
| 1969 | Music from the Film More       | 153     | 9           |
| 1969 | Ummagumma                      | 74      | 5           |
| 1970 | Atom Heart Mother               | 55      | 1           |
| 1972 | Obscured by Clouds             | 46      | 6           |
| 1973 | The Dark Side of the Moon      | 1       | 1           |
| 1975 | Wish You Were Here             | 1       | 1           |
| 1977 | Animals                        | 3       | 2           |
| 1979 | The Wall                       | 1       | 3           |
| 1983 | The Final Cut                  | 6       | 1           |
| 1987 | A Momentary Lapse of Reason    | 3       | 3           |
| 1994 | The Division Bell              | 1       | 1           |
| 2014 | The Endless River              | 3       | 1           |

### Se Pide

Indicar los comandos empleados para resolver las siguientes cuestiones:

1. Crear un fichero llamado `discos.txt`.
2. Arrancar HDFS, YARN y el "job history".
3. Subir el fichero a HDFS dentro de la carpeta `/ejerciciosPig/discos.txt`.
4. Ejecutar la instrucción `ls` sobre Hadoop para indicar el tamaño del fichero.
5. Arrancar Pig en modo distribuido y ejecutar el comando `cat hdfs://localhost:9000/ejerciciosPig/discos.txt` para confirmar que el fichero está subido a HDFS.
6. Cargar el fichero de HDFS en una variable llamada `discos`.
7. Calcular los discos que no estuvieron ni en el top ten de EE. UU. ni en el top ten del Reino Unido (indicar también el resultado).
8. Obtener la máxima y mínima posición que ocuparon los discos de Pink Floyd en EE. UU. y en el Reino Unido (indicar también el resultado), empleando los comandos de Pig Latin.
9. Explicar, desde la opinión personal, lo que se pretende obtener con los siguientes comandos e indicar el resultado obtenido:

```pig
a = foreach discos generate anio;
b = distinct a;
dump b;
```

10. **(OPCIONAL)** Realizar el ejercicio 8 empleando las funciones de PiggyBank:  
    https://pig.apache.org/docs/r0.15.0/api/org/apache/pig/EvalFunc.html

---

### Solución

#### 1. Crear el fichero `discos.txt`

```bash
mkdir ejerciciosPig
sudo nano ejerciciosPig/discos.txt
```

#### 2. Arrancar HDFS, YARN y el JobHistory

Comprobar que están ya arrancados los servicios de HDFS, YARN y el JobHistory.

#### 3. Subir el fichero a HDFS

```bash
hdfs dfs -put ejerciciosPig/discos.txt hdfs://localhost:9000/ejerciciosPig
```

#### 4. Ejecutar `ls` sobre Hadoop

```bash
hdfs dfs -ls -R /ejerciciosPig
```

El tamaño del fichero es **438**.

#### 5. Arrancar Pig en modo distribuido y verificar el fichero

Acceder a Pig en modo distribuido:

```bash
pig -x mapreduce
```

Comprobar que el fichero está correctamente subido a HDFS:

```pig
cat hdfs://localhost:9000/ejerciciosPig/discos.txt
```

#### 6. Cargar el fichero en una variable `discos`

```pig
discos = load 'hdfs://localhost:9000/ejerciciosPig/discos.txt'
    using PigStorage(',')
    as (anio:int, disco:chararray, eeuu:int, uk:int);
```

Comprobar que se ha cargado bien:

```pig
describe discos
illustrate discos
dump discos
```

#### 7. Discos fuera del top ten en EE. UU. y Reino Unido

```pig
discos_notop = filter discos by eeuu > 10 and uk > 10;
dump discos_notop;
```

**Resultado:** No hay ningún disco que no estuviera ni en el top ten de EE. UU. ni en el top ten del Reino Unido.

#### 8. Máxima y mínima posición en EE. UU. y Reino Unido

```pig
rank_eeuu  = order discos by eeuu desc;
rank_uk    = order discos by uk desc;
min_eeuu   = limit rank_eeuu 1;
min_uk     = limit rank_uk 1;
rank2_eeuu = order discos by eeuu;
rank2_uk   = order discos by uk;
max_eeuu   = limit rank2_eeuu 1;
max_uk     = limit rank2_uk 1;

dump max_eeuu;
dump min_eeuu;
dump max_uk;
dump min_uk;
```

**Resultados:**

| Mercado      | Máxima posición | Mínima posición |
|--------------|-----------------|-----------------|
| EE. UU.      | 1               | 999             |
| Reino Unido  | 1               | 999             |

#### 9. Explicación de los comandos

```pig
a = foreach discos generate anio;
b = distinct a;
dump b;
```

- `foreach discos generate anio` → obtiene los datos de la columna `anio` de la variable `discos`, es decir, los años en los que se ha publicado un disco.
- `distinct a` → elimina los valores duplicados de la variable que contiene los años.
- `dump b` → muestra el resultado obtenido (años únicos de publicación).

#### 10. (OPCIONAL) Ejercicio 8 con PiggyBank

```pig
a = foreach discos generate eeuu;
dump a;
max_eeuu = foreach a GENERATE org.apache.pig.piggybank.evaluation.math.MAX(eeuu);
min_eeuu = foreach a GENERATE org.apache.pig.piggybank.evaluation.math.MIN(eeuu);

b = foreach discos generate uk;
dump b;
max_uk = foreach a GENERATE org.apache.pig.piggybank.evaluation.math.MAX(uk);
min_uk = foreach a GENERATE org.apache.pig.piggybank.evaluation.math.MIN(uk);
```

---

## PARTE 2: HIVE

### Objetivo

Poner en práctica los conocimientos adquiridos sobre la herramienta Hive para resolver el ejercicio.

### Datos

Discografía de Pink Floyd (año, nombre del disco, ranking EE. UU., ranking Reino Unido) — los mismos datos que en la Parte 1.

### Se Pide

Indicar los comandos empleados para resolver las siguientes cuestiones:

1. Crear un fichero de texto con la información anterior (importante: tener cuidado con los caracteres al final de línea).
2. Crear una tabla en Hive que permita almacenar los datos anteriores, indicando que el formato de separación es de tipo coma:
   ```sql
   create table ...... (.......) row format delimited fields terminated by ',' stored as textfile;
   ```
3. Cargar el fichero de texto.
4. Acceder a Hive y ejecutar una consulta sencilla (`select *`) para verificar que hay datos y que se han cargado correctamente. En caso contrario, volver a cargar los datos.
5. Calcular los discos que estuvieron a la vez entre los cinco primeros puestos en EE. UU. y en el Reino Unido.
6. **(OPCIONAL)** Obtener la máxima y mínima posición que ocuparon los discos de Pink Floyd en EE. UU. y en el Reino Unido (empleando los comandos `order` y `limit` en dos sentencias).

### Solución

#### 1. Crear el fichero de texto

```bash
mkdir ejerciciosHive
sudo nano ejerciciosHive/discografia
```

#### 2. Crear la tabla en Hive

Arrancar Hive:

```bash
hive
```

Crear la tabla con los cuatro campos necesarios:

```sql
create table discografia (
    anio INT,
    disco STRING,
    eeuu INT,
    uk INT
)
ROW FORMAT DELIMITED
FIELDS TERMINATED BY ','
LINES TERMINATED BY '\n'
STORED AS TEXTFILE;
```

Comprobar que se ha creado:

```sql
show tables;
```

#### 3. Cargar el fichero de texto

```sql
LOAD DATA LOCAL INPATH '/home/bigdata/ejerciciosHive/discografia'
INTO TABLE discografia;
```

#### 4. Verificar la carga con `select *`

```sql
select * from discografia;
```

#### 5. Discos en el top 5 simultáneamente en EE. UU. y Reino Unido

```sql
select * from discografia where eeuu <= 5 and uk <= 5;
```

#### 6. (OPCIONAL) Máxima y mínima posición en EE. UU. y Reino Unido

```sql
select max(eeuu) as MaxEEUU, max(uk) as MaxUK from discografia;
```

**Resultado:** 999 para EE. UU. y 9 para el Reino Unido.

```sql
select min(eeuu) as MinEEUU, min(uk) as MinUK from discografia;
```

**Resultado:** 1 para EE. UU. y 1 para el Reino Unido.
