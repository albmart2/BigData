# Caso práctico
## Se pide
Haciendo uso de Pentaho Business Analytics, el departamento de ventas de una compañía, realizar un modelo multidimensional OLAP de prueba, para poder realizar un análisis de la información departamental.

Para ello, el departamento de ventas facilita un fichero fuente de datos, a partir del cual hay que diseñar el modelo multidimensional que implementar:
- Se puede descargar dicho fichero de datos en el siguiente enlace: Datos_Ventas_Limpios.csv
- Este fichero se adjunta también en la máquina virtual.

El objetivo es generar una solución que proporcione al equipo de ventas la capacidad de analizar sus datos mediante informes dinámicos OLAP.

<img width="1579" height="647" alt="image" src="https://github.com/user-attachments/assets/eec21cbe-c4db-49e2-b86e-712f97b9af7e" />

## Solución

Para plantear la solución de este caso práctico, primero hay que hacer un rápido análisis del enunciado. Es evidente que es bastante abierto, por lo que podrían admitirse varias soluciones.

Para realizar este rápido análisis, será conveniente hacer uso de conceptos explicados en unidades anteriores.

En primer lugar, el enunciado solicita hacer uso de la solución Pentaho Business Analytics, que es una solución HOLAP, aunque aquí se utilizará como ROLAP, u OLAP sobre relacional, lo que implica que se debe usar una base de datos relacional para implementar la capa física y una capa de metadatos para implementar el modelo lógico multidimensional.

Del mismo modo, el enunciado indica que se trata de una prueba de concepto para determinar la viabilidad de este desarrollo, lo que implica carácter local y temporal del desarrollo. Con este requerimiento, es recomendable plantear una estrategia de diseño inicial de Kimball o bottom-up que permita comenzar a nivel local o departamental, para escalar al resto de la organización.

Sin embargo, el carácter de prueba que se señala en el enunciado hace que sea más conveniente utilizar herramientas ágiles de modelado, orientadas a obtener un resultado final que el usuario pueda explotar y evaluar, que el método tradicional de diseño e implementación, que puede ser más profundo, pero también más lento. Es por ello que, para este caso, en vez de crear un proceso ETL específico para la fuente de datos identificada, y generar un almacén de datos físico sobre la base de datos relacional, se realizará una implementación ágil del modelo lógico multidimensional, que se encuentra por encima del modelo físico, obviando, por tanto, este modelo físico y haciendo que Pentaho cargue en memoria los datos directamente.

<b>Para realizar el modelo multidimensional</b>, hay que acceder a la máquina virtual.

Para acceder a la PUC de Pentaho Business Analytics, hay que asegurarse de que está el servicio arrancado haciendo doble clic en “<b>start-pentaho.batch</b>”, que se encuentra en el escritorio. En la máquina virtual, hay que acceder a la URL <b>localhost:8080</b> del navegador Edge, y loguearse como usuario <i>Admin</i>. 

<img width="1579" height="647" alt="image" src="https://github.com/user-attachments/assets/ba8cdd46-ed0a-4ee0-99fe-8b6eb0c5d9d6" />

Una vez en la PUC de Pentaho, para crear el modelo multidimensional, hay que identificar la nueva fuente de datos, en este caso, el fichero. Para ello, hay que acceder a la opción del menú lateral <b>Manage Data Sources</b>.

<img width="965" height="469" alt="image" src="https://github.com/user-attachments/assets/6591235a-2cff-4b8f-b04f-c3c5743dd166" />

Ahora, se debe seleccionar la opción <b>New Data Source</b> en el nuevo menú que aparece.

<img width="652" height="489" alt="image" src="https://github.com/user-attachments/assets/25039791-aade-4925-81c7-a46d726a45c0" />

Esta opción lanzará un proceso a modo de Wizard que permitirá crear e identificar la fuente de datos y el modelo que se quiere implementar.

