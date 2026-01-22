# Caso Práctico Repaso Final
## Enunciado
1. <b>¿Qué es el Grupo World Bank?</b>

    El Grupo World Bank tiene 189 países miembros, personal en más de 170 países y oficinas en más de 130 ubicaciones. El Grupo World Bank es una asociación global única: consta de cinco instituciones que trabajan en soluciones sostenibles que reducen la pobreza y generan prosperidad compartida en los países en desarrollo. El Grupo World Bank es una de las mayores fuentes de financiación y conocimiento del mundo para los países en desarrollo. Sus cinco instituciones comparten el compromiso de reducir la pobreza, aumentar la prosperidad compartida y promover el desarrollo sostenible.

    El grupo recoge y pone a disposición del público general grandes cantidades de datos. Se pueden estudiar desde aquí.

    Los Archivos protegen la memoria institucional del Grupo World Bank y proporcionan acceso público a los registros del World Bank de Reconstrucción y Fomento (BIRF) y la Asociación Internacional de Fomento (AIF). Este sitio web ofrece una variedad de recursos históricos e información.

2. <b>¿Qué datos vamos a usar?</b>

    En octubre de 2014, el Grupo World Bank lanzó la nueva base de datos SDDS de Estadísticas Trimestrales de Deuda Externa (QEDS). Esta base de datos es consistente con las clasificaciones y definiciones de las Estadísticas de la deuda externa de 2013 (Guía EDS de 2013) y Sexta edición de la Balanza de pagos y el Manual de posición de inversión internacional (BPM6). La base de datos QEDS SDDS proporciona datos detallados de la deuda externa a partir de 1998Q1. Los datos se publican individualmente por países que se suscriben al Estándar Especial de Divulgación de Datos (SDDS) del FMI, así como por los países participantes en el GDDS que están en condiciones de producir los datos de deuda externa prescritos por la SDDS.

    El conjunto básico de tablas se basa en la categoría de datos de deuda externa prescrita en SDDS (Tabla 1) y en las categorías de datos de deuda alentadas (Tablas 2, 3 y 4). La Tabla 1 incluye el desglose de la posición de la deuda externa bruta total por sector, vencimiento e instrumento, y las otras tres tablas, Tabla 2, 3 y 4, recopilan datos sobre el desglose de la deuda externa en moneda nacional y extranjera, el programa de servicio de la deuda a plazo y pagos de capital e intereses adeudados en un año o menos. El conjunto restante de tablas comprende estadísticas suplementarias que van más allá de los requisitos de SDDS para proporcionar presentaciones analíticas adicionales, particularmente con respecto a los datos sectoriales, y facilitar el análisis de datos entre países.

    La fuente consta de dos ficheros, un maestro de países y otro maestro de datos. El maestro de datos tiene un formato que debemos pivotar para ya que las fechas están en columnas en vez de en filas. Además, se debe proceder a limpiar todas las series cuyos valores sean nulos.

    Para la realización del caso práctico se deberán utilizar los archivos “SDDSData.csv” y “SSDSCountryData.csv”.

## Se pide
1. Crear una base de datos de <i>staging</i>.
2. Crear una base de datos de DWH.
3. Realizar una pequeño análisis de los datos.
4. Abrir Spoon de PDI y crear las primeras tareas de integración de datos en la base de datos STG.
5. Crear y cargar el DWH, la tabla “Fact” solo debe almacenar las métricas que tengan valores desde 1998Q1.
6. Crear un <i>job</i> o trabajo con todas las transformaciones en orden que se hayan generado previamente.
7. Crear el <i>data source</i> (cubo) en Pentaho Data Analytics.
8. Crear una visualización con Visualizer.

## Solución

1. Crear una base de datos de staging.

    <img width="571" height="488" alt="image" src="https://github.com/user-attachments/assets/163e7016-f9ab-473d-96b7-7a37d511b93d" />

2. Crear una base de datos de DWH.

    <img width="571" height="552" alt="image" src="https://github.com/user-attachments/assets/bd451d22-2bee-4705-9235-e6af1668840f" />

3. Realizar una pequeño análisis de los datos.

    En esta fase se debe realizar una explicación de los datos que se tienen y su estructura.

    El fichero de datos contiene columnas para país, métricas y una por cada trimestre desde 1998 a 2019. Estos datos se trataran en el paso al DWH.

