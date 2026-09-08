# Caso práctico con solución

La actividad se estructura en tres partes crecientes en esfuerzo requerido. La premisa es similar: el alumno deberá elegir un hashtag y ejecutar un ejercicio parecido.

## Enunciado

Programas como Volando voy suelen tener una respuesta generalmente positiva (es decir, el interesado en el programa o la región comenta en positivo si quiere, pero si no le gusta no suele comentar). Esto hace que las comunidades se dividan en áreas de influencia o interés. Pero hay otro caso interesante: el debate. Para seguir con la televisión, programas como Al Rojo Vivo o La Sexta noche suelen girar en torno a temas que generan división de opiniones y reacciones. Además, suelen incluir un hashtag concreto para cada uno de esos temas, así que es relativamente sencillo monitorizarlos. De cara a este ejercicio, por tanto, hay varios casos posibles, como los debates ya mencionados, los eventos deportivos (que se dividen por simpatías), concursos… Cualquiera de estas opciones os dará facilidades a la hora de entender los resultados obtenidos en el ejercicio intermedio, pero son solo recomendaciones; el tema es libre.

### Ejercicio básico

Para el ejercicio básico vamos a utilizar únicamente Gephi. Se debe cargar la red proporcionada en el siguiente enlace: (1_uclfinal.gephi), que corresponde, por ejemplo, a una extracción de unos minutos antes de la final de la Champions League, y ejecutar el mismo guion/idea base que en el apartado 6.5. Como entregable se espera:

- Capturas de pantalla de Gephi (al menos, la inicial tras la carga del fichero, la final y una intermedia del proceso).
- ¿Cuáles son las principales comunidades obtenidas? ¿Y los usuarios de mayor importancia? ¿Los podrías dividir en bandos y en neutrales?

#### Solución

Tras la carga y varias operaciones, el grafo puede quedar, por ejemplo, así: (Nótese que ni es la visualización más ideal posible ni estoy mostrando las etiquetas).

<img width="655" height="495" alt="image" src="https://github.com/user-attachments/assets/aaaca0e9-77db-463b-9993-4ad1f1c97721" />

### Ejercicio intermedio

Para el ejercicio intermedio vamos a utilizar las posibilidades de la API de Twitter de forma distinta: a partir de un plugin de Gephi llamado Twitter Streaming Importer que facilita la tarea de almacenar tuuits de forma automática.

1. Instalar el plugin de Gephi en Tools > Plugins.

    <img width="886" height="559" alt="image" src="https://github.com/user-attachments/assets/363ec871-1a0d-48df-a8d4-30e4dab20c6e" />

2. Mostrarlo en el menú Window > Twitter Streaming Importer.
3. Introducir las claves de la API (ver el ejemplo para saber de dónde obtenerlas).
4. En el siguiente enlace se facilita un tutorial base de Bill Wolff (se recomienda poner el vídeo a 1080p o 720 p):

    [Gephi Streaming Twitter Importer Tutorial](https://www.youtube.com/watch?v=Vryp2yCgC4Y).

5. Seleccionad el hashtag (o los hashtag) de vuestra elección, añadidlos (ADD) y seleccionad User Network como lógica para aplicar. Por ejemplo, para el ejercicio básico se usó el que se muestra en la figura.

    <img width="501" height="666" alt="image" src="https://github.com/user-attachments/assets/d056e681-96da-4141-8672-903ce9c907ad" />

6. Conectar el plugin (en Connect) y volver a la vista general. Arriba a la derecha, en Contexto, veréis que se va incrementando el número de nodos. Esperad a tener unos 2000, por lo menos, y desconectad el plugin.

    Como entregable se espera el grafo obtenido de la extracción, utilizando File > Save As (o guardar como) y guardado en el formato por defecto, (.gephi).

    Debería ocupar unos cientos de KB, pero no mucho más.

    <img width="701" height="431" alt="image" src="https://github.com/user-attachments/assets/3e2607bc-0751-401a-bbef-462be60c2d3b" />

#### Solución

La solución para la parte intermedia pasa por ser capaz de obtener las claves de la API de Twitter (detallado en el caso práctico) y utilizar el plugin propuesto (se incluye el tutorial en vídeo en el enunciado). Tras esto, basta con usar cualquier hashtag que esté, por ejemplo, entre los trending topic en el momento de la ejecución o esperar a un evento (debate, encuentro deportivo, programa…) que use uno.

### Ejercicio avanzado

Con los datos extraídos en el ejercicio intermedio (el grafo obtenido), se solicita buscar las comunidades y realizar una interpretación de estas, es decir:
- Que ejecutéis la misma dinámica que en el ejercicio básico, pero sobre vuestra propia extracción.
- Y que extraigáis unas conclusiones mucho más detalladas, al estilo de las del caso práctico visto en la unidad (en el ejercicio base se pide menos detalle).

#### Solución

Tras obtener los datos del punto intermedio, se trata de ejecutar los mismos pasos o la misma idea que en el caso práctico. El grafo tendrá distinta forma y comunidades en función del tema elegido.
