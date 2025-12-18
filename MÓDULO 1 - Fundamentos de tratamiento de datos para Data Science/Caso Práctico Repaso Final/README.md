# Se pide
## ENUNCIADO
Se va a plantear un ejercicio práctico de análisis de datos real a partir de los datos contenidos en un fichero CSV. Para ello, hay que descargar el siguiente archivo “electronic-card-transactions.csv”*

Este archivo contiene una muestra de datos acerca de transacciones de pago electrónico, agrupadas por comercio y por mes, durante un periodo de 15 años. Cada fila contiene el importe en dólares gastado (columna ‘Data_value’), el mes y año, y el sector (columna ‘Series_title_2’).

## DATOS
Se pide ejecutar las siguientes tareas sobre dicho documento, en un notebook de Jupyter:

1. Crear una función que lea el contenido del fichero y genere una lista de diccionarios, donde cada diccionario contenga los datos de una fila.

2. Desarrollar una función aggregate_year, que calcule la suma de los importes, agrupados por año y por sector. Esta función debe retornar un diccionario cuyas claves serán los sectores, y para cada una de ellas su valor será otro diccionario donde cada clave será el año, y su valor la suma de las transacciones durante ese año.
  
3. Construir un dataframe a partir de la estructura retornada por aggregate_year, donde los sectores estarán en el eje X y los años en el eje Y.

4. Calcular la suma y la media de las transacciones, agrupadas por sector y año.

5. Crear una función plot_sectors_by_date que reciba como parámetros el dataframe, una lista de sectores, y dos años, uno de inicio y otro de fin.

Esta función debe generar una gráfica lineal, donde se muestre la progresión de los datos de los sectores seleccionados, entre las dos fechas.

## SOLUCIONES
### <i>Solución 1:</i>
<img width="563" height="338" alt="image" src="https://github.com/user-attachments/assets/7e3f9ec6-cab2-49dc-b209-53ab0b45a0f9" />

### <i>Solución 2:</i>
<img width="563" height="395" alt="image" src="https://github.com/user-attachments/assets/0e5ad40c-961c-42d5-8e9d-eecff05bd816" />