4. Abrir Spoon de PDI y crear las primeras tareas de integración de datos en la base de datos STG.

    Ahora se configura la salida a base de datos, MiSQL Server local

    <img width="799" height="452" alt="image" src="https://github.com/user-attachments/assets/e8ebbe4e-38b5-4347-a290-a6fdf5f179da" />

    Desde aquí se crea la conexión a base de datos.

    <img width="729" height="349" alt="image" src="https://github.com/user-attachments/assets/c64ae9e2-17eb-430e-8cbf-8ce8cf1657fe" />

    <b>Una vez creada la conexión, seleccionar, con el boton derecho, compartir.</b>

    La carga del CSV de datos es como sigue, usando una transformación.

    <img width="773" height="376" alt="image" src="https://github.com/user-attachments/assets/bf88cc92-2085-4a26-87f7-a293f18b12c8" />

    Repetir pasos para la tabla “STG_COUNTRY”.

    <img width="736" height="296" alt="image" src="https://github.com/user-attachments/assets/8d68b37f-920a-4b37-8386-8727b9e36aab" />
5. Crear y cargar el DWH. La tabla “Fact” solo debe almacenar las métricas que tengan valores desde 1998Q1.
    - Se crea la base de datos.
    - Se crea la tabla “Fact_QEDS”, con los ID componiendo la PK.

      ``` SQL
      CREATE TABLE [dbo].[FACT_QEDS](
        [ID_PAIS] [varchar](3) NOT NULL , [ID_TRIM] [varchar](50) NOT NULL , [ID_METRICA] [varchar]
        (50) NOT NULL , [IN_VALUE] [float] NULL PRIMARY KEY ([ID_PAIS],[ID_TRIM],[ID_METRICA])
      ) ON [PRIMARY]
      ```
    En PDI se crea una transformación con las dos conexiones de base de datos.

    <img width="522" height="212" alt="image" src="https://github.com/user-attachments/assets/9bedc148-6df6-48cf-a4c6-07f99bef103b" />

    Se introduce en la transformación una entrada de tabla.

    <img width="851" height="416" alt="image" src="https://github.com/user-attachments/assets/cad7b129-fa95-4168-9923-a5d1c939fc96" />

    Como existen muchas series de datos que no están completas se van a seleccionar las series que tengan datos desde 1998Q1, añadiendo a la select este filtro:

    ```SQL
    FROM STG_data_SSDSWHERE "Indicator Code" IN (SELECT [Indicator Code]
    FROM [STG_QEDS].[dbo].[STG_data_SSDS] group by [Indicator Code] having count( [a1998Q1] )>1)
    ```
    Así se pasa de 1800 métricas a 159.

    Desde transformaciones con un normalizar filas, se pivotan los datos.

    <img width="761" height="418" alt="image" src="https://github.com/user-attachments/assets/94279ac5-38c0-4c1b-be25-a045e2a51f42" />

    Y se configura de la siguiente forma:

    <img width="680" height="730" alt="image" src="https://github.com/user-attachments/assets/4a7dce25-b8ff-4ee7-b885-2ab1208dafbd" />

    La transformación queda de esta forma.

    <img width="765" height="204" alt="image" src="https://github.com/user-attachments/assets/cf197bf1-80a6-4c82-bec0-d0a97826dd16" />

6. Crear un job o trabajo con todas las transformaciones en orden que se hayan generado previamente.

    <img width="571" height="293" alt="image" src="https://github.com/user-attachments/assets/1ec6e303-5261-43ce-87b3-0ac2f7de44de" />

7. Crear el data source (cubo) en Pentaho Data Analytics.

    Arrancar el servicio con el script que esta en el escritorio “start-pentaho - Acceso directo.bat”.

    Entrar como <i>admin</i> evaluador y generar un nuevo cubo y un <i>data source</i>. Para ello crear un nuevo <i>data source</i> basado en la tabla “FACT_QEDS” que se acaba de crear.

    <img width="571" height="262" alt="image" src="https://github.com/user-attachments/assets/6ef704d4-dff7-4ed3-8756-3e2bb39129f1" />

    Es importante seleccionar opción <i>reporting</i> y <i>análisis</i>.

    <img width="571" height="428" alt="image" src="https://github.com/user-attachments/assets/862411f8-19b2-4d75-aec3-e6d3e7dafde3" />

    Es importante seleccionar tabla de <i>hechos</i> y <i>joins</i>.

    <img width="591" height="839" alt="image" src="https://github.com/user-attachments/assets/b9fe6ae0-67b8-4cd0-80a9-35741f5ec0ad" />

    Editar el cubo por defecto.

    <img width="571" height="340" alt="image" src="https://github.com/user-attachments/assets/44875fea-3363-4ba7-886d-daa3eba78c42" />

8. Crear una visualización con Visualizer.

    <img width="416" height="293" alt="image" src="https://github.com/user-attachments/assets/d7ea1ea3-d4c9-4d31-a5fd-c95d0fa951b2" />

    Para la visualización se usarán los siguientes parámetros:
    - <i>Eje x</i>: Id_trim
    - <i>Leyenda</i>: TableName(Country)
    - <i>Métrica</i>: InValue
    - <i>Filtro</i>: Una id_metrica
  
    <img width="723" height="260" alt="image" src="https://github.com/user-attachments/assets/e0172849-3caf-4e92-99d7-355f0d90e6ca" />
