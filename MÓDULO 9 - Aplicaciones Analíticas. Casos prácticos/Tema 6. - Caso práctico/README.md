# Caso práctico: crear un índice para consulta de empleados de una empresa

A modo de ejemplo, vamos a imaginarnos que nos ponen al frente de la base de datos de una pizzería y, en ella, tenemos que dar de alta a los empleados y las pizzas de esta empresa. Para ello, primero, vamos a practicar con los datos de los empleados y, posteriormente, como ejercicio de evaluación, manejaremos en ES el menú de pizzas de este negocio.

Gracias a esta plataforma, se puede conseguir lo siguiente:

- Realizar operaciones de inserción y creación de los datos en el motor de búsqueda Elasticsearch.
- Realizar operaciones de borrado y modificación de datos.
- Realizar consultas en estos datos.

1. No obstante, en primer lugar, debemos importar ES_UBUNTU.ova. Para ello, tenemos que tener instalado en nuestro entorno la Virtual Box 5.2 de Oracle. Este entorno requiere la instalación de la VirtualBox 5.2.18 Platform Packages correspondiente a nuestro servidor, generalmente Windows host, así como el Extension Pack, que es único para todas las plataformas. Este se puede encontrar en el siguiente enlace: [Virtual Box](https://www.virtualbox.org/wiki/Downloads)

    Una vez realizada la instalación, en el caso de que todavía no se haya llevado a cabo, se abre la herramienta y se importa el fichero ES_UBUNTU.ova. Para ello, se va a Archivo --> Importar servicio virtualizado.

    <img width="492" height="476" alt="image" src="https://github.com/user-attachments/assets/9abbe0b9-369f-4103-b55e-2b3e7c4eadd8" />

    Se da al botón Next o Siguiente, se revisan los parámetros como la CPU o RAM si fueran demasiado altos para nuestro entorno; no obstante, en su defecto, se aconseja usar los que vienen. Y se presiona el botón Importar que aparece a continuación.

2. Una vez importada la máquina, el proceso es muy simple; solo hay que pinchar la máquina virtual y, en el menú Máquina --> Iniciar o con el menú emergente o en la flecha verde del menú superior, se arranca la máquina virtual.

    > El usuario es *code* y la clave es el mismo nombre, es decir, *code*

    <img width="501" height="495" alt="image" src="https://github.com/user-attachments/assets/986824cc-f4c7-4cb3-9f69-2b50c049f4dd" />

Para manejar las instrucciones HTTP API, se van a utilizar dos tipos de herramientas. Una mediante el uso del comando curl y otra con el navegador Chromium (equivalente al Chrome de Windows) y un plugging que ya está instalado y se llama ElasticSearch Head. Este último se ha puesto para facilitar, especialmente, las salidas de los comandos de forma más amigable.

En la siguiente figura, vemos que tenemos la terminal de comando en Linux. Simplemente se ejecuta con el menú emergente haciendo clic en el escritorio y, además, en la parte superior derecha, veremos marcado en amarillo el plugging instalado. Con cualquiera de estas dos herramientas, podemos ejecutar los comandos.

<img width="915" height="315" alt="image" src="https://github.com/user-attachments/assets/bdd316ec-0124-40ee-b8ff-85bb10fc364d" />

En primer lugar, es preciso verificar que ES está arrancado.

```bash
curl -XGET http://localhost:9200
```

Vamos a explicar este comando. Los demás se agregarán a este.

- **curl**: es la aplicación en modo línea de comandos que sirve para ejecutar el HTTP APLI.
- **–X**: es propio de curl para que entienda el tipo de API. Siempre es el mismo para ES.
- **GET**: corresponde a modo consulta del API.
- **http://localhost:9200**: es la ruta y puerto donde escucha ES.

La salida tiene que ser algo similar a esto:

<img width="726" height="445" alt="image" src="https://github.com/user-attachments/assets/cebafe19-2468-484d-aeb5-200375785871" />

En segundo lugar, nos piden crear un sistema que pueda almacenar los datos de los empleados de la pizzería. Por este motivo, pensamos en poner sus nombres, apellidos, puestos, salarios, fechas de incorporación, direcciones, género, edad, estado civil y aficiones. Para ello, si le damos formato JSON, nos quedaría algo así:

```JSON
{"Nombre":"Miguel",
"Apellido":"Maino",
"Puesto":"CEO",
"Salario":"92000",
"FechaDeIncorporacion":"2013-01-22",
"Direccion":"Calle compostela 12",
"Genero":"Hombre",
"Edad":25,
"EstadoCivil": "Casado",
"Aficiones":"Cine,Teatro,Pintar"}
```

Para poder incorporar estos datos, se debe crear un Index y su Type (hasta la versión 6, un Index podía tener varios Type pero, ahora que la última versión es la 6, el Index solo puede tener un Type).

Creamos el tipo de empleados y, como toda tecnología JSON es auto explicativa, es mejor partir de los ejemplos que partir de la teoría. Los Type son los habituales en la mayoría de los lenguajes de programación.

```JSON
{
  "mappings": {
    "empleados": {
      "properties": {
        "Nombre": { "type": "text" },
        "Apellido": { "type": "text" },
        "Puesto": { "type": "text" },
        "Salario": { "type": "integer" },
        "FechaDeIncorporacion": { "type": "date", "format": "yyyy-MM-dd" },
        "Direccion": { "type": "text" },
        "Genero": { "type": "text" },
        "Edad": { "type": "integer" },
        "Aficiones": { "type": "text" }
      }
    }
  }
}
```

Para dar de alta el Index y su Type (los llamaremos pizzeriamilan y empleados respectivamente), se usa el comando PUT. La sentencia que se ejecutaría en curl quedaría de la siguiente manera:

```bash
curl -XPUT 'localhost:9200/pizzeriamilan?pretty' -H 'Content-Type: application/json' -d '{"mappings":{"empleados":{"properties":{"Nombre":{"type":"text"},"Apellido":{"type":"text"},"Puesto":{"type":"text"},"Salario":{"type":"integer"},"FechaDeIncorporacion":{"type":"date","format":"yyyy-MM-dd"},"Direccion":{"type":"text"},"Genero":{"type":"text"},"Edad":{"type":"integer"},"Aficiones":{"type":"text"}}}}}'
```

El nombre del Index siempre tiene que ir en minúscula. Además, en la versión 6 de ES, a un Index solo puede agregársele un Type; mientras que, en versiones anteriores, un Index podía tener varios Type.

Una vez ejecutada la anterior sentencia, se podría ver algo similar a la siguiente captura de pantalla:

<img width="735" height="485" alt="image" src="https://github.com/user-attachments/assets/393061a6-c569-4417-928d-a705d0d37e52" />

A continuación, creamos un fichero para poder incorporar los datos de los empleados. Aunque hay formas de insertarlos uno a uno, la incorporación mediante ficheros con múltiples registros —podría tener solo uno— es más útil.

Este formato consiste en dos líneas por cada registro: una donde se pone el Index y, en otra, el Type del registro, también en formato JSON, del registro a insertar.

```JSON
{"index":{"_index":"pizzeriamilan","_type":"empleados"}}
{"Nombre":"Miguel","Apellido":"Maino","Puesto":"CEO","Salario":"92000","FechaDeIncorporacion":"2013-01-22","Direccion":"Calle compostela 12","Genero":"Hombre","Edad":25,"EstadoCivil":"Casado","Aficiones":"Cine,Teatro,Pintar"}

{"index":{"_index":"pizzeriamilan","_type":"empleados"}}
{"Nombre":"ELMA","Apellido":"CUBERO","Puesto":"Contable","Salario":"30000","FechaDeIncorporacion":"2015-01-27","Direccion":"Calle Peloponeso","Genero":"Mujer","Edad":21,"EstadoCivil":"Soltero","Aficiones":"R/C Aviones,Cine"}.....
```

El fichero pizzeriamilan.dataset.json, en la ruta /home/code/materialcurso, está ya creado en el formato adecuado y con la inserción de 37 registros. Una vez en esa ruta, se ejecuta el comando:

```bash
curl -XPUT 'localhost:9200/pizzeriamilan/_bulk' -H 'Content-Type: application/json' --data-binary @pizzeriamilan.dataset.json
```

La salida de este comando será algo similar a esto:

<img width="724" height="312" alt="image" src="https://github.com/user-attachments/assets/b2241829-6b09-472e-9ac9-2dccdef0dcf8" />

Con el fin de comprobar que hemos insertado todos los documentos, podemos hacer una consulta para contar todas las filas. Como son consultas, se usa GET:

```bash
curl -XGET 'localhost:9200/pizzeriamilan/_count'
```

Para comprobar que hemos insertado todos los documentos, podemos hacer una consulta para contar todas las filas. Como es una consulta, se usa el comando GET y la salida es:

```bash
{"count":37,"_shards":{"total":5,"successful":5,"skipped":0,"failed":0}}
```

Dentro del Chromium, está instalado el plugging Elasticsearch Head. Este es un plugging que nos facilita ver de forma más visual el resultado de las consultas.

<img width="684" height="340" alt="image" src="https://github.com/user-attachments/assets/436d9228-a25a-40ee-a7af-8ed667786584" />

Aquí podemos ver fácilmente el índice y la cantidad de documentos insertados, que, en este caso, son 37 documentos.

<img width="1053" height="677" alt="image" src="https://github.com/user-attachments/assets/0c815e83-bb77-4d88-9bb7-efa38394f3b6" />

Consulta mediante range. Se trata de un tipo de consulta que busca una serie de valores entre un mayor y menor, ambos incluidos. Para esta consulta, si se quieren ver las fechas, por ejemplo, entre el 10/12/2011-12/12/2012:

```bash
curl -XGET 'http://localhost:9200/pizzeriamilan/_search?pretty=true' -H 'Content-Type: application/json' -d '{
  "query": {
    "range": {
      "FechaDeIncorporacion": {
        "from": "2011-12-10",
        "to": "2012-12-12"
      }
    }
  }
}'
```

Este comando es similar al que se ejecutaría en ES Head en la pestaña de Any Request. Aquí es igual que con curl, pero solo poniendo la query. En la query: http://localhost:9200/pizzeriamilan/

```JSON
{
  "query": {
    "range": {
      "FechaDeIncorporacion": {
        "from": "2011-12-10",
        "to": "2012-12-12",
        "format": "yyyy-MM-dd"
      }
    }
  }
}
```

<img width="936" height="687" alt="image" src="https://github.com/user-attachments/assets/63788e01-c5f3-4664-9b5c-29235c356f69" />

Otra de las búsquedas por rango puede llevarse a cabo mediante el rango de cantidades. En este ejemplo, podemos buscar aquellos sueldos que estén entre 35 000 y 50 000.

Como es formato JSON, no se pueden usar los símbolos > o <. Por tanto, se usa greater than (gt) o lower than (lt). Se agrega la “e” (or equals); en resumen, gte (Greater or Equal than).

```JSON
{
  "query": {
    "range": {
      "Salario": {
        "gte": "35000",
        "lte": "50000"
      }
    }
  }
}
```

El comando en curl equivalente es:

```bash
curl -XGET 'http://localhost:9200/pizzeriamilan/_search?pretty=true' -H 'Content-Type: application/json' -d '{
  "query": {
    "range": {
      "Salario": {
        "gte": "35000",
        "lte": "50000"
      }
    }
  }
}'
```

<img width="936" height="687" alt="image" src="https://github.com/user-attachments/assets/4457f74e-1cd2-4cbe-b21e-2a6d3b3b446d" />

> **Ejemplo**
>
> Por ejemplo, queremos buscar a una persona que sabemos que se apellida Pérez, pero no recordamos bien su nombre. Para ello, usamos la sentencia term, que nos indica una igualdad.

```JSON
{"query":{"term":{"Apellido":"perez"}}}
```

> La misma sentencia con *curl* sería:

```bash
curl -XGET 'http://localhost:9200/pizzeriamilan/_search?pretty=true' -H 'Content-Type: application/json' -d '
{"query":{"term":{"Apellido":"perez"}}}'
```

> Es importante fijarse en que la búsqueda se hace con el apellido en minúsculas.

Aprovechando este ejemplo, vamos a explicar el concepto de tokenización e índice inverso que usa ES.

- Tokenización

    En ES, por defecto, la información que se le pasa en cada campo se almacena como palabras separadas, tomando como separación los espacios en blanco. Es decir, “calle Rosa Matías”, lo almacenará como tres palabras. Además, por defecto, para evitar problemas de mayúsculas y minúsculas, las almacena preferiblemente en minúsculas, esto es, lo almacena como tres palabras: Calle,Rosa,Matías.

- Índice inverso

    Se trata de un paradigma de almacenamiento de ES. En concreto, por cada palabra que almacena (recordad que las convierte todas en minúsculas), crea una entrada en el índice, el número de veces que se repite (si ya existe) y los documentos y campos a los que pertenece. En concreto, en este ejemplo, dado que pérez está en dos documentos, el índice será algo similar a:

    |Palabra|Nº de Documentos|Documentos|
    |-------|----------------|----------|
    |pérez|2|"_id" : "5q5ke2UBzFOlmWbGc8fr", "_id" : "6a5ke2UBzFOlmWbGc8fr"|

    <img width="969" height="745" alt="image" src="https://github.com/user-attachments/assets/c5765e52-7862-4fcb-a29f-035456b08ca7" />

Modificar (updatear) datos: vamos a imaginar que, en el caso de los dos “Pérez”, uno de ellos, Andreas, es en realidad “Péres” (terminado en s).

Para ello:

- Primero, tenemos que identificar el documento. El documento se identifica por el campo _id. Este campo lo puede dar ES de forma automática, o bien nosotros le decimos de cuál se trata. Si es automático, como en nuestro ejemplo, en cada sistema será diferente.
- Una vez encontrado el ID, se ejecuta la acción:

    ```bash
    curl -X POST "localhost:9200/pizzeriamilan/empleados/5q5ke2UBzFOlmWbGc8fr/_update?pretty" -H 'Content-Type: application/json' -d '{ "doc": { "Apellido": "Peres" }}'
    ```

> **Nota**
>
> El ID es aleatorio; por tanto, esta consulta al copiar y pegar de forma literal puede dar error, hay que cambiar el id.

<img width="730" height="360" alt="image" src="https://github.com/user-attachments/assets/74950e8a-5f74-4400-84d5-07db1af681b7" />

Se puede hacer la consulta {"query":{"term":{"Apellido":"peres"}}} y podemos ver cómo Andreas ha cambiado de nombre.

- La otra operación de modificación que nos queda es la del borrado. Si continuamos con el mismo ejemplo, se puede imaginar que el otro Pérez que nos queda, Tasha Pérez, ha salido de la empresa. Por lo tanto, tenemos que borrarlo del índice y sabemos, por la consulta anterior, que su id es: 6a5ke2UBzFOlmWbGc8fr.

    ```bash
    curl -X DELETE "localhost:9200/pizzeriamilan/empleados/6a5ke2UBzFOlmWbGc8fr"
    ```

    La salida será algo similar a esto:

    ```JSON
    {
      "_index": "pizzeriamilan",
      "_type": "empleados",
      "_id": "6a5ke2UBzFOlmWbGc8fr",
      "_version": 2,
      "result": "deleted",
      "_shards": {
        "total": 2,
        "successful": 1,
        "failed": 0
      },
      "_seq_no": 7,
      "_primary_term": 1
    }
    ```

- También puede haber consultas de agregación y estadísticas. Se va a ver la denominada como stats, la cual nos proporciona un número de registros, mínimo, máximo y media. Así, la sentencia que habría que ejecutar en la consola sería la siguiente:

    ```bash
    curl -X POST "localhost:9200/pizzeriamilan/empleados/_search?size=0" -H 'Content-Type: application/json' -d '{
      "aggs": {
        "Estadisticas Principales": {
          "stats": {
            "field": "Salario"
          }
        }
      }
    }'
    ```

    La misma sentencia en ES Head sería:

    ```bash
    {
      "aggs": {
        "Estadisticas Principales": {
          "stats": {
            "field": "Salario"
          }
        }
      }
    }
    ```

    <img width="729" height="454" alt="image" src="https://github.com/user-attachments/assets/5cc8be0d-a498-488d-aa60-046be1c200b1" />