El primer paso es seleccionar la fuente de datos, en este caso, un fichero CSV, por lo que hay que seleccionar un nombre para esta nueva fuente y el tipo de fuente (CSV, en este caso).

<img width="691" height="638" alt="image" src="https://github.com/user-attachments/assets/d5134a93-7aa9-4e6c-88a5-70eb2e529a16" />

Una vez seleccionado el tipo de data source, se podrá importar el fichero CSV de la ruta donde esté ubicado.

<img width="690" height="573" alt="image" src="https://github.com/user-attachments/assets/795862c7-fcf1-4f72-9338-1270b48855be" />

Una vez importado, será necesario configurar tanto el <i>encoding</i> usado por el fichero como el delimitador de campos usados y de texto.

Se podrán ver en todo momento los datos que se van recuperando en la parte inferior de la pantalla del proceso.

<img width="963" height="796" alt="image" src="https://github.com/user-attachments/assets/30c4ab2d-2639-4deb-adde-f59911c5c228" />

Es importante asegurarse de que los datos se previsualizan bien y usar los separadores adecuados.

Tras esto, hay que hacer clic sobre Next para pasar a la siguiente fase.

A continuación, Pentaho proporciona un listado de todos los nombres de campos con una descomposición de tipos, longitud y formato para cada uno de ellos, y la posibilidad de modificarlos o ajustarlos al criterio propio.

<img width="962" height="790" alt="image" src="https://github.com/user-attachments/assets/1824d8cf-a17a-4ea1-b3bf-e0c5564ac57c" />

Cuando se ha finalizado, hay que clicar sobre el botón Finish para terminar con la importación de la nueva fuente de datos.

Este último paso dará lugar a la carga automática en memoria de los datos, para su posterior explotación, y dará comienzo el proceso de creación del modelo multidimensional.

En este proceso, Pentaho ha creado una tabla de datos relacional que conformará el modelo físico del nuevo modelo: se trata de la capa física, pero, como ya es sabido, se necesita, además, una capa lógica, donde se define el modelo multidimensional, que es lo que permite traducir/ejecutar un motor OLAP multidimensional de Pentaho (Mondrian) sobre una base de datos relacional.

Wizard de Pentaho lanza automáticamente la fase de creación del modelo multidimensional. Y para ello da la opción de crear uno por defecto automático o customizarlo/crearlo uno mismo. Se elegirá esta segunda opción para ver qué es lo que realmente se está haciendo.

<img width="918" height="768" alt="image" src="https://github.com/user-attachments/assets/5ad4f3f0-d102-4e0b-b601-f06026a64ee1" />

Una vez que se ha indicado que se desea crear un modelo propio, hay que acceder a un editor ligero de creación de cubos OLAP.

En una primera aproximación, Pentaho propone el modelo más sencillo de cubo, que sería el que considera cada campo de tipo texto como dimensión, y cada campo de tipo numérico como métricas.

Sin embargo, esto no es lo que aquí se está buscando, por lo que habrá que rehacerlo desde el principio. Para ello, se borra la propuesta por defecto clicando sobre el botón <i>Clear model</i>.

<img width="963" height="634" alt="image" src="https://github.com/user-attachments/assets/455fc092-df1a-4c49-8d21-8ed24a7c156c" />

Se acepta. Esto borrará todo el modelo inicial.

<img width="923" height="609" alt="image" src="https://github.com/user-attachments/assets/1589c1cd-dbdd-48a9-bcb2-c474bc74063b" />

Como se ha visto en las unidades anteriores de este módulo, para crear el modelo lógico, es necesario identificar y definir las dimensiones, jerarquías, niveles, atributos, métricas y agregaciones.

Hay que ir definiendo sobre Pentaho los datos de ventas de entradas de los que se dispone.

