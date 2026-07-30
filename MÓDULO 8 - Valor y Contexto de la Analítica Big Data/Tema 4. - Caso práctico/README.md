# Caso práctico con solución

## Enunciado

Uno de tus clientes del sector del marketing y los *media* se ha embarcado en un plan de transformación con el objetivo de incrementar los ingresos que recibe por usuario. Como consultor experto, el cliente te llama para exponerte su plan de mejora. En la reunión inicial, la única guía que recibes es que desea mejorar los ingresos a la par que fidelizar a sus clientes y que, para ello, se está planteando usar algoritmos matemáticos y *machine learning*.

Tras esta primera reunión, observas que no hay información suficiente para empezar a trabajar en un plan, por lo que requieres un segundo encuentro.

En esta segunda reunión conseguís detallar el requisito macro en requisitos menores:

- Mejorar el conocimiento que se tiene de los clientes, sus intereses y comportamientos.
- Generar un perfil de cliente, con hábitos y gustos de cara a optimizar los contenidos que se le ofrecen.
- Aumentar el valor percibido por los clientes de los productos y contenidos contratados.
- Mejorar el tráfico en los canales digitales para aumentar los ingresos percibidos por publicidad.
- Mejorar los contenidos y hacerlos más personalizados, de forma que las suscripciones aumenten y disminuyan las cancelaciones.
- Elaborar modelos de recomendación de contenidos y productos de cara a mejorar la efectividad de las recomendaciones comerciales.

Una vez definidos los objetivos concretos, el siguiente paso es evaluar el tipo de tecnología y proyectos que necesita el cliente. Para ello, lo primero que se plantea es si hace falta o no incorporar tecnología big data y analytics dentro del proyecto. Para decidirlo, realizas un análisis como el que se muestra a continuación.

**Necesidad de tecnología big data**
- Volumen:
    - Los sistemas de los que el proyecto va a alimentarse son sistemas tradicionales, operacionales, con información estructurada y un volumen medio.
    - Hay interés por procesar la información de logs de los sistemas digitales para definir el flujo de comportamiento de los clientes y poder optimizarlo. Se trata de datos NoSQL con un volumen alto de información.
- Velocidad:
    - Los sistemas se plantean, principalmente, en batch, aunque existe interés en realizar acciones en near-real-time (NRT) en el futuro.
- Variedad:
    - Los datos son mayoritariamente SQL, aunque, si se desea procesar la información de logs, se incluirán datos NoSQL en el sistema.

En función de todo ello, se plantea utilizar una plataforma big data, principalmente, por el uso de información de logs.

**Necesidad de modelos analíticos**

La decisión de si se necesita analytics o qué tipo de analytics debe tomarse basándose en las preguntas de negocio. Es decir, si se entiende qué objetivos de negocio se persiguen, el primer punto es analizar qué tipo de algoritmos necesitan.

- Generar conocimiento del cliente:
    - Segmentación.
    - Clasificación.
    - Data processing.
- Generar un perfil de cliente, hábitos y gustos:
    - Microsegmentación.
    - NLP.
- Aumentar el valor percibido de los productos y servicios ofertados o contratados:
    - Recomendación de productos.
    - Modelos de previsión.
    - Basket-item models.

Según esto, se considera vital aplicar modelos para la mejora de los objetivos de negocio definidos.

El siguiente paso, una vez decidida la tecnología y el uso de técnicas de business analytics, es generar el catálogo de posibles proyectos. Para ello dibujas el ciclo de vida de un cliente y marcas dentro los puntos donde los diferentes proyectos pueden aplicarse.

<img width="1283" height="613" alt="image" src="https://github.com/user-attachments/assets/1ef9bcd3-4e7d-45b1-9203-774785fda1d2" />

