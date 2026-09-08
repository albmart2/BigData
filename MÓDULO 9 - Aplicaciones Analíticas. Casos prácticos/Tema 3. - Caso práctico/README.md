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

## Desarrollo práctico

Para el seguimiento de este ejercicio guiado, debe descargarse el siguiente archivo comprimido que contiene todos los archivos necesarios:

[Archivos_02_UseCase_apdo_2_3_plat.zip](https://github.com/user-attachments/files/31975740/lAhb2dvcns6vI3m9-Archivos_02_UseCase_apdo_2_3_plat.zip)

### Fase de integración de componentes

1. Ejecutar los comandos del siguiente fichero “0_createscripts.txt” para crear dos servidores Leshan con nombres “KafkaGW” http://localhost:8080 y “KafkaGW2” http://localhost:8077 (este puerto no está mapeado en la máquina virtual, añadir la configuración en la parte de Devices => network => network settings => Advanced => Port Forwarding).

   No vamos a configurar seguridad en los servers para mantener la configuración sencilla.

2. El servidor bootstrap ya lo tenemos ejecutando http://localhost:8079. Añadir la configuración para clientes “device[1….n]” para que los ‘n/2’ devices apunten al “KafkaGW” (coap://localhost:5683) y la otra mitad al “KafkaGW2” (coap://localhost:5680).

    <img width="581" height="547" alt="image" src="https://github.com/user-attachments/assets/0524c358-ac04-4162-bfe0-200b348de3f4" />

3. La parte de conexión entre los lwM2M servers ya está hecha en el mismo cliente. Para más detalle, se puede consultar el código en [este enlace](https://github.com/cvasilak/leshan-server-kafka).

    El cliente exporta a tópicos los registros (new, up, del) y las observaciones efectuadas. Utiliza formato avro. Se pueden consultar, en los correspondientes tópicos de Kafka, los esquemas y estructura (Kafdrop => http://localhost:8085/ )

4. Importamos los pipelines:

    ```2_kakfaTemp.json```

    ```2_locations.json```

5. Para el ejercicio en StreamSet Data Collector: http://localhost:18630 (admin/admin)

    ```“2_kakfaTemp.json”```

    Este pipeline lee de varios tópicos de Kafka, escoge solo aquellos relativos a la temperatura (object “3303/0/”) y realiza una conversión para simplificar los valores a tipo json.

    ```JSON
    {"DeviceName":"device1","serverId":"KafkaGW","timestamp":1528045507855,"id":5700,"value": 10.1}
    ```

    <img width="1680" height="1074" alt="image" src="https://github.com/user-attachments/assets/a2a8430f-bd8e-4488-9a7f-71c2ab3de96d" />

    Se aplica un formato de conversión para pasar el timestamp de unix epoc a formato fecha estándar y se envía a tres destinos: ficheros locales, Cassandra y Elasticsearch.

    ```“2_locations.json”```
   
    Este *pipeline* lo utilizaremos para leer un fichero con las posiciones de los devices y popular datos tanto en Casandra y Kafka como en Elasticsearch.

6. Vamos a crear las bases de datos necesarias en Cassandra, http://localhost:8090. Los comandos se encuentran en el fichero: ```3_BaseDeDatos.txt```.

    <img width="1680" height="3493" alt="image" src="https://github.com/user-attachments/assets/41d69a62-5fc7-4959-b32f-f735eeb088b7" />

    Quedarían dos tablas, básicamente:

    <img width="550" height="328" alt="image" src="https://github.com/user-attachments/assets/4f052bc3-cbf2-448f-b258-67d21ddecf06" />

7. Ahora, continuamos con la definición de los datos en Elasticsearch, ejecutando los comandos disponibles en el siguiente fichero ```4_IndicesElastic.txt``` desde la consola:

   <img width="735" height="680" alt="image" src="https://github.com/user-attachments/assets/4c637a55-a8a8-4338-9856-c57b42d44bfe" />

    A continuación, se puede descargar este código en formato editable: archivo "7_2_Apdo_3_1_punto7.docx".

8. Configuramos los índices en Kibana, http://localhost:5601:

    <img width="1680" height="2113" alt="image" src="https://github.com/user-attachments/assets/6b0e3ac1-814e-436a-8404-fe22c598a1c2" />

    <img width="1680" height="1297" alt="image" src="https://github.com/user-attachments/assets/4797241f-8435-474b-af97-436cd3898092" />

9. Creamos la estructura de datos en la máquina virtual para los datos y copiamos el fichero: ```leshanBULK.sh``` (nano => copy&paste por ejemplo).

    ```bash
    imf@imf-vm:~$ mkdir -p /home/imf/e2e/out
    imf@imf-vm:~$ chmod -R 777 /home/imf/e2e/out
    imf@imf-vm:~$ touch /home/imf/e2e/bulklocations.log
    imf@imf-vm:~$ nano /home/imf/e2e/leshanBULK.sh
    imf@imf-vm:~$ chmod +x /home/imf/e2e/leshanBULK.sh
    ```

10. Ya tenemos definidas todas las estructuras de datos y flujos.

11. Configurar el schemaRegistry para poder parsear y reconocer los flujos de datos en formato Avro
    - Editamos el siguiente archivo:

        ```bash
        sudo nano /etc/schema-registry/schema-registry.properties
        ```
    - Añadimos al final del archivo la siguiente línea:

        ```bash
        kafkastore.bootstrap.servers=PLAINTEXT://localhost:9092
        ```

        <img width="600" height="166" alt="image" src="https://github.com/user-attachments/assets/8903b478-758f-4381-aeab-3a03ae738496" />

    - Ahora, ya hemos conectado el schemaRegistry con el servidor Kafka.
    - Editamos el siguiente archivo:

        ```bash
        sudo nano /etc/kafka/server.properties
        ```
    - Añadimos la siguiente línea:

        ```bash
        listeners=PLAINTEXT://localhost:9092
        ```

        <img width="600" height="190" alt="image" src="https://github.com/user-attachments/assets/9c28fa51-c529-4737-b2f2-093a84ac9bfd" />

12. Arrancamos el schemaRegistry:

    ```bash
    sudo systemctl start confluent-schema-registry
    ```

13. Verificamos que el schemaRegistry funciona correctamente:

    ```bash
    sudo systemctl status confluent-schema-registry
    ```

[wLTisPEkTCOlQzVK-7_2_Apdo_3_1_punto7.docx](https://github.com/user-attachments/files/31976476/wLTisPEkTCOlQzVK-7_2_Apdo_3_1_punto7.docx)

### Fase de ejecución

1. Se puede observar que no hay datos todavía.

    - Kafka.
        > **Nota**: están los tópicos de prueba del ejercicio “KafkaGW”, pero podéis observar que no hay nuevos datos ni están los tópicos del “KafkaGW2”.
        
        <img width="1680" height="1439" alt="image" src="https://github.com/user-attachments/assets/11c88b52-5c24-4ac8-8f6d-ade7b66c4cc7" />

    - Cassandra.
    - Elasticsearch, http://localhost:9200/sensors/_count

        <img width="1680" height="1450" alt="image" src="https://github.com/user-attachments/assets/b482b54b-27f4-4de3-b752-e56829e0ecf3" />

2. Ejecutamos el *pipeline* de “```2_locations```”:

    De momento, no hay datos de localización porque no hemos lanzado el script de los devices (el único registro es de la salida “2” metadatos que lo hemos descartado y enviado a la basura).

   <img width="672" height="491" alt="image" src="https://github.com/user-attachments/assets/2fdf1674-8f79-4958-8627-4f51312263e0" />

3. Comprobar que no hay ningún device registrado en los lwM2M server:
    - KafkaGW => http://localhost:8080/#/clients
    - KafkaGW2 => http://localhost:8077/#/clients
  
4. Vamos a ejecutar el script de leshanBULK.sh:

    - Sin argumentos, elimina los procesos de leshan-client que hubiera ejecutándose, por lo que lo utilizaremos para parar los procesos.

    ```bash
    imf@imf-vm:~/e2e$ ./leshanBULK.sh
    ```

    No arguments supplied. Deleting all leshan-clients running

    ```bash
    imf@imf-vm:~/e2e$
    ```
    - Con argumentos, define el número de devices especificados. El output de los clientes-leshan se mostrará en la misma sesión, por lo que tiene que permanecer abierta.

    ```bash
    imf@imf-vm:~/e2e$ ./leshanBULK.sh 20
    imf@imf-vm:~/e2e$
    ```

5. Una vez ejecutado el *script*, se habrán registrado los ‘n’ *devices* configurados. En la ventana de ejecución se pueden observar los mensajes de los clientes.

6. Comprobar que ahora están los devices registrados en los lwM2M server:

    - KafkaGW => http://localhost:8080/#/clients
    - KafkaGW2 => http://localhost:8077/#/clients
  
    <img width="1680" height="1507" alt="image" src="https://github.com/user-attachments/assets/df509ef8-53c0-46a3-ae82-5843377afbb0" />

7. Ejecutamos el siguiente pipeline ahora que tenemos ya todos los tópicos creados:

    <img width="1680" height="1856" alt="image" src="https://github.com/user-attachments/assets/131ba5e5-dbc0-4a3a-8d0d-2e8b4eabfab4" />

8. Ahora están ya todos los flujos de datos y comunicación abiertos. El cliente demo de Leshan tiene un carácter académico, por lo que no realiza automáticamente el refresco de los datos a menos que se lo indiquemos.

    Una vez que le demos a “observe” a la Instancia 0 de Temperature, se podrá observar cómo ya se están recibiendo datos en toda la cadena.
   
   <img width="672" height="364" alt="image" src="https://github.com/user-attachments/assets/2c1f073f-e080-4054-a6c0-c284932b9619" />

9. Iniciar la observación en todos los *devices*:

    <img width="672" height="297" alt="image" src="https://github.com/user-attachments/assets/3097f9fa-e892-4b86-918b-88237666c389" />

10. Observar que no hay datos todavía:
    - Kafka, http://localhost:8085/topic/KafkaGW2_observation
    - Cassandra

        http://localhost:8090/datos/sensors

        http://localhost:8090/datos/location

        <img width="1680" height="1069" alt="image" src="https://github.com/user-attachments/assets/9379d1f1-7a38-49ae-937a-f02a1ef24c30" />

    - Elasticsearch, http://localhost:9200/sensors/_count

        <img width="498" height="100" alt="image" src="https://github.com/user-attachments/assets/4f22249b-15d0-4544-a685-e04f9ac8b661" />

### Visualización en *real time*

Utilizamos Kibana: http://localhost:5601

- Discover:

    Para visualizar los datos que podemos obtener de los índices de Elasticsearch.

    <img width="572" height="269" alt="image" src="https://github.com/user-attachments/assets/93bc3793-73bf-4106-a251-88dd366c9776" />

    Para *locations*, ajustar el periodo (parte superior derecha) para ver los datos, pues puede darse el caso de que existan datos en ese periodo.

    <img width="572" height="269" alt="image" src="https://github.com/user-attachments/assets/c0fa7c02-fea4-44da-8ccd-5dc737d75975" />

    <img width="672" height="280" alt="image" src="https://github.com/user-attachments/assets/631d2834-e9b3-4c6e-8795-64744c940771" />

- Visualize:

    Vamos a crear dos visualizaciones básicas a modo de ejemplo.

    <img width="672" height="349" alt="image" src="https://github.com/user-attachments/assets/e4e87217-77d7-4a39-9922-fd8a7658f13a" />

    “CoordinateMaps”, para utilizar los datos de geopoint del índice de “locations”:

    <img width="672" height="341" alt="image" src="https://github.com/user-attachments/assets/90ab75b2-160b-47ce-a48c-cac3e8f2a142" />

    “Basic Charts => Line”, para visualizar la tendencia de los valores:

    <img width="672" height="281" alt="image" src="https://github.com/user-attachments/assets/d6526fea-0e6c-487d-98cf-3f257a51b75b" />

    > **Nota**: Los más observadores se darán cuenta de que los datos están continuamente bajando, es decir, disminuyendo la temperatura, incluso a valores imposibles. Esto se debe a que el cliente Leshan tiene un ciclo de histeria mal diseñado y tiende a bajar constantemente cuando genera los valores de temperatura.

### Procesamiento analítico desde Jupyter y Python

Ahora, vamos a leer esa información desde un notebook en Python. Abrir Jupyter notebooks, http://localhost:8888. Importar el notebook: ```6_PythonReadCassandra2.ipynb``` y seguir los pasos.

<img width="497" height="476" alt="image" src="https://github.com/user-attachments/assets/a3d0f2d0-db40-48df-be03-9eae984239c3" />

<img width="525" height="260" alt="image" src="https://github.com/user-attachments/assets/9b3cd413-6e15-445b-b71f-94bc240662a7" />

### Ejemplo con *devices* reales

A modo de ejemplo, sustituyendo los emuladores de Leshan por HW de verdad. Para la parte de adquisición de datos se ha utilizado la Raspberry Pi 3 y un único sensor (AOSONG DHT11) que recoge de forma simultánea las medidas de temperatura y humedad. Para ello, se ha utilizado el bus GPIO de la Raspberry Pi y la plataforma AdaFruit para acceder al bus y leer la información del sensor.

<img width="533" height="331" alt="image" src="https://github.com/user-attachments/assets/7f693a31-944f-4b41-b02e-16b6e2a2ce07" />

Esta información se vuelca a ficheros de log que van rotando diariamente y con una retención de 7 días (configurado con logwatch).

Con esos datos se va a alimentar el bus de comunicaciones a través de un Kafka Producer client. Para ello se ha instalado dicho SW en la Raspi. En cada una de las instancias se crearán diferentes flujos de trabajo para inyectar los datos en Kafka y realizar los procesos de ETL para Cassandra y visualización.

Para la distribución y transformación de los datos para almacenamiento y visualización, se han definido los siguientes pipelines: “Kafka2Cassandra” y “Kafka2ElasticSearch”. Ambos flujos leen los datos de Kafka para el tópico “SensorTH”, aplican una pequeña conversión en el campo fecha para pasarlo de Unix a un formato humano y lo almacenan en ficheros locales (tanto en la RaspberryPi como en el ordenador) e inyectan a la base de datos Cassandra y al indexador/almacenamiento Elasticsearch respectivamente.

La base de datos ha creado simplemente una tabla para almacenar los datos tal cual son recibidos a través de Kafka. Los valores clave son SensorId y Fecha (para poder permitir múltiples sensores).

Para la visualización se ha optado por Kibana, ya que ofrece una integración más sencilla y la posibilidad de incluir Elasticsearch (para una indexación y almacenamiento buffer), que nos permitirá observar en tiempo real y con poco coste de cómputo consultas de los datos obtenidos. Además, ofrece interesantes funcionalidades para las agregaciones de las fechas de forma muy sencilla y transparente para el usuario.

Se ha elaborado un dashboard básico con la información agregadas de humedad, temperatura, gráficos con los históricos de las temperaturas y humedad, valores medios de los sensores, etc.

Este dashboard está mostrando los valores cada 5 segundos con un delay de 10-15 segundos respecto al valor leído. Este retraso se introduce por volcado Linux al fichero en la RaspberryPi.

<img width="792" height="478" alt="image" src="https://github.com/user-attachments/assets/72a25d00-2533-4fdb-9abe-4d038910f317" />

## Conclusión

En este trabajo se ha observado de cerca y se ha implementado una solución end-to-end de IoT: desde el sensor hasta la visualización de datos y analítica, utilizando componentes asequibles para el consumidor, SW gratuito y reutilización de HW.

Las mayores complicaciones han sido principalmente interconectar todos los componentes de una forma rápida, eficaz, de bajo coste y que sea escalable tanto vertical como horizontalmente.

La elección de los componentes de la arquitectura siempre será una tarea ardua, pues requerirá valorar las capacidades y beneficios de cada una de las herramientas en sus funciones, con la peculiaridad añadida de que existe una gran variedad de SW para las mismas funciones y que muchas de ellas realizan funciones complejas. Por ejemplo, para la distribución de mensajes, podría haberse optado por Flume o RabbitQM en vez de Kafka, que hubieran sido también viables para esta solución.

Esta solución es escalable gracias en gran parte a la distribución de mensajes mediante Kafka y bases de datos de Cassandra, que pueden ser fácilmente ampliables añadiendo nuevos elementos en los respectivos clústeres de trabajo. Asimismo, la herramienta de visualización e indexación (que también es escalable) ofrece grandes posibilidades de desarrollo para el dashboard independientemente de las medidas, número de variables o cantidad de elementos que interconectar.

La posibilidad de analizar los datos con R o Python utilizando la base de datos o incluso el mismo Kafka ofrece grandes posibilidades de procesamiento batch para un análisis de los datos y añadir nuevas fuentes de datos para poder contrastar o potenciar estos análisis. Es verdad, no obstante, que debido a los pocos datos obtenidos en esta simulación y a la validez de los mismos se ha limitado el caso prácticamente a monitorización y procesado de los datos.

## Ejercicio

El objetivo de este ejercicio es realizar una reflexión teórica basada en la arquitectura anterior.

> *Nota*: este ejercicio es evaluable y deberá entregarse al final del módulo junto con los ejercicios del resto de unidades.

1. Valora qué usos podría tener registrar los datos de temperatura y humedad. Es decir, qué casos de uso, modelo de negocio y aplicaciones podrían darse con estos datos. Por ejemplo, cómo podrían usarse para mejorar la calidad de vida o los servicios de una ciudad.

    Estos datos pueden utilizarse para mejorar la calidad de vida en ciudades inteligentes, controlar la climatización de edificios, optimizar el consumo energético y detectar condiciones ambientales desfavorables. También tienen aplicaciones en agricultura, logística, almacenamiento de alimentos y hogares inteligentes. Como modelo de negocio, se podrían ofrecer servicios de monitorización, alertas y análisis de datos mediante suscripción.

2. ¿La arquitectura funcional cumple con los requerimientos de escalabilidad, redundancia, gestión y seguridad para poder conectar miles de dispositivos? ¿La arquitectura tiene en cuenta la no homogeneidad que se representa en la realidad y puede integrar y gestionar dispositivos de diferentes proveedores y con diferentes tecnologías?

    La arquitectura puede ser escalable si permite añadir nuevos servidores y dispositivos sin afectar al funcionamiento del sistema. La redundancia y replicación permiten evitar pérdidas de datos ante fallos. Además, debe incorporar autenticación, cifrado y control de acceso. Para gestionar dispositivos de diferentes fabricantes, es necesario utilizar protocolos y sistemas de integración que permitan normalizar los datos.

3. En vez de un broker basado en Kafka, ¿podría haberse utilizado un MQTT? En vez de almacenar en Cassandra, si lo almacenamos en HDFS, ¿qué beneficios inherentes podríamos tener?

    Sí, MQTT podría utilizarse en lugar de Kafka, ya que es un protocolo ligero y especialmente diseñado para dispositivos IoT. Kafka está más orientado a gestionar grandes volúmenes de eventos.

    Si se utilizara HDFS en lugar de Cassandra, se obtendría un almacenamiento distribuido y escalable, adecuado para grandes cantidades de datos históricos y procesamiento Big Data. Cassandra sería más adecuada para consultas rápidas y frecuentes.

4. ¿Qué costes de implementación, mantenimiento y gestión de la plataforma observas claramente?

    Los principales costes serían la compra e instalación de sensores, infraestructura de servidores y almacenamiento, comunicaciones, mantenimiento de dispositivos, actualizaciones de software, seguridad y gestión de la plataforma. Además, cuantos más dispositivos haya, mayores serán los costes de almacenamiento, procesamiento y mantenimiento.

## Herramientas utilizadas

A continuación, se facilita un listado con una breve descripción sobre las herramientas (software) utilizadas para el desarrollo del ejercicio. Se pueden consultar los enlaces para profundizar sobre esas herramientas:

- Leshan, https://github.com/eclipse/leshan. Leshan es un proyecto de Eclipse que ofrece un cliente y servidor para LwM2M en java.
- StreamSets, http://streamsets.com/. Herramienta utilizada para los procesos de ETL (Extract-Tranform-Load) e interconexión de los diferentes componentes del ejercicio.
- Apache Kafka, Confluent, https://www.confluent.io/. Versión de Apache Kafka, herramienta de distribución de alta capacidad para la publicación/distribución de mensajes.
- Apache Cassandra, http://cassandra.apache.org/. Base de datos NoSQL de alta capacidad y servicios en clúster.
- Elastic, https://www.elastic.co/. Herramienta de indexación y visualización de datos en tiempo real. En este caso hemos utilizado los componentes Elasticsearch y Kibana.
- Anaconda, https://anaconda.org/. Plataforma de SW que combina multitud de herramientas útiles para Data Science. Ofrece una plataforma unificada, gestión de paquetes y entornos de forma sencilla. En este caso hemos utilizado principalmente los componentes de Jupyter, Python y R.
- Draw, http://draw.io. Para la elaboración de los diagramas y dibujos de interconexión, hemos utilizado esta herramienta de diagramas gratuita.
- Stack Overflow, https://es.stackoverflow.com/. Página web de gran ayuda para todos los programadores. Un gran foro donde resolver, plantear y ayudar con los problemas de programación en cualquier lenguaje y entorno.
