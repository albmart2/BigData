# Caso práctico
## Enunciado

En esta unidad, la práctica consistirá en subir un data set a Google Big Query y realizar dos análisis sobre los datos.

El dataset es “Sample_Superstore.csv”, que se puede descargar en el siguiente enlace.

[Sample_Superstore.csv](https://github.com/user-attachments/files/27082340/Sample_Superstore.csv)

## Se pide

Realizar las siguientes tareas:
1. Logarse y crear un proyecto.
2. Habilitar Google Big Query.
3. Crear un conjunto de datos.
4. Crear una tabla usando el fichero csv.
5. Explorar la tabla.
6. Una vez subido, realizar los siguientes dos análisis con Data Studio:
    1. Histograma de las ventas por categoría para el año 2018.
    2. Mapa que muestre las ventas por ciudad.
    3. Guardar informe.

## Solución
Acceder a la consola de Google Cloud Platform mediante este link. Una vez aquí, es fácil logarse con cualquier cuenta de Google. Esto activará el trial de GCP; si los estudiantes no desean usar sus cuentas personales de Gmail, se recomienda crear una alternativa para las prácticas. En esta propuesta se usará test.imf.bd@gmail.com.

1. Crear el proyecto.

    Si no existiera: desde el navegador de organizaciones se abre esta ventana y se crea un nuevo proyecto.

    <img width="1418" height="386" alt="image" src="https://github.com/user-attachments/assets/23b06583-e9d5-4301-abbd-2b7602b068ef" />

    <b>Se asigna al proyecto el nombre "test1"</b>

    <img width="712" height="501" alt="image" src="https://github.com/user-attachments/assets/e22457bf-80e7-47a6-82a0-8ad7ea2ba53b" />

    <b>Y se selecciona para abrirlo</b>

    <img width="631" height="254" alt="image" src="https://github.com/user-attachments/assets/034a8ddb-ecd8-4bb2-b8be-c03ce7625ff5" />

2.  Una vez en el proyecto, abrir Google Big Query.

    <img width="331" height="424" alt="image" src="https://github.com/user-attachments/assets/b33c548b-2007-419e-814b-07d399206a20" />

3. Crear un conjunto de datos “CP3”.

    Una vez se tiene la infraestructura, se crea el primer conjunto de datos, que es donde se van a crear las tablas.

    <img width="679" height="519" alt="image" src="https://github.com/user-attachments/assets/6ea16ee6-5cb1-4703-9ef6-c5ed80d2d2c5" />

    <b>Se le asigna el nombre “CP3” y se crea.</b>

    Luego se abre el conjunto para poder operar con tablas.

    <img width="499" height="710" alt="image" src="https://github.com/user-attachments/assets/a5ae25c4-2302-421f-b142-b532ecc40917" />

4. Crear una tabla para subir datos.

    Se crea una tabla desde un fichero local o cloud. Estos datos se almacenan como una tabla en Big Query.

    Se usará el fichero “Sample_Superstore.csv”.

    <b>Crear tabla</b> con datos subidos desde un CSV. Es muy sencillo, solo con cinco clics:

    - Crear tabla.
    - Seleccionar la opción “Subir”.
    - Seleccionar el fichero CSV que se quiere subir.
    - Indicar el nombre de la tabla en Big Query.
    - Seleccionar detección automática del esquema.
    - Crear tabla.
  
    <img width="945" height="924" alt="image" src="https://github.com/user-attachments/assets/6f2dd039-3aeb-43fd-9360-957948b53fe7" />

5. Explorar la tabla.

    Una vez creada la tabla, se lanza una sentencia SQL para analizar los datos que contiene. Al seleccionar la opción “Consultar”, el asistente no indica qué columnas mostrar, por lo que hay que indicar el resultado del <i>select</i>.

    <img width="1098" height="421" alt="image" src="https://github.com/user-attachments/assets/dc01e993-43fb-4117-95c5-b1a7e1dbc7d3" />

6. Análisis.

    Se exploran los datos con Data Studio y se hacen los siguientes análisis.

    <img width="1165" height="417" alt="image" src="https://github.com/user-attachments/assets/34f78d87-6f12-4b66-8a9b-8a9fb5899c7a" />

    1. Histograma de las ventas por categoría para el año 2018.

        <img width="1680" height="869" alt="image" src="https://github.com/user-attachments/assets/6b850084-e6c3-4bba-a7cf-70b08c83e409" />

    2. Mostrar las ventas por ciudad.

        <img width="950" height="682" alt="image" src="https://github.com/user-attachments/assets/7bc09614-7869-40e9-863a-6fde2fd2a459" />

    3. Guardar informe.

        <img width="1506" height="871" alt="image" src="https://github.com/user-attachments/assets/27e5e0c5-f24e-438e-8e2b-806d4a2b1176" />
