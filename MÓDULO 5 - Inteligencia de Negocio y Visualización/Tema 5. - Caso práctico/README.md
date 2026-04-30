
# Caso práctico
## Enunciado
En esta unidad, la práctica consistirá en elaborar un cuadro de mando de marketing basándose en el dataset “Actividades_de_marketing.csv”, el cual se puede descargar en el siguiente enlace:

[Actividades_de_marketing.csv](https://github.com/user-attachments/files/27253665/Actividades_de_marketing.csv)

## Se pide
1. Subir el fichero a Google Big Query.
2. Crear un cuadro de mando de marketing con las siguientes visualizaciones:
    1. Despliegue geográfico de las actividades de marketing.
    2. Distribución temporal por tipo de actividad.
    3. Distribución por tipo de actividad y campaña.
    4. Resultado final, en el que se incluyen filtros del estado de la actividad y grupo de actividad.
  
## Solución

Acceder a la consola de Google Cloud Platform mediante este [link](https://accounts.google.com/v3/signin/identifier?continue=https%3A%2F%2Fconsole.cloud.google.com%2F&dsh=S-670297987%3A1777573171727418&followup=https%3A%2F%2Fconsole.cloud.google.com%2F&osid=1&passive=1209600&service=cloudconsole&flowName=GlifWebSignIn&flowEntry=ServiceLogin&ifkv=AWa2PasO63xy8Jmzcl2jvN137luh5k0GvlfV3X6I47d-3L_JF_baUuKwlqr589BtxoZ0w7o-W9dAMg). Una vez aquí, es fácil logarse con cualquier cuenta de Google. Esto activará el trial de GCP; si los estudiantes no desean usar sus cuentas personales de Gmail, se recomienda crear una alternativa para las prácticas. En esta propuesta se usará test.imf.bd@gmail.com

> Nota: si se realizaron las prácticas de unidades anteriores, no es necesario realizar los pasos 1.1 – 1.3.

1. Subir el dataset a Google Big Query:
    1. Crear proyecto si no existiera.
        1.  Desde el navegador de organizaciones se abre esta ventana y se crea un nuevo proyecto:

            <img width="1418" height="386" alt="image" src="https://github.com/user-attachments/assets/8a798ad9-cb46-49a3-a130-c2ff4f655144" />

        2.  Se asigna un nombre al proyecto:

            <img width="712" height="501" alt="image" src="https://github.com/user-attachments/assets/e4c0f440-e4d8-4c5c-96e4-be65ae4e47b0" />

        3.  Y se selecciona para abrirlo:
      
            <img width="631" height="254" alt="image" src="https://github.com/user-attachments/assets/d1fa6dcf-41c3-42ba-b3db-53972e2c56b9" />
    2. Una vez en el proyecto, abrir Google Big Query.

        <img width="331" height="424" alt="image" src="https://github.com/user-attachments/assets/9ce6d523-2e15-4375-952d-b9b191088c41" />

    3. Crear un conjunto de datos “CP3”.

        1. Una vez está la infraestructura, se crea el primer conjunto de datos, que es donde se crearán las tablas.
  
            <img width="679" height="519" alt="image" src="https://github.com/user-attachments/assets/6ae126a4-1e6d-4abd-982c-2154dd11a968" />

        2. Se le asigna el nombre “CP3” y se crea. Luego se abre el conjunto para poder operar con tablas.
      
            <img width="499" height="710" alt="image" src="https://github.com/user-attachments/assets/121af8b0-00db-4304-b15b-c7371093e05f" />

    4. Crear una tabla para subir datos. Se crea una tabla desde un fichero local o cloud. Estos datos se almacenan como una tabla en Big Query. Se usará el fichero “<b>Actividades de marketing.csv</b>”.

        Crear tabla con datos subidos desde un CSV. Es muy sencillo, solo con cinco clics:
        - Crear tabla.
        - Seleccionar opción “Subir”.
        - Seleccionar el fichero CSV que se quiere subir.
        - Indicar el nombre de la tabla en Big Query.
        - Seleccionar detección automática del esquema.
        - En la opción “Avanzado”, cambiar delimitador por punto y coma.
        - Crear tabla.

        <img width="725" height="874" alt="image" src="https://github.com/user-attachments/assets/f6cad9d1-262c-4594-bf43-b7852c7f41b3" />

    5. Explorar la tabla.

        Una vez creada la tabla, se lanza una sentencia SQL para analizar los datos que contiene. Al seleccionar la opción “Consultar”, el asistente no indica qué columnas mostrar, por lo que hay que indicar el resultado del <i>select</i>.

        <img width="934" height="391" alt="image" src="https://github.com/user-attachments/assets/59984359-c2b7-4c0c-8d50-fb8d32ca9c1c" />

2. Crear el cuadro de mando de marketing:

    1. <b>Despliegue geográfico de las actividades de marketing.</b> En este caso no hay métricas, solo la cuenta de filas que aparecen para cada agrupación de dimensiones. Entonces se muestra por ciudad una cuenta de registros.

        <img width="666" height="393" alt="image" src="https://github.com/user-attachments/assets/a12eca37-8e6f-427b-afd0-bb3e68bdb412" />

    2. <b>Distribución temporal por tipo de actividad.</b> Igual que antes, la métrica es la cuenta de registros desglosada por fecha y tipo de actividad.

        <img width="1159" height="497" alt="image" src="https://github.com/user-attachments/assets/a36ee205-87aa-44b7-b7b7-24646cddb023" />

    3. <b>Distribución por tipo de actividad y campaña.</b> Esta visualización es abierta, se puede solventar con un gráfico de barras o columnas apiladas.

        <img width="639" height="649" alt="image" src="https://github.com/user-attachments/assets/fd7ce51b-3f75-495b-946d-d8513c10e59b" />

    4. <b>Resultado final</b>, en el que se incluyen filtros del estado de la actividad y grupo de actividad.

        <img width="1572" height="801" alt="image" src="https://github.com/user-attachments/assets/1b399588-68e6-4c6c-bd25-6270218d707f" />
