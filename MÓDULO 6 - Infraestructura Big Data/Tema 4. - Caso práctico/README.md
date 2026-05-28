# Caso práctico

## Objetivo

Aplicar los conocimientos adquiridos en la unidad para proponer el tipo de arquitectura más adecuada en cada caso.

## Se Pide

Proponer el tipo de arquitectura, **Lambda o Kappa**, más adecuada para cada caso y argumentar por qué.

---

## Caso A — Empresa del Sector Bancario

### Enunciado

Supóngase una empresa relacionada con el sector bancario. Como es evidente, esta empresa gestiona una ingente cantidad de información acerca de sus clientes (información personal, financiera, laboral, etc.).

Además, cuando cada cliente accede al "área cliente" de la página web, la empresa se encarga de recopilar información de navegación como: clics que realiza, áreas de la web que reciben más atención, etc.

En función del área de la web por la que esté navegando el cliente, la empresa quiere emplear un sistema de recomendación en tiempo real, de forma que si, por ejemplo, el cliente está visitando la sección sobre productos bancarios, el sistema le ofrezca un producto como un préstamo personal o fondos de inversión.

> ¿Qué arquitectura es más adecuada en este caso, Lambda o Kappa? ¿Por qué?

### Solución

**Arquitectura recomendada: Lambda**

Pese a que se podría tratar la persistencia de los datos de navegación de cada cliente como un log y ofrecer una arquitectura Kappa, lo más conveniente es una **arquitectura Lambda**, con las siguientes capas:

**Batch layer (Capa batch):** capa en la que se almacenan en raw todos los datos de navegación del cliente, junto con su información personal y financiera.

**Speed layer (Capa stream):** capa que se encarga de procesar en tiempo real los últimos datos de navegación del cliente para detectar en qué sección de la web se encuentra en cada momento.

**Serving layer (Capa de servicio):** capa en la que, a través de queries, se realiza el merge de los datos de navegación junto con la información personal o financiera del cliente. A partir de las *batch views* y las *real-time views*, es posible ofrecer una respuesta del canal de recomendación sobre productos bancarios adaptada a cada cliente.

**Justificación:** se elige Lambda porque el sistema de recomendación necesita combinar datos históricos del cliente (información personal, financiera, historial de navegación consolidado) almacenados en la capa batch, con los datos de navegación en tiempo real de la speed layer. Esta combinación de ambas capas en la serving layer es lo que permite ofrecer recomendaciones verdaderamente personalizadas.

---

## Caso B — Empresa de Transportes (Flota de Camiones)

### Enunciado

Supóngase una empresa de transportes que administra una flota de camiones que circulan a nivel nacional.

Cada uno de estos camiones tiene incorporado un sistema **OBD (On Board Diagnostics)** mediante el cual es posible acceder a los siguientes parámetros del vehículo:

- Velocidad.
- Temperatura y estado del motor.
- Temperatura, estado y nivel de aceite.
- Estado de los frenos.
- Coordenadas de posición actual del camión.
- Consumo instantáneo de combustible.
- Nivel de combustible.

La empresa asume un gran coste en la recarga de combustible y cuenta con varias gasolineras con las que tiene acuerdos y promociones.

**El propósito de la arquitectura es el siguiente:** sabiendo que se dispone de la posición en tiempo real de cada camión y del nivel de combustible, si el nivel de combustible está por debajo del **20 %** de la capacidad del depósito y, además, el camión se encuentra cerca de una de las gasolineras asociadas, entonces el conductor deberá recibir una **notificación con el porcentaje de descuento** si reposta en dicha gasolinera.

La respuesta del sistema debe ser completamente inmediata, al encontrarse los conductores en movimiento.

> ¿Qué arquitectura es más adecuada en este caso, Lambda o Kappa? ¿Por qué?

### Solución

**Arquitectura recomendada: Kappa**

Dada la constante generación de datos —como mínimo, cada segundo— toma una importancia clave el uso de la herramienta **Kafka**; por lo tanto, se trata de un caso de **arquitectura Kappa**.

Toda la información del OBD del conductor puede ser tratada como un *log*, en el cual cada una de sus líneas genera información sobre una parametrización del dispositivo conectado al camión. Cada uno de estos parámetros que generan información serán los distintos **topics de Kafka** para esta arquitectura.

Los principales topics sobre los que consumir la información en tiempo real (*consumers*) serán:

- Coordenadas de posición actual del camión.
- Nivel de combustible.

La información relativa a la ubicación de cada gasolinera asociada con la empresa estará almacenada en otro soporte, accesible a través de queries. Estas gasolineras podrían tratarse como **centroides estáticos**, y las coordenadas del camión como los diferentes puntos sobre los que calcular distancias sujetas a la restricción del nivel de combustible. Es decir, se podría incorporar **machine learning** (en este caso, *k-means*).

**Justificación:** se elige Kappa porque toda la lógica de negocio puede resolverse procesando únicamente los datos en tránsito (posición + nivel de combustible) sin necesidad de cruzar con datos históricos complejos. La arquitectura Kappa simplifica el sistema al eliminar la capa batch, usando un único framework de procesamiento en tiempo real que es suficiente para cumplir el requisito de respuesta inmediata.

**Ejemplo de arquitectura Kappa para este caso:**

```
Fuentes OBD (camiones)
        ↓
   [Kafka Cluster]          ← topics: posición, nivel combustible
        ↓
 [Streaming Layer]          ← Real-time Engine (Spark Streaming / Flink)
        ↓
  [Serving Layer]           ← Serving Backend + Results DB
        ↓
Notificación al conductor
```
