# Caso de estudio de IoT "Small IoT Platform with Analytics"

## Introducción

Se pretende desarrollar una plataforma End-to-End de Internet of Things (IoT) que incluirá dispositivos/sensores, canales de distribución, almacenamiento y procesamiento analítico y visualización en tiempo real.

Para ello, se utilizará sobre todo software open source y de desarrollo propio para interconectar toda la infraestructura. En esta práctica, se simularán los sensores/dispositivos para simplificar el caso.

Se cubrirán áreas de aprendizaje como ingesta de datos, procesado y transformación de los datos, distribución y seguridad de los datos, procesado analítico, almacenamiento en base de datos y en Hadoop y visualización de estos. Asimismo, se repasará la normativa que podría aplicarse y los costes de implementación.

Por tanto, los objetivos clave serán:
- Planificar una solución de IoT para el ámbito del hogar.
- Utilizar software libre y gratuito para la solución.
- Entender cómo los sensores/dispositivos se interconectan y distribuyen la información.
- Utilizar las herramientas/métodos aprendidos en el máster de una forma práctica enfocándose al caso de uso.

> **Nota**: es necesario remarcar que el área de seguridad estará fuera del estudio, por no complicar la solución y la integración de los componentes. También hay que tener en cuenta que se pretende desarrollarlo en un ámbito personal y controlado y los datos que se utilizarán no serán de información personal o clave, por tanto, el nivel de seguridad puede ser mucho menor que en otros entornos críticos.

## Desarrollo teórico
### Descripción de la arquitectura
La arquitectura que vamos a desarrollar será la siguiente:

<img width="534" height="389" alt="image" src="https://github.com/user-attachments/assets/2a157b8e-1494-4a9b-ac60-6a565c6995c3" />

En ella tendremos varios sensores conectados a un dispositivo; este será el encargado de alimentar, gestionar y controlar los sensores. En el dispositivo también se realizarán las tareas de recolectar, agrupar y procesar la información recogida por los sensores según los intervalos establecidos y enviarla de forma ordenada y controlada a los *gateways*.

- Gateway

    La función del *gateway* o pasarela es ofrecer un punto de acceso común a todos los dispositivos (con sensores) que pudiera haber y canalizar la información hacia el bus de distribución o *broker* de mensajes.

- Broker

    La función del *broker* de mensajes es recibir toda la información de todos los dispositivos/sensores y *gateways* y ofrecer canales de distribución o de consumo para todas las partes. Es pieza clave para la escalabilidad y la posibilidad de real time en la solución.

- Mensajero

    Desde el mensajero se podrán alimentar diferentes canales según la solución lo requiera. En este caso, planificamos básicamente dos distribuciones prioritarias: el almacenamiento de los datos y su visualización.
    
- Visualización

    Para la visualización, se conectarán las herramientas de exposición gráfica del usuario al bus de datos directamente o bien pasando por un proceso de ETL previamente (extracción, transformación y carga) según lo requieran los datos. La intención de esta herramienta gráfica es ser un *dashboard* o escritorio de datos con información en tiempo real de los valores de los sensores principalmente, por ejemplo.

    <img width="672" height="444" alt="image" src="https://github.com/user-attachments/assets/8f760d76-9098-4f4d-92c3-5d3740a74a89" />

- Leshan

    Simularemos sobre ‘n’ *devices* con sensor de temperatura, con el Leshan client. Estos ‘n’ dispositivos se registrarán al mismo bootstrap pero la mitad irán a un LwM2M server diferente.

    Los servidores Leshan están integrados y enviando directamente la información de registro (*new*, *up*, *delete*) y de observación de valores a tópicos de Kafka.

- Kafka

    Kafka será también nuestro bus de control y con un simple *pipeline* en SDC extraemos todos los datos de los tópicos que nos interesan y procesaremos los datos relativos a la temperatura, que serán distribuidos a una base de datos Cassandra, logs tradicionales y también a Elasticsearch. Estamos implementando una arquitectura lambda de procesamiento en idea, trabajando en tiempo real y en procesamiento *batch*.
