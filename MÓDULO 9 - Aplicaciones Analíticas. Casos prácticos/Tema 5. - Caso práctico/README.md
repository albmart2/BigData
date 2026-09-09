# Ejercicio guiado: caso de oficinas de turismo en Madrid

Una vez que en la unidad se han planteado una serie de ejemplos prácticos de las posibilidades de la analítica espacial, en esta sección se va a ver un caso completo de este tipo de analítica.

El problema planteado consiste en que una empresa quiere establecer en Madrid cuatro oficinas de servicios turísticos para clientes de hoteles en el centro de la ciudad. En función de la analítica espacial, tenemos que ayudar a decidir dónde se aconseja la ubicación de dichas oficinas. En este contexto y siguiendo el esquema de monetización de datos inspirado en lo que se ha explicado en la unidad (sintetizado en la figura 5), vamos a resolver este problema de decisión.

> **Anotación**
> 
> Tanto los datos necesarios para la resolución de este ejercicio como los requisitos de entorno son los mismos que en el apartado “Análisis avanzado de mapas”.

Preparación del entorno:

- Sustituir *midirectorioGEO* por la ruta completa de dicho directorio.

    <img width="447" height="72" alt="image" src="https://github.com/user-attachments/assets/a916171d-9bc3-489b-9d16-287539a6a233" />

- Vamos a usar la función rgdal, rgeos.

    <img width="499" height="297" alt="image" src="https://github.com/user-attachments/assets/ee31d8b6-84ab-4673-a0ba-735894c35c83" />

Una vez realizadas estas acciones, vamos a seguir los siguientes pasos para resolver el problema:

1. Obtención de datos en crudo.
2. Preprocesamiento de datos.
3. Obtención del *insight*.
4. Presentación de los resultados y decisión final.

## Obtención de datos en crudo

Partimos de datos proporcionados por administraciones públicas y de acceso libre (open data). En concreto, usamos los datos del portal Nomecalles, www.madrid.org/nomecalles/, que están en su mayoría en formato SHP.

La primera fase, por tanto, sería obtener dichos datos y dejarlos en los correspondientes ficheros locales, conforme al siguiente esquema:

<img width="914" height="300" alt="image" src="https://github.com/user-attachments/assets/8506e601-6ab4-460c-944a-de81d5ed8587" />

Por simplificar el ejercicio, esta primera fase ya se da resuelta, de tal manera que esos ficheros se encuentran en el correspondiente directorio *midirectorioGEO/RSpatialTutorial/data* obtenido tal y como se ha explicado en el tutorial del apartado 8.6.

En concreto, en dicho directorio ya se encuentran datos espaciales referidos a hoteles, oficinas turísticas actuales y barrios de Madrid obtenidos originalmente, como se ha comentado, desde www.madrid.org/nomecalles/.

### Hoteles de Madrid, oficinas de turismo y barrios

<img width="740" height="260" alt="image" src="https://github.com/user-attachments/assets/c7fa75f5-4e7c-46b5-a028-ba1182ed41e2" />

## Preprocesamiento de datos

En función de los datos en crudo obtenidos, en esta fase procederemos a preprocesar los datos realizando diversas acciones.

### UNIÓN DE DATOS ESPACIALES DE HOTELES

Unión de datos espaciales de hoteles:

<img width="424" height="185" alt="image" src="https://github.com/user-attachments/assets/2716af07-2d4a-4117-9861-3c7f7512c198" />

### GEORREFERENCIAR Y PROYECTAR LOS DATOS USANDO CÓDIGO EPSG DE MADRID
- Creamos la lista de códigos EPSG disponibles:

    <img width="221" height="42" alt="image" src="https://github.com/user-attachments/assets/c9aabe68-3d64-47bc-9dcb-14e564635c52" />

- Obtener EPSG Madrid:

    <img width="609" height="133" alt="image" src="https://github.com/user-attachments/assets/6892a055-e312-40a5-9326-89c9a9d4507a" />

- Proyección según CRS elegido:

    <img width="685" height="1125" alt="image" src="https://github.com/user-attachments/assets/679b8965-3c3b-419f-b6f6-2294d09c087f" />

### SELECCIÓN DE BARRIOS DEL CENTRO DE MADRID

Selección de barrios del centro:

<img width="685" height="102" alt="image" src="https://github.com/user-attachments/assets/40240106-7517-404e-a560-94837f7fb882" />

Visualización inicial:

<img width="551" height="516" alt="image" src="https://github.com/user-attachments/assets/bcc97be5-33ae-4ed3-bd5d-12c10f754659" />