Como siempre, la primera dimensión que ha de identificarse es el <i>Tiempo</i> (o temporal). Esta dimensión siempre debe estar presente en todo cubo multidimensional y, por norma general, en todo almacén de datos o <i>data warehouse</i>. Es importante recordar que el <i>data warehouse</i> tiene una de característica que destaca sobre el resto de bases de datos: su cualidad de almacenar y mantener la información histórica. Este hecho hace que una de las principales capacidades del <i>data warehouse</i> sea la posibilidad del análisis de los datos a lo largo del tiempo, y es por ello que el eje temporal, o dimensión temporal, es el más relevante en cualquier modelo multidimensional.

Para crear la dimensión, hay que arrastrar el campo <i>YEAR_ID</i> sobre Dimensiones y soltarlo:

<img width="962" height="518" alt="image" src="https://github.com/user-attachments/assets/654a8997-d95d-4d2e-a84b-a1996caa42ca" />

Esta acción creará por defecto una dimensión, una jerarquía y un primer nivel, todos ellos con el nombre del campo, por defecto.

<img width="622" height="420" alt="image" src="https://github.com/user-attachments/assets/56ede7e2-8aae-4cbb-893d-54ec1ba51f5f" />

A continuación, hay que particularizar la definición de la dimensión:

- Renombrar la dimensión como Tiempo e identificarla como dimensión temporal.
- Renombrar la jerarquía con un nombre indicativo. En este caso se desea crear una jerarquía de tres niveles: año, mes y fecha, por lo que se renombra como A-M-Fecha.
- Renombrar el nivel como Año.

<img width="962" height="630" alt="image" src="https://github.com/user-attachments/assets/dceb7613-ffc7-4a9e-bf01-a4aac765ef3b" />

En el nivel Año, es importante también identificar el tipo de nivel temporal a Pentaho, así como el formato de columna.

<img width="680" height="456" alt="image" src="https://github.com/user-attachments/assets/f9c88dc6-4add-4f16-b9b3-500ddd6adaed" />

A continuación, para agregar un nuevo nivel a la jerarquía generada A-M-Fecha, se arrastra el campo MONTH_ID y se deja caer sobre el nombre de la jerarquía. Como se puede apreciar en la siguiente captura de pantalla, se creará un nuevo nivel, a la misma altura de Año, pero con un nivel inferior. Es importante guardar el orden descendente de los niveles. No sería correcto definir primero los meses y por debajo los años.

Se configuran el resto de opciones como se ha hecho con los años:

<img width="963" height="636" alt="image" src="https://github.com/user-attachments/assets/e63ba842-f402-4323-a62a-7f569b46f979" />

Para incluir el último nivel de esta jerarquía, se repite el proceso. Se arrastra el campo a la jerarquía, se renombra y se configura.

<img width="807" height="535" alt="image" src="https://github.com/user-attachments/assets/025b8af1-9ec9-457b-96b8-24914d2b0edd" />

El modelo ya dispone de una dimensión completamente funcional: la dimensión Tiempo. Sin embargo, el cubo o modelo no es completo, pues, como mínimo, es necesario definir una métrica.

Para definir las métricas directas hay que recordar que estas están compuestas por un campo/valor y una función de agregación que indica al motor OLAP de Pentaho cómo debe agregar la información cuando se trabaja a niveles superiores de información.

Para crear la métrica, en este caso basta con identificar el campo que contiene los datos de interés, arrastrarlos y soltarlos sobre el grupo de métricas. Por ejemplo, el campo QUANTITYORDERED.

En este caso, se renombra como Cantidad Pedida y se le asigna una función de agregación SUM, de suma, que será la función que se aplique para agregar a niveles superiores.

<img width="963" height="628" alt="image" src="https://github.com/user-attachments/assets/240e7bf2-45ae-4590-98bb-ba1bcf1afb84" />

El modelo ya es funcional, pero se trata de un modelo mínimo (1 dimensión + 1 métrica): su capacidad de análisis sería muy limitada, prácticamente, lo único que podría mostrar sería el comportamiento de los pedidos a lo largo del tiempo.