**A continuación, se describe cada uno de los posibles proyectos:**
- *Heavy user*. Se trata de generar un modelo para las áreas de captación de nuevos clientes que, en función de las variables disponibles de los potenciales clientes, estime los ingresos esperados de cada uno de ellos para, así, priorizar las acciones de captación de los clientes de los que mejor retorno se espera.
- Abandono del proceso de compra. Se trata de un modelo que genera, para cada segmento de cliente, los flujos de comportamiento en el proceso de compra y detecta zonas donde los clientes abandonan el proceso. El modelo proporciona, por tanto, para cada segmento de clientes los puntos críticos donde un cliente abandona para modificar el flujo y evitar esas pérdidas.
- Recomendación por similitud. Se realiza una recomendación de contenidos similares. Es decir, según las preferencias de los clientes, se proporcionan recomendaciones de contenidos y productos similares a los ya consumidos. Se trata de un modelo de up-selling, es decir, proporcionar más de lo que se ha comprobado que gusta.
- *Cross-selling*. Según las compras o consumos de contenidos de los clientes, generar un modelo de estimación de afinidad a productos o contenidos de áreas diferentes para incentivar la diversificación de ingresos de un cliente entre todos los departamentos. A diferencia del up-selling, en este caso el objetivo es diversificar los ingresos entre diferentes áreas de productos.
- Reactivación por tiempo. Consiste en proponer acciones a clientes que llevan un tiempo sin actividad. Se trata de reactivar clientes que en el último periodo de tiempo han tenido poca actividad, lo cual puede llevar a una fuga.
- Recomendación personalizada. Según los gustos, preferencias e intereses mostrados, generar un grafo de intereses para proporcionar productos de atractivo, similar al modelo de Amazon, no solamente de áreas testeadas de interés, sino descubriendo nuevas temáticas de contenidos y productos para los clientes.
- Usuarios dormidos. Detectar clientes que llevan un largo tiempo sin actividad, aunque sin darse de baja de los sistemas, y realizar acciones comerciales para atraerlos de nuevo a una actividad óptima. Se diferencia de la reactivación por tiempo en que en este caso los usuarios dormidos llevan un periodo de tiempo muy largo inactivos y, más que evitar el riesgo de fuga, el objetivo es incrementar los ingresos.
- Detección de fuga. Elaborar un modelo de estimación del valor del cliente y un modelo que estime su satisfacción. En función de estas dos variables, desarrollar un modelo predictivo que prediga a N meses vista qué clientes tienen más posibilidades de darse de baja de los sistemas.

## Se pide

Según este mapa de proyectos, se deberá generar un gráfico o una tabla donde se estudie:
1. Coste/dificultad del proyecto: de forma cualitativa, dar una medida de complejidad a cada uno de los proyectos.
2. Beneficio del proyecto: dar, en una escala del 1 a 10, el potencial beneficio de cada proyecto.
3. Tiempo de retorno: dar, en una escala del 1 a 10, el tiempo de retorno del beneficio, es decir, desde que el proyecto se concluye y se pone en producción, el tiempo que pasa hasta que la empresa ve el beneficio real.

Los estudiantes deberán entonces elaborar dos gráficos:

<ol type="a">
  <li>Coste vs. beneficio del proyecto.</li>
  <li>Coste vs. tiempo de retorno.</li>
</ol>

Según estos gráficos, establecer una priorización en un intervalo de tres años y explicar qué proyectos se abordarían y en qué orden.

## Solución

Una posible solución al problema sería la siguiente:

En la siguiente tabla, se anotan todos los casos de uso y se ponderan del 1 al 10 las columnas “Complejidad”, “Beneficio neto” y “Tiempo de retorno”, de acuerdo con las instrucciones planteadas en el enunciado.

En esta tabla, ponemos todos los casos de uso y ponderamos del 1 al 10 las columnas Complejidad, Beneficio neto y Tiempo de retorno de acuerdo con las instrucciones planteadas anteriormente.

<img width="1257" height="816" alt="image" src="https://github.com/user-attachments/assets/bb5aa019-998f-4c06-9282-d11dfa265113" />

Una vez tabulados los datos, se procede a construir las dos gráficas.

En la primera, “Beneficio neto vs. complejidad”, se coloca en el eje X el beneficio neto con una escala de 1 a 10, y en el eje Y la complejidad con la misma escala:

<b><p align="center">
  Beneficio vs. complejidad.
</p></b>

<img width="1079" height="632" alt="image" src="https://github.com/user-attachments/assets/0576dc8b-e6a7-449c-b98a-e9e6a527d296" />

En la segunda gráfica, “Tiempo de retorno vs. complejidad”, se utiliza el eje X para el tiempo de retorno y la complejidad se representa en el eje Y, ambas con escala de 1 al 10:

<b><p align="center">
  Tiempo de retorno vs. complejidad.
</p></b>

<img width="1185" height="630" alt="image" src="https://github.com/user-attachments/assets/de571202-d62b-447a-a914-f5ed9da19dfa" />

Una vez analizadas estas dos gráficas, corresponde tomar la decisión de qué casos de uso se abordarán en el primer, segundo y tercer año respectivamente. Para esta decisión, se toman como base las tres variables analizadas: complejidad, beneficio neto y tiempo de retorno, así como lo que se considere más beneficioso para el negocio.

<img width="1206" height="880" alt="image" src="https://github.com/user-attachments/assets/ee700315-f9b3-4da6-a717-994adc8e544f" />
