# Caso práctico
## Datos

Haciendo uso de Pentaho Data Integrator, se va a automatizar la integración de un conjunto de datos. Como anteriormente en la demo, se van a usar datos abiertos de la Nasa: NASA Open APIs.

En este caso se quiere automatizar los datos de la API de datos de fireballs. Esta proporciona un método para solicitar registros específicos del conjunto de datos disponible. Cada consulta exitosa devolverá contenido que representa uno o más registros de datos de bola de fuego. Fireball Data API (nasa.gov).

Para ello se realizará una petición de los últimos 50 sucesos y se cargará de forma automática y actualizando los datos con PDI.

<b>Nota</b>: si la API estuviera fuera de servicio temporalmente, se deja un fichero JSON en la carpeta de recursos de la máquina virtual.

## Se pide
Realizar un análisis del conjunto de datos y realizar el proceso de carga con PDI.

## Solución
1. <b>Data set</b>

    La API de datos de bola de fuego proporciona un método para solicitar registros específicos del conjunto de datos disponible. Cada consulta exitosa devolverá contenido que representa uno o más registros de datos de bola de fuego. Consúltese la página de CNEOS sobre bolas de fuego para obtener detalles sobre este conjunto de datos.

    Esta API consta de los siguientes parámetros:
    - <i>date-min</i>: excluir datos anteriores a esta fecha AAAA-MM-DD o fecha/hora AAAA-MM-DDThh: mm: ss.
    - <i>date-max</i>: excluir datos posteriores a esta fecha AAAA-MM-DD o fecha/hora AAAA-MM-DDThh: mm: ss.
    - <i>energy-min</i>: excluir los datos con energía radiada total menor que este valor positivo en julios × 1010 (por ejemplo, 0,3 = 0,3 × 1010 julios).
    - <i>energy-max</i>: excluir datos con energía total radiada mayor que esto (ver energía-min).
    - <i>impact-e-min</i>: excluir datos con energía de impacto estimada menor que este valor positivo en kilotones (kt) (por ejemplo, 0,08 kt).
    - <i>impact-e-max</i>: excluir datos con energía total radiada mayor que esto (ver impacto-e-min).
    - <i>vel-min</i>: excluir datos con velocidad en el pico de brillo menor que este valor positivo en km/s (p. ej., 18,5).
    - <i>vel-max</i>: excluir datos con una velocidad en el pico de brillo mayor que este valor positivo en km/s (por ejemplo, 20).
    - <i>alt-min</i>: excluir datos de objetos con una altitud menor que esta (por ejemplo, 22 significa objetos más pequeños que esto).
    - <i>alt-max</i>: excluir datos de objetos con una altitud mayor que esta (por ejemplo, 17,75 significa objetos más grandes que esto).
    - <i>req-loc</i>: ubicación (latitud y longitud) requerida; cuando se establece en verdadero, excluye los datos sin una ubicación.
    - <i>req-alt</i>: altitud requerida; cuando se establece en verdadero, excluye los datos sin una altitud.
    - <i>req-vel</i>: velocidad requerida; cuando se establece en verdadero, excluye los datos sin una velocidad.
    - <i>req-vel-comp</i>: componentes de velocidad requeridos; cuando se establece en verdadero, excluye los datos sin componentes de velocidad.
    - <i>vel-comp</i>: incluir componentes de velocidad.
    - <i>sort</i>: ordenar datos en el campo especificado: “fecha”, “energía”, “impacto-e”, “vel” o “alt” (el orden de clasificación predeterminado es ascendente: anteponer “-” para descender).
    - <i>limit</i>: limitar los datos a los primeros N resultados (donde N es el número especificado y debe ser un valor entero mayor que cero).

    Generando la siguiente URL, para limitar los últimos 50 eventos con el siguiente resultado: https://ssdapi.jpl.nasa.gov/fireball.api?limit=50

    <img width="1575" height="352" alt="image" src="https://github.com/user-attachments/assets/d3b65abb-41a0-4a57-b18c-b380cd299041" />

    Los datos se devuelven en formato JSON como un solo objeto (tabla hash). El número de registros contenidos en el objeto se indica en la tecla “contar”. En los casos en los que las restricciones especificadas por el usuario son demasiado estrictas (sin resultados coincidentes), solo se devuelven las claves de “recuento” y “firma”, como en el siguiente ejemplo.

    ```JSON
   {
      "count": 0,
      "signature":
        {
          "version": "1.0",
          "source": "NASA / JPL Fireball Data API"
        }
    }
    ```

    Cada registro se proporciona como un elemento del objeto “datos” y cada registro es una matriz de campos. Los nombres de cada campo contenido en cada registro se proporcionan en la matriz de objetos “campos”.

    Los campos se definen de la siguiente manera:
    - <i>date</i>: fecha/hora de brillo máximo (GMT).
    - <i>lat</i>: latitud en el brillo máximo (grados).
    - <i>lon</i>: longitud en el brillo máximo (grados).
    - <i>lat-dir</i>: dirección de latitud (“N” o “S”).
    - <i>lon-dir</i>: dirección de latitud (“E” o “W”).
    - <i>alt</i>: altitud sobre el geoide en el brillo máximo (km).
    - <i>vel</i>: velocidad con brillo máximo (km/s).
    - <i>energy</i>: energía total radiada aproximada (1010 julios).
    - <i>impact-e</i>: energía de impacto total aproximada (kt).
    - <i>vx</i>: velocidad estimada previa a la entrada (componente X centrada en la Tierra, km/s).
    - <i>vy</i>: velocidad estimada previa a la entrada (componente Y centrada en la Tierra, km/s).
    - <i>vz</i>: velocidad est. previa a la entrada (componente Z centrada en la Tierra, km/s).