Así pues, a continuación, se mostrará cómo enriquecer el modelo para ganar en capacidad de análisis.

Hay que generar una nueva jerarquía en la dimensión Tiempo. Esto permitirá que los usuarios puedan navegar por la información de diferente manera y, por tanto, también podrán analizarla de distintos modos.

Téngase presente que una dimensión puede tener una o más jerarquías. En este caso, lo que se desea es crear una jerarquía que solo contenga dos niveles: años y trimestres. Para crear esta segunda jerarquía en la dimensión Tiempo, hay que arrastrar el campo YEAR_ID, como ya se hizo, pero, esta vez, dejándolo caer sobre el nombre de la dimensión. La siguiente captura de pantalla muestra el resultado:

<img width="962" height="631" alt="image" src="https://github.com/user-attachments/assets/bd28852f-bc26-47eb-ba41-681cfa40cc90" />

A continuación, hay que renombrar la jerarquía, esta vez como A-Q, y configurar los niveles: tanto el nivel año ya agregado, como el nivel QTR ID, que también se arrastra:

<img width="815" height="538" alt="image" src="https://github.com/user-attachments/assets/e7c99d41-d71e-48e7-afdd-d2114b8c9efb" />

Hay que repetir este proceso con el resto de las dimensiones que quieran crearse. La siguiente dimensión que se propone es la geográfica.

Para ello, se arrastran los campos, se renombran y configuran, tal y como se muestra en la siguiente imagen:

<img width="962" height="630" alt="image" src="https://github.com/user-attachments/assets/6b35f4f0-2245-46cd-9aa4-27f788aa2d99" />

Para ello, hay que crear una jerarquía de cinco niveles: desde Territorio hasta Código postal.

<img width="873" height="574" alt="image" src="https://github.com/user-attachments/assets/47ef729b-49c3-436f-867c-495d19760adb" />

Una vez configurados y renombrados todos los niveles, se crea una segunda jerarquía, como, por ejemplo, País y Ciudad, con el objetivo de que el usuario pueda analizar más rápidamente sin tener que bajar tantos niveles.

El proceso de diseño es idéntico al mencionado en párrafos anteriores. Únicamente es necesario particularizar nombre y campos.

<img width="963" height="635" alt="image" src="https://github.com/user-attachments/assets/2a2865bf-ebde-4612-ace7-fe70a6f84d50" />

La siguiente dimensión que debe crearse es Cliente, a partir del campo CUSTOMERNAME:

<img width="824" height="546" alt="image" src="https://github.com/user-attachments/assets/9f9449e0-11a3-4e4f-ab7b-2a5d4ea8bac8" />

A continuación, se repite el proceso para editar y modificar el nombre de dimensión, jerarquía y nivel:

<img width="963" height="634" alt="image" src="https://github.com/user-attachments/assets/661c0e73-fb5b-4a54-ac3f-398e886541e8" />

Se repite también el proceso para la dimensión Tamaño Acuerdo, a partir de la columna DEALSIZE:

<img width="868" height="573" alt="image" src="https://github.com/user-attachments/assets/245b226f-a0b0-4184-bf1f-2c4824965eb0" />

Se repite también el proceso para editar y modificar el nombre de dimensión, jerarquía y nivel:

<img width="963" height="633" alt="image" src="https://github.com/user-attachments/assets/38da9e1b-6df6-4ca4-8732-be3f6a7f7065" />

Se repite el proceso para la dimensión Estado, a partir de la columna STATUS:

<img width="963" height="633" alt="image" src="https://github.com/user-attachments/assets/07e742fa-bf9a-443d-959f-93727c80606f" />

Se repite el proceso para editar y modificar el nombre de dimensión, jerarquía y nivel:

