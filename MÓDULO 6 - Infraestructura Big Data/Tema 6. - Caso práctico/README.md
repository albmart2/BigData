# Caso práctico

Aplica los conocimientos adquiridos en esta unidad

## Enunciado

Supóngase una compañía que ofrece a sus clientes servicios de alojamiento; por lo tanto, para su negocio es clave conocer la opinión de los clientes, a través de diferentes canales información, por ejemplo:

- Rating de cada alojamiento
- Opiniones de los clientes sobre los alojamientos
- Opiniones de clientes y otros usuarios en redes sociales (Facebook, Twitter, Instagram, etc.)

De esta forma, desde un punto de vista analítico, todas estas opiniones y reviews, estarán disponibles en distintos puntos origen de datos.

El objetivo de la compañía es poder almacenar, procesar y extraer valor de todas estas opiniones, creando un modelo basado en sentiment analysis, mediante el cual poder hacer frente a malas críticas y elaborar planes de contingencia para mejorar tanto las críticas como la retención de clientes, así como poder premiar a los usuarios más fieles y con mejores opiniones.

Teniendo en cuenta estas necesidades, es imprescindible atender a ciertos aspectos clave para la elaboración de la arquitectura big data de este proyecto de sentiment analysis:

- Disponibilidad de instancias en cloud para la conexión a API de referencia sobre las redes sociales y otros medios.
- Ingesta y almacenamiento de datos.
- Unificación de fuentes de datos mediante procesos ETL.
- Desarrollo de un algoritmo de machine learning con enfoque NLP (procesamiento del lenguaje natural) basado en sentiment analysis.
- Persistencia de datos procesados y limpios.
- Visualización de resultados.

## Se pide

Elaborar un diagrama de arquitectura en el que se enmarquen todos los componentes necesarios para la obtención automática de predicciones y visualización de resultados a través de uno de los principales proveedores cloud: AWS (Amazon Web Services), Microsoft Azure o GCP (Google Cloud Platform).

Además, deben argumentarse las diferentes capas de la arquitectura, así como las herramientas escogidas.

## Solución

En esta ocasión, se selecciona el proveedor de servicios cloud AWS (Amazon Web Services); aunque, por supuesto, es posible escoger cualquiera de los tres, ya que ofrecen servicios similares para el mismo tipo de proyecto.

Pese a que se podrían reducir los costes de instanciación para la arquitectura empleando servicios de contenedores Docker, se tomará Amazon EC2 para la creación de instancias sobre las que elaborar los desarrollos pertinentes de conexión a las diferentes API (por ejemplo, scripts en Python). Incluso, podría tomarse en cuenta el desarrollo de alguna herramienta de web-scrapping para agregar más valor al sentiment analysis. Todo lo desarrollado en las instancias EC2 forma parte de la capa de Cloud.

> **Nota:** en este caso se tiene en cuenta un desarrollo propio; sería posible hacer uso de la herramienta Amazon API Gateway.

Posteriormente, una vez que se dispone de las conexiones a los orígenes de datos, se debe decidir qué tipo de arquitectura utilizar. En este caso, para hacer frente tanto a malas como a buenas críticas u opiniones en el menor tiempo posible, se hará en tiempo real, NRT (near real time). Por lo tanto, será necesario capturar streams. Este paso obliga a crear una capa de velocidad o stream (speed layer); para este propósito, se contará con la herramienta Amazon Kinesis Data Streams. Desde esta herramienta se tomarán dos salidas:

- Persistencia de datos en bucket de AWS S3.
- Envío de datos para su procesamiento a AWS Lambda.

Una vez que se dispone de los datos en tiempo real, es momento de unificarlos y procesarlos. Antes de pasar a su procesamiento mediante algoritmos, se continúa, evidentemente, en la capa de velocidad; no obstante, también se realizan procesos de transformación sobre los datos. Pese a que existen herramientas como Amazon Kinesis Analytics que se encargan de la realización de ETL¹ en tiempo real, se seleccionará la opción de realizar la ETL mediante funciones en tiempo real, como Amazon Lambda.

Tras la unificación de los diferentes streams en datos unificados, transformados y limpios, se pasa a la aplicación de modelos de machine learning.

> **Nota:** en esta capa de procesamiento, dado que se dispone de datos limpios, es conveniente ingestarlos y persistirlos en otra fuente de datos. Se tomará de nuevo un bucket S3.

Una vez sea posible garantizar la consistencia, validez y disponibilidad de los datos, es necesario aplicar modelos predictivos basados, en este caso, en técnicas de NLP para la obtención del sentiment analysis; por lo tanto, se trata de la capa de analítica. Como no puede ser de otra manera, se utilizará Amazon SageMaker para el entrenamiento y puesta en producción de modelos de aprendizaje automático. Además, en esta ocasión, es importante tomar en cuenta sus opciones en tiempo real o real-time inference.² Adicionalmente, para monitorizar los resultados de las predicciones, se utilizará SageMaker Model Monitor.

> **Nota:** es recomendable incluir capas de persistencia para el resultado de los modelos; de esta forma es posible disponer de históricos sobre los scores y métricas del modelo de sentiment analysis (o de cualquier otro).

Finalmente, se llega a la capa de visualización de resultados, en la que se podría mostrar de forma gráfica un cuadro de mando. En dicho cuadro de mando, sería posible ver la valoración otorgada por el modelo de sentiment analysis y comprobar otros factores, como la polaridad o la popularidad de la marca en función de un histórico. Para este propósito se emplearía Amazon QuickSight.

De forma adicional, si se desea informar, por ejemplo, mediante correo electrónico, de cualquier resultado crítico arrojado por el modelo, se puede incluir Amazon SNS.

El diagrama final de nuestra arquitectura sería el siguiente.

<img width="1526" height="692" alt="image" src="https://github.com/user-attachments/assets/d0ed3fd8-282b-463c-95e2-e2c1abe9189d" />
