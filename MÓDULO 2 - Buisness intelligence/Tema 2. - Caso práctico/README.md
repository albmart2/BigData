# Tema 2. Caso práctico.
## Enunciado
Una compañía del sector financiero realiza el scoring de numerosos clientes y entidades, a partir de los datos e información que recibe de numerosas entidades y fuentes de datos externas.

A diario, esta compañía recibe miles de ficheros que son depositados por fuentes externas en repositorios para ser procesados a continuación y cargarlos en el data warehouse corporativo de la compañía.

Sin embargo, la compañía pretende diseñar un proceso de data quality que permita descartar de forma automática los ficheros fuentes que tengan algún error y cargar únicamente la información que sea correcta.

## Se pide

Realizar el diseño e implementación de una solución sencilla de proceso de data quality que permita verificar, en un proceso previo a la carga en el DW, que la información que se carga cumple unas reglas de formato y negocio definidas por la compañía. En concreto, se solicita:

- Proceso automatizado de data quality.
- Lectura periódica de fichero en formato Excel, .XLS.
- Notificación de error de lectura de fichero o no existencia de fichero en repositorio de destino.
- Aplicación de cuatro reglas de negocio definidas por la compañía.
- Cargar únicamente la información válida en el DW corporativo.
- Enviar notificación a la compañía origen del fichero, para reenvío de información errónea.

Así como la definición de las reglas que deben cumplirse:

- Regla 1:
    - Que CL_RAMO_MOD contenga alguno de estos valores: “14A”, “14D”, “14E”, “14H”, “14L”, “14M”, “14P”, “14R”, “14T”, “14U”, “14Z”.
- Regla 2:
    - Que FECHA_EFECTO sea mayor que FECHA_CALCULO.
- Regla 3:
    - En los casos en los que el campo AGE_AT_ENTRY < 14 -> hay que realizar un recálculo del campo AGE_AT_ENTRY == ROUND((FECHA_EFECTO - FECHA_NACIMIENTO) / 365.25)
- Regla 4:
    - El campo POLIZA debe tener una longitud igual a 9.
 
<img width="1128" height="294" alt="image" src="https://github.com/user-attachments/assets/51ec5d8d-a3fc-45b7-96dc-857ec54c8487" />

## Solución

Este caso se va a afrontar con la herramienta de procesamiento y ETL de Pentaho, Pentaho Data Integration. 

Y, para ello, primero se va a realizar un diseño top-down de la posible solución e implementación, teniendo en cuenta que es una solución recomendada, orientada a que el alumno entienda y asimile algunos conceptos básicos.

Se comienza con el diseño a nivel conceptual, mediante diagramas de flujo, de cómo se van a procesar los datos y qué acciones hay que incluir en el proceso de información:

<img width="894" height="382" alt="image" src="https://github.com/user-attachments/assets/20da7271-2fc2-4c36-9ebc-a7e875387128" />

Para implementar el flujo anterior, se crea un nuevo “trabajo” en PDI:

1. Ir a Archivo > Nuevo > Trabajo.

    <img width="936" height="650" alt="image" src="https://github.com/user-attachments/assets/143e9757-4574-45ea-817a-c9898e9a2b23" />

2. Expandir la carpeta “General” y arrastrar una entrada de trabajo de inicio al espacio de trabajo gráfico. La entrada del trabajo de inicio define dónde comenzará la ejecución.

3. Seleccionar y arrastrar una entrada de inicio o “Start”, que definirá el inicio del trabajo.

    <img width="737" height="550" alt="image" src="https://github.com/user-attachments/assets/a8d0d880-147c-459d-a0a0-0911addf9feb" />

4. Se incluye una entrada para comprobar si el fichero existe en una ubicación específica. Esta entrada falla si no encuentra el nombre exacto del fichero.

    <img width="918" height="644" alt="image" src="https://github.com/user-attachments/assets/3d7eec82-1c9b-4ee5-b27d-1f52bb1075ed" />

5. Se configura la entrada.

    <img width="1359" height="523" alt="image" src="https://github.com/user-attachments/assets/493d6b34-bbfb-4fbf-81a2-e340f386c5cf" />

6. Se incluye una entrada a una transformación para el caso de que sí exista el fichero de datos de entrada. Esta entrada de transformación se diseñará más adelante. 

    Del mismo modo, se incluye una llamada a Abort para abortar el proceso, en caso de que el fichero de entrada no esté disponible.

    <img width="893" height="538" alt="image" src="https://github.com/user-attachments/assets/cf3208d9-51d5-435d-87fe-3b901884bdf7" />

7. El siguiente paso consiste en incluir las notificaciones que necesite el proceso. A continuación, se identifican tres:

    1. Enviar un correo electrónico de notificación a la entidad que envía el fichero, cuando este no se encuentra en la carpeta prevista.
    2. Enviar un correo electrónico a soporte, cuando el proceso de aplicación de las reglas no sea correcto o falle por cualquier motivo.
    3. Tras el procesado de las reglas, filas de datos correctas son almacenadas en el DW, pero las que son erróneas se envían por correo electrónico a las entidades origen.

    <img width="971" height="515" alt="image" src="https://github.com/user-attachments/assets/bc467b59-025b-424d-9670-26ca1ecc6d6c" />

Para realizar el diseño, hay que tener claro cuál es el objetivo que se debe cumplir y plantear una estrategia de diseño. En este caso, se parte de un fichero de entrada, tal y como se muestra a continuación:

<img width="963" height="306" alt="image" src="https://github.com/user-attachments/assets/3f1b3f51-747d-4382-8e5c-65878c8714c6" />

En donde las filas marcadas en rojo no cumplen con alguna de las reglas que hay que aplicar. 

La transformación tendrá, pues, como objetivo verificar fila a fila si cumple o no con cada una de las reglas definidas. El resultado final de esta transformación debe ser diferente para cada caso de fila. Es decir, para las filas que cumplen con todas las reglas, la salida debe ser un fichero igual al de entrada, y se debe incluir esta información en una tabla para su procesamiento en el DW.

Las filas que incumplan una o más reglas deben ser separadas y agrupadas para crear un fichero de salida que contenga la información de entrada, así como la o las reglas que ha incumplido, con el propósito de poder reenviarlo al origen para su corrección.

A continuación, se muestra una posible implementación:

<img width="962" height="518" alt="image" src="https://github.com/user-attachments/assets/aada0a53-9273-48a2-98f2-a5f1a15ee9de" />
