# Caso práctico
## Enunciado

Para este caso práctico se ha elegido un dataset común para ejercicios: “Sample_Superstore.csv”. (Adjuntado abajo).

“Sample_Superstore” es un conjunto de datos de un e-commerce de EE. UU. con datos de 2014 a 2018.

El sector e-commerce, al que se hace referencia como "clics", ha ido aumentando lentamente la cuota de mercado en las últimas dos décadas.

La plataforma de comercio electrónico permite a las personas comprar productos: desde libros, juguetes, ropa y zapatos hasta alimentos, muebles y otros artículos para el hogar.

[Sample_Superstore.csv](https://github.com/user-attachments/files/26946346/Sample_Superstore.csv)

## Se pide

1. Realizar un análisis del dataset facilitado, en cuanto a sus datos y a calidad del dato.
2. Detallar un caso de uso de business intelligence que se podría aplicar con este dataset.
3. Conceptualizar una arquitectura de BI.

<b>Tareas específicas</b>:

1. Descargar y abrir el dataset “Sample_Superstore.csv”.
2. Analizar los datos y el tipo de información que contiene:
    1. ¿Qué columnas de datos tiene respecto al producto vendido?
    2. ¿Qué columnas de datos tiene respecto al cliente?
    3. ¿Qué columnas de datos tiene respecto a la venta en sí?
3. Ver el ámbito de los datos:
    1. ¿Qué periodos de tiempo abarca?
    2. ¿Qué tipo de productos venden?
    3. Geográficamente, ¿de dónde son los clientes que compran en esta tienda?
4. ¿Qué tipo de análisis podría efectuarse con estos datos?
5. Conceptualizar una arquitectura de BI.
    1. Definir un diagrama de la arquitectura de BI que se usaría para almacenar, procesar y visualizar los datos del dataset.
    2. Definir las cuatro fases del entorno de BI que se ha definido:
        1. Origen de datos.
        2. Área de staging.
        3. Área analítica (data mart).
        4. Área de visualización.

## Solución

1. Descargar fichero del portal.
2. Datos de entrada que se van a analizar.

    Los datos de entrada se componen de las siguientes columnas:
    
    Para analizar por el eje de productos:
    - Category.
    - Sub-Category.
    - Manufacturer.
    - Product Name.
    - Segment.
    
    Para analizar por el eje de cliente:
    - City.
    - Country.
    - Region.
    - Customer Name.
    - Postal Code.
    - State.
  
    Datos propios de la venta:
    - Discount.
    - Number of Records.
    - Order Date.
    - Order ID.
    - Profit.
    - Quantity.
    - Sales.
    - Ship Date.
    - Ship Mode.
  
3. Análisis del dataset:

   El dataset tiene datos de 2015 a mayo de 2019. Abarca segmentos de productos como:
    - Consumer.
    - Corporate.
    - Home Office.
    
    Y geográficamente tiene datos de Estados Unidos.

5. Los datos permiten realizar análisis del siguiente tipo.

   Los datos de entrada permiten responder a preguntas como:
    - Beneficio que se obtiene por cada producto.
    - Qué ciudad / estado compra más.
    - Qué cliente es habitual / fiel a lo largo de los años.
    - Productos que tienen una alta tasa de descuento.

6. Arquitectura de BI.

    Una arquitectura de BI clásica tiene cuatro fases:

    - Origen de datos, dataset “Sample – Superstore.csv”. Fichero que podría generar un sistema operacional que gestiona las ventas.
    - Se carga este fichero en una primera área de staging, donde está el dato en bruto.
    - Se procesa y se carga a una tercera capa donde están los datos normalizados y formateados para el análisis.
    - Y la cuarta fase es la visualización en sí.
  
<img width="1680" height="391" alt="image" src="https://github.com/user-attachments/assets/2a5693ca-abce-4fea-93bf-a947e9ec1e15" />