### *JOIN* ESPACIAL PARA QUEDARNOS SOLO CON LAS OFICINAS TURÍSTICAS DE LOS BARRIOS DEL CENTRO DE MADRID

*Join* espacial: hoteles y oficinas de turismo en el centro:

<img width="721" height="73" alt="image" src="https://github.com/user-attachments/assets/ccdd7108-0c13-40f2-b6de-bc51609320f9" />

Visualización: hoteles y oficinas de turismo en el centro:

<img width="574" height="493" alt="image" src="https://github.com/user-attachments/assets/47f409bf-2549-43b9-b012-0a7942c2d2fd" />

## Obtención del *insight*

Partiendo de los datos preprocesados, realizaremos las siguientes acciones para obtener el oportuno insight (conocimiento) que ayude a la toma de decisiones.

Seguiremos los siguientes pasos:

1. OBTENCIÓN DE LA ZONA DE INFLUENCIA DE LAS OFICINAS TURÍSTICAS ACTUALES DEL CENTRO DE MADRID

    <img width="852" height="45" alt="image" src="https://github.com/user-attachments/assets/086172fe-f1dd-4bb4-a6e6-f7a602b2a65c" />

    *Buffer* objeto espacial: zona de influencia de oficinas de turismo, 500 metros.

2. OBTENCIÓN DE LA ZONA DE INFLUENCIA DE LAS OFICINAS TURÍSTICAS ACTUALES DEL CENTRO DE MADRID

    Visualizamos hoteles, oficinas en el centro y su zona de influencia.
   
    <img width="584" height="149" alt="image" src="https://github.com/user-attachments/assets/a82fe3e6-d1dd-4dc6-bcce-0a939195631b" />

    <img width="288" height="412" alt="image" src="https://github.com/user-attachments/assets/57f3299f-e989-437a-98c7-c010f4f3b8c5" />

3. FILTRADO ESPACIAL

    Filtrado objeto espacial: en principio nos quedamos con los hoteles **dentro** de la zona de influencia de las oficinas de turismo.
   
    <img width="731" height="36" alt="image" src="https://github.com/user-attachments/assets/2f6b1d04-ca91-43ef-97da-79f0fcfe3784" />

    <img width="574" height="185" alt="image" src="https://github.com/user-attachments/assets/cbeda9a9-e76e-48ef-a0df-f4ad5776d540" />

    <img width="213" height="271" alt="image" src="https://github.com/user-attachments/assets/6b1457c1-4738-4744-ab7a-624293a46532" />

    Al principio se identifican hoteles que están dentro de la zona de influencia de las oficinas de turismo.

    <img width="739" height="185" alt="image" src="https://github.com/user-attachments/assets/a59725aa-859c-4519-9377-7426d08f171f" />

    Filtrado objeto espacial: ahora nos quedamos con los que están **fuera** de la zona de influencia.

    <img width="587" height="149" alt="image" src="https://github.com/user-attachments/assets/6f26c44b-e801-4979-b4dd-9761aed38819" />

    Visualizamos.

    <img width="300" height="437" alt="image" src="https://github.com/user-attachments/assets/fd013970-2ea6-41ff-9a88-1f5883fcf0c8" />


4. REALIZAMOS UNA SEGMENTACIÓN CON LAS COORDENADAS DE LOS HOTELES FUERA DE LA ZONA DE INFLUENCIA IDENTIFICADOS ANTERIORMENTE

    <img width="875" height="389" alt="image" src="https://github.com/user-attachments/assets/5abd71cc-9734-4dff-8d98-6923db2cddcd" />

    *Clustering* sobre coordenadas objeto espacial: segmentamos los que están **fuera** de la zona de influencia por sus coordenadas (obtenemos cuatro grupos).

    <img width="333" height="303" alt="image" src="https://github.com/user-attachments/assets/d002bec4-027b-4788-8dd7-0a515971db93" />

    Coordenadas segmentos.

    <img width="716" height="111" alt="image" src="https://github.com/user-attachments/assets/c67222c4-2056-4e58-9173-7094fbc16e43" />

    Se convierten en puntos espaciales y se proyectan.

## Presentación de los resultados y decisión final

Con el conocimiento adquirido gracias al uso de técnicas de *machine learning* en la anterior etapa, procedemos a visualizarlo de cara a ayudar a la toma de decisiones que resuelva el problema planteado.

Visualización:

<img width="875" height="185" alt="image" src="https://github.com/user-attachments/assets/368080bb-ca5b-48c7-b21b-5695b107e3ae" />

<img width="1392" height="764" alt="image" src="https://github.com/user-attachments/assets/03e2108f-1c27-4082-af3c-83513de955f2" />