2. <b>Carga en PDI</b>

    <b>Primero</b> se crean la base de datos en SQL Server y la tabla.
   
    <img width="861" height="1314" alt="image" src="https://github.com/user-attachments/assets/40cdf9e2-8192-45d2-bab5-180a2a801888" />

    Como se ha visto anteriormente en este módulo, se usará PDI para extraer la información desde las API a un fichero o tabla de base de datos.

    Para ello se usará PDI y se creará una transformación que realizará una llamada a la API de datos abiertos de la NASA seleccionada y transformará el fichero JSON en datos estructurados.

    Lo <b>segundo</b> será generar la conexión a la base de datos que se va a usar para cargar datos.

    <img width="1680" height="1034" alt="image" src="https://github.com/user-attachments/assets/4aec2526-7478-4016-8b67-d149f3a5a63b" />

    En <b>tercer lugar</b>, se realizará <b>la llamada al servicio Rest</b>, que devuelve los datos en formato JSON. Para ello se usarán dos objetos:

    <img width="237" height="104" alt="image" src="https://github.com/user-attachments/assets/6ba1a7f6-5702-456f-b5a5-019bd901a2db" />

    <b>Generador de filas</b>. Actúa como trigger para el siguiente paso, si no, no se ejecuta. En este solo se especifica la URL que proporciona los datos.

    <img width="1348" height="582" alt="image" src="https://github.com/user-attachments/assets/d269bf0c-dc86-49f4-a5d0-65f3a8b88dc6" />

    <b>Cliente rest</b>. Este objeto realiza la llamada a la URL y descarga los datos.

    <img width="914" height="752" alt="image" src="https://github.com/user-attachments/assets/2722053f-dd82-4a52-9e22-11528ddde68a" />

    A partir de aquí se realiza el <b>procesado de los datos en formato JSON</b>. Para ello se necesita un conversor de datos en formato JSON. Y luego, dada la estructura en la que se encuentra ese fichero JSON, se realizan un reemplazo de caracteres y una separación de campos.

    <img width="1043" height="363" alt="image" src="https://github.com/user-attachments/assets/d27c4673-8cb7-451e-9c7e-25dcd7384371" />

    1. <b>Json Input</b> parsea el formato JSON:

        Primero se configura la pestaña de fichero, indicando la entrada.

        <img width="1416" height="712" alt="image" src="https://github.com/user-attachments/assets/de2e7f93-be65-4ef9-bb61-e1773a6cde74" />

        Después se configura la pestaña de campos, donde se especifica la ruta de los datos dentro del fichero JSON. Esta sección depende de la composición del fichero JSON.

        <img width="1406" height="362" alt="image" src="https://github.com/user-attachments/assets/f33242a3-4614-453c-ab43-33a15592830b" />

        Si se ejecutamos el paquete de carga hasta este punto, se verá que ya se dispone de los datos, pero <b>en una única columna</b> con corchetes y los campos separados por comas:

        <img width="1003" height="709" alt="image" src="https://github.com/user-attachments/assets/91b12a4c-5706-47a9-b976-5fcfb668c2a1" />

    2. Se reemplazan caracteres del resultado que sobran como [,],”.

        <img width="1505" height="839" alt="image" src="https://github.com/user-attachments/assets/84bd3be6-bb29-464c-908f-6112eac5c627" />

    3. Se separan los campos por un separador dado.

        <img width="1680" height="551" alt="image" src="https://github.com/user-attachments/assets/b1e45ad7-aab0-4f24-8d65-077cce9be3d9" />

    4. Se seleccionan solo los campos que se quieren de salida. Primero se selecciona la opción para traer todos los campos y luego se filtran solo aquellos que se quieren mostrar.

        <img width="1680" height="1123" alt="image" src="https://github.com/user-attachments/assets/1dd37d04-b782-4b81-8e2c-a5aa2db9251c" />

        Por ultimo, hay que definir la salida a la tabla de SQL Server:

        <img width="256" height="234" alt="image" src="https://github.com/user-attachments/assets/8b7c66a9-5cb2-4d85-917b-9232a89d62aa" />

        Reasignando el maping del paso anterior (Seleccionar/renombrar valores 2):

        <img width="1680" height="832" alt="image" src="https://github.com/user-attachments/assets/27d45851-b6c1-4875-a676-08e9a23aed62" />

        Ejecutando la tarea se debe cargar en la tabla final de SQL Server:

        <img width="1371" height="1291" alt="image" src="https://github.com/user-attachments/assets/c27dfc1e-bda7-452d-b8b1-b71a4aa4d9b5" />