<img width="962" height="632" alt="image" src="https://github.com/user-attachments/assets/0d136195-d976-4bb3-b1c5-4a5014be13a4" />

Y, por último, se añade una última dimensión, Línea de Producto, a partir de la columna PRODUCTLINE:

<img width="908" height="600" alt="image" src="https://github.com/user-attachments/assets/ef57a62d-f11c-4aa9-9357-60fae5e23ef3" />

Se repite el proceso para editar y modificar el nombre de dimensión, jerarquía y nivel:

<img width="962" height="630" alt="image" src="https://github.com/user-attachments/assets/b8902d13-5623-435f-874a-ec7e96f430ce" />

El modelo ya cuenta con seis dimensiones para poder analizar la información. Se añadirá una métrica más, que en este caso sería la métrica por defecto o básica: las ventas.

Para ello, y como ya se vio con la métrica anterior, se crea la métrica directa Ventas, a partir del campo SALES, y se define como función de agregación la suma, SUM:

<img width="861" height="572" alt="image" src="https://github.com/user-attachments/assets/4c0b9d62-6c68-4965-9be6-e29b64f27e3b" />

Por lo que el modelo quedaría del siguiente modo:

<img width="281" height="324" alt="image" src="https://github.com/user-attachments/assets/398faa18-4ab8-432d-ac38-c62c8806719e" />

Una vez finalizado el modelo, hay que clicar sobre OK para que Pentaho guarde el modelo lógico o cubo en el repositorio y poder trabajar con él:

<img width="861" height="1111" alt="image" src="https://github.com/user-attachments/assets/534937f4-f691-43f4-ac04-1695ea4a2e86" />

En este momento, el departamento de ventas ya tendría disponible un cubo multidimensional OLAP para poder hacer informes dinámicos OLAP y analizar la información, tal y como solicitaba el enunciado.

Para ver un ejemplo de cómo los usuarios utilizarían el modelo, a continuación, se creará un informe dinámico. Para ello, hay que clicar sobre la opción de crear nuevo contenido, Create New, y seleccionar un visor OLAP de los que hay disponibles en el entorno (Pivot4j view, Saiku Analytics, jPivot View).

Por ejemplo, se usará Visualizer:

<img width="508" height="393" alt="image" src="https://github.com/user-attachments/assets/fd5d1387-d1db-41ff-8c35-e7cf8f22cbab" />

Se abrirá la opción de visualizar, desde donde se podrán configurar una serie de visualizaciones desde distintas fuentes.

Así, se arrastran los objetos que se quieren configurar para la visualización, en este caso, una tabla cruzada y un gráfico de barras que luego se filtrarán para permitir el análisis.

<img width="292" height="648" alt="image" src="https://github.com/user-attachments/assets/0b7d33de-12a0-4901-a712-d67fe0a8fb21" />

En el caso de la tabla cruzada, hay que seleccionar la fuente de datos, filas y columnas que la componen, así como la métrica que se va a mostrar.

<img width="1680" height="584" alt="image" src="https://github.com/user-attachments/assets/57730163-3b1c-406f-be2a-bca487319108" />

El gráfico de barras se configura de forma similar:

<img width="1680" height="616" alt="image" src="https://github.com/user-attachments/assets/a7614722-d954-419f-bd2e-720a52a78716" />

Se puede retocar el formato en la pestaña de Style.

<img width="1680" height="624" alt="image" src="https://github.com/user-attachments/assets/60e23a21-5691-4fb5-bb6f-01d94420f837" />

Por último, se añaden los filtros.

<img width="827" height="497" alt="image" src="https://github.com/user-attachments/assets/075072f2-2573-4380-aea9-a2a79e4996a6" />

Como resultado final, el departamento dispone de una solución de inteligencia de negocio para dar respuesta a las necesidades de prueba de los usuarios demandantes. Se ha creado en esta práctica un cubo en memoria temporal, para que se realicen los análisis y pruebas necesarios.
