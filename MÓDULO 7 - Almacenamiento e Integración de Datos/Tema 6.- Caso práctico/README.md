# Caso práctico con solución

## Enunciado

Crear un productor-consumidor simple, escrito en Python, para la herramienta Apache Kafka.

## Solución

En primer lugar, para crear el productor, se debe indicar el servidor donde está corriendo Kafka y el tema sobre el que se quiere escribir los mensajes:

```python
from kafka import KafkaProducer
import json

productor = KafkaProducer(bootstrap_servers='localhost:1234')

for _ in range(100):
  productor.send('item', b'Un mensaje')

#Bloquear hasta que se envíe un solo mensaje (o se supere el tiempo de espera
future = productor.send('item', b'Otro mensaje')
resultado = future.get(timeout=60)

#Bloquear hasta que todos los mensajes pendientes estén al menos en la red
productor.flush()

#Usar una clave para realizar un particionado hash
productor.send('item', key=b'clave', value=b'valor')

#Mensajes json serializados
productor = KafkaProducer(value_serializer=lambda v: json.dumps(v).encode('8'))
productor.send('ejemplo', {'clave': 'valor'})

#Claves serializadas
productor = KafkaProducer(key_serializer=str.encode)
productor.send('otro ejemplo', key='ping', value=b'1234')

#Comprimir mensajes
productor = KafkaProducer(compression_type='gzip')

for i in range(1000):
  productor.send('item', b'mensaje %d' % i)

#Obtener métricas de rendimiento del productor
metricas = productor.metrics()
```

Y para codificar el consumidor (se usa la API que proporciona Kafka), se crea un consumidor indicando el *host* y el puerto donde está arrancado el broker. El consumidor devuelve registros que son simples tuplas con nombre que exponen los atributos básicos del mensaje: tema, partición, desplazamiento, clave y valor:

```python
from kafka import KafkaConsumer
from kafka import TopicPartition

consumidor = KafkaConsumer('Tema favorito')
for msg in consumidor:
  print (msg)

#Unirse a un grupo de consumidores para asignaciones dinámicas de asignación y partición
consumidor = KafkaConsumer('Tema favorito', group_id='grupo_Tema favorito')

for msg in consumidor:
  print (msg)

#Asignar manualmente la lista de particiones para el consumidor
consumidor = KafkaConsumer(bootstrap_servers='localhost:1234')
consumidor.assign([TopicPartition('item', 2)])
msg = next(consumidor)

#Deserializar valores codificados en msgpaquete
consumidor = KafkaConsumer(value_deserializer=msgpack.loads)
consumidor.subscribe(['msgpaquete'])
for msg in consumidor:
  assert isinstance(msg.value, dict)

#Obtener métricas de consumo
metricas = consumer.metrics()
```

A continuación, se levanta un consumidor para ver que todo esté funcionando:

```bash
$ bin/kafka-console-consumer.sh --zookeeper localhost:1234 --topic Prueba
```
