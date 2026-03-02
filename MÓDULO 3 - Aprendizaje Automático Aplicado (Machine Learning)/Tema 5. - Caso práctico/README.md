# Caso práctico

## Se pide

Implementar una red neuronal que permita reproducir la función XOR de tres entradas, es decir:

|X<sub>1</sub>|X<sub>2</sub>|X<sub>2</sub>|XOR|
|----|----|----|---|
|0|0|0|0|
|0|0|1|1|
|0|1|0|1|
|0|1|1|0|
|1|0|0|1|
|1|0|1|0|
|1|1|0|0|
|1|1|1|1|

## Solución

### Requisitos previos

- Crearse un entorno en <i>Anaconda promt</i>.

    ```bash
    conda create -n tf python=3.10
    ```

- Activar el entorno.

    ```bash
    conda activate tf
    ```

- Instalar <i>Tensorflow</i>.

    ```bash
    conda install -c conda-forge tensorflow
    ```

- Instalar <i>Pandas</i>.

    ```bash
    conda install pandas -c conda-forge
    ```

### Proceso

Como hay tres entradas, para intentar predecir el resultado se va a utilizar una capa con tres neuronas.

En el diseño de la red neuronal se ha de tener en cuenta que los vectores de peso tienen que tener tres elementos, como en el esquema que se muestra en la figura:

<img width="353" height="259" alt="image" src="https://github.com/user-attachments/assets/8e3afc37-d6ea-4769-959d-5e37bf04b9c6" />

La implementación del modelo es similar a la realidad. En primer lugar, se han de crear los vectores de peso como variables compartidas, que en esta ocasión serán cuatro vectores de pesos y dos escalares para el <i>bias</i>. Los valores iniciales se fijan para garantizar la reproducibilidad de los resultados. Posteriormente se multiplica la matriz de entrada por los pesos para crear las tres neuronas de la primera capa e insertar las mismas en la neurona de la cuarta capa.

```python
import tensorflow.compat.v1 as tf
tf.disable_v2_behavior()
import pandas as pd
import numpy as np
# Red Neuronal XNOR con TensorFlow
# Defino las entradas
entradas = tf.placeholder("float", name='Entradas')
datos = np.array([[0, 0]
                 ,[1, 0]
                 ,[0, 1]
                 ,[1, 1]])

# Defino las salidas
uno = lambda: tf.constant(1.0)
cero = lambda: tf.constant(0.0)

with tf.name_scope('Pesos'):
    # Definiendo pesos y sesgo
    pesos = {
        'a1': tf.constant([[-1.0], [-1.0]], name='peso_a1'),
        'a2': tf.constant([[1.0], [1.0]], name='peso_a2'),
        'a3': tf.constant([[1.0], [1.0]], name='peso_a3')
    }
    sesgo = {
        'a1': tf.constant(0.5, name='sesgo_a1'),
        'a2': tf.constant(-1.5, name='sesgo_a2'),
        'a3': tf.constant(-0.5, name='sesgo_a3')
    }


with tf.name_scope('Red_neuronal'):
    # Defino las capas
    def capa1(entradas, pesos, sesgo):
        # activacion a1
        a1 = tf.reduce_sum(tf.add(tf.matmul(entradas, pesos['a1']), sesgo['a1']))
        a1 = tf.case([(tf.less(a1, 0.0), cero)], default=uno)
        # activacion a2
        a2 = tf.reduce_sum(tf.add(tf.matmul(entradas, pesos['a2']), sesgo['a2']))
        a2 = tf.case([(tf.less(a2, 0.0), cero)], default=uno)
        return a1, a2
    
    def capa2(entradas, pesos, sesgo):
        # activacion a3
        a3 = tf.reduce_sum(tf.add(tf.matmul(entradas, pesos['a3']), sesgo['a3']))
        a3 = tf.case([(tf.less(a3, 0.0), cero)], default=uno)
        return a3
```

Una vez definida la red, se ha de calcular la función de coste utilizando la entropía, las derivadas de esta con respecto a las variables compartidas y definir una función que permita actualizar los valores.

```python
# Sesion red neuronal XNOR
logs_path = "./logs"
with tf.Session() as sess:
    # para armar el grafo
    summary_writer = tf.summary.FileWriter(logs_path,graph=sess.graph)
    # para armar tabla de verdad
    x_1 = []
    x_2 = []
    out = []
    for i in range(len(datos)):
        t = datos[i].reshape(1, 2)
        # obtenos resultados 1ra capa
        a1, a2 = sess.run(capa1(entradas, pesos, sesgo), feed_dict={entradas: t})
        # pasamos resultados a la 2da capa
        ent_a3 = np.array([[a1, a2]])
        salida = sess.run(capa2(ent_a3, pesos, sesgo))
        # armar tabla de verdad en DataFrame
        x_1.append(t[0][0])
        x_2.append(t[0][1])
        out.append(salida)
    tabla_info = np.array([x_1, x_2, out]).transpose()
    tabla = pd.DataFrame(tabla_info,columns=['x1', 'x2', 'x1 XNOR x2'])
tabla
```

Finalmente se ha de entrenar la red neuronal ejecutando la función de entrenamiento una cantidad de veces. Para esto, se utilizan los siguientes vectores de entrada y salida:

<img width="138" height="119" alt="image" src="https://github.com/user-attachments/assets/30f97836-ddff-4b9e-820a-0c4c8754d0f3" />

<img width="3526" height="758" alt="image" src="https://github.com/user-attachments/assets/66767599-841c-468e-8b67-add5e428e1d9" />
