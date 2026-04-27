# Caso práctico
## Enunciado
En esta unidad, la práctica consistirá en crear varias visualizaciones sobre el dataset “Sample_Superstore.csv” dado de alta en Google Big Query en unidades anteriores.

Se puede descargar el dataset en el siguiente enlace:

[Sample_Superstore.csv](https://github.com/user-attachments/files/27133039/Sample_Superstore.csv)

## Se pide
<b>Desarrollar las siguientes visualizaciones:</b>
1. Cantidad vendida por subcategoría de productos.
2. Evolución de ventas por fecha de pedido y categoría de producto.
3. Mostrar la cantidad vendida según la jerarquía de la dimensión producto.
4. Mostrar el volumen de ventas por ciudad.
5. Por subcategoría, comparar la cantidad vendida con el beneficio (profit).

<b>Para cada visualización, se debe contestar a las siguientes preguntas:</b>
- ¿Por qué se eligió esa visualización?
- ¿Cuál es el resultado final? Configuración y resultado.

### Por ejemplo
Cantidad vendida por categoría de productos.
- Se va a usar una gráfica de tarta, aunque se podría usar una gráfica de barras, que son las indicadas para comparar volúmenes cuando hay pocas ocurrencias en la dimensión.
- Ejemplo de visualización, se usa como dimensión la categoría y como métrica la cantidad.

<img width="760" height="453" alt="image" src="https://github.com/user-attachments/assets/cd60f9ce-8dff-482b-9bcd-5157a6b8d8e3" />

## Solución

Acceder a la consola de Google Cloud Platform. Una vez aquí, es fácil logarse con cualquier cuenta de Google. Esto activará el trial de GCP. Si los estudiantes no desean usar su cuenta personal de Gmail, se recomienda crear una cuenta alternativa para las prácticas. Aquí se usará test.imf.bd@gmail.com

Se exploran los datos con Data Studio y se hacen los siguientes análisis:

<img width="1165" height="417" alt="image" src="https://github.com/user-attachments/assets/ba1b8651-d1e4-4d31-bbda-ff9d708d5386" />

1. <b>Cantidad vendida por subcategoría de productos.</b>
    1. Se va a usar una gráfica de barras, que son las indicadas para comparar volúmenes cuando hay muchas ocurrencias en la dimensión.
    2. Ejemplo de visualización, se usa como dimensión la subcategoría y como métrica la cantidad.

        <img width="760" height="645" alt="image" src="https://github.com/user-attachments/assets/89281c5f-223a-4c64-92f0-94a7830f008a" />
        
2. <b>Evolución de ventas por fecha de pedido y categoría de producto.</b>
    1. Al indicar que se quiere ver la evolución por fecha de pedido, se usará una gráfica de líneas.
    2. En la configuración, se selecciona como dimensión “order_date”, dimensión de desglose “Category” y métrica “Quantity”.
  
       <img width="1057" height="425" alt="image" src="https://github.com/user-attachments/assets/c59276e7-c0db-4047-8f52-b883d5ac5ba0" />

3. <b>Mostrar la cantidad vendida según la jerarquía de la dimensión producto.</b>
    1. En este caso, se pueden elegir varios tipos de gráficos, como barras o columnas apiladas, pero el que mejor transmite volumen usando una jerarquía es el denominado treemap.
    2. En dimensiones se indicará “Category”, “Subcategory”, y como métrica la cantidad vendida.

       <img width="950" height="660" alt="image" src="https://github.com/user-attachments/assets/ef9f7592-aec0-489f-a951-917e1a6f9260" />

4. <b>Mostrar el volumen de ventas por ciudad.</b>
    1. Se elige un mapa de burbujas, donde las burbujas definen la cantidad de ventas.
    2. Se usa un mapa con la ciudad como dimensión geografía y tamaño de la burbuja para la cantidad.
  
       <img width="747" height="470" alt="image" src="https://github.com/user-attachments/assets/43aa1ee0-c451-4225-b190-f3a92c7dc670" />

5. <b>Por subcategoría, comparar la cantidad vendida con el beneficio (profit).</b>
    1. En este caso se pueden elegir varias visualizaciones, como la de barras, columnas e incluso de dispersión. La que mejor permite comparar ambas métricas sería la de barras.
    2. La dimensión es la subcategoría, con dos métricas: “Quantity” y “Profit”.
  
       <img width="1165" height="503" alt="image" src="https://github.com/user-attachments/assets/3bb08063-cfd2-4aba-8f41-012a18b3b23c" />
