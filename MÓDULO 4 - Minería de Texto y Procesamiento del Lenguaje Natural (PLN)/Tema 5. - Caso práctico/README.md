# Caso práctico

## PARTE 1

### Se pide
A partir de lo estudiado a lo largo de la unidad, construir un bot de NLTK propio.

El chatbot puede ser de cualquier temática que resulte de interés para los estudiantes. Puede ser en inglés o en español; pero si se hace en español habrá que crear unas reflections nuevas (yo-tú, mío-tuyo…).

Los estudiantes podrán compartir su bot con los demás en el foro del máster.

### Solución

Se trata de una práctica abierta, por lo que la solución dependerá del tipo de bot elegido por los estudiantes. Se deberá partir de lo estudiado en el apartado Ejemplo "práctico: asistentes conversacionales" de la unidad.

Como punto de partida, se puede tomar el pequeño código de ejemplo disponible en el siguiente enlace.

```Python
from __future__ import print_function
from nltk.chat.util import Chat, reflections

reflections = {"yo soy":"tú eres"}

pairs = (
  (r'Necesito (.*)',
  ( "Por qué necesitas %1?",
    "Realmente te aydar %1?",
    "Estás seguro de que necesitas %1?")),
    
  (r'salir',
  ( "Gracias por hablar conmigo.",
    "Adiós.",
    "Gracias, que tengas un buen día!")),
 
  (r'(.*)',
  ( "Por favor, cuéntame más detalles.",
    "Cambiemos de tema... cuentame qué tal tu familia.",
    "Podrías ser más específico?",
    "Por qué dices %1?",
    "Entiendo.",
    "Muy interesante.",
    "%1.",
    "Ya veo.  Y eso qué representa para tí?",
    "Cómo te hace sentir eso?",
    "Cómo te sientes cuando dices eso?"))
)

chatbot = Chat(pairs, reflections)


def prueba_chat():
    print("Bot de prueba\n---------")
    print('escribe "salir" para terminar la conversación.')
    print('='*72)
    print("Hola.  ¿Qué tal estás?")

    chatbot.converse(quit='salir')
```

```Python
prueba_chat()
```

<img width="642" height="98" alt="image" src="https://github.com/user-attachments/assets/c5d0b1ab-2336-4ac3-9758-755107470fee" />

## PARTE 2. Información de partida.

### Se pide

Crear un bot propio con Wit y entrenar el sistema con unas 100 frases y con dos o más intenciones. Se deberá compartir en el foro del máster la URL de la API y el fichero de configuración.

<i>Nota</i>: para descargar el fichero de configuración de Wit, basta con descargar el archivo ZIP en la página de configuración:

<img width="954" height="199" alt="image" src="https://github.com/user-attachments/assets/674c401d-f8f6-4003-8655-4bafb96d30e1" />

### Proceso

1. Una vez exploradas las posibilidades de nltk.chat, se puede pasar a la segunda práctica de bots. Ahora se usará una API gratuita que permite construir un bot de la manera más rápida: introduciendo frases de ejemplo para entrenar el sistema.

    Para ello hay que entrar en la web de Wit y darse de alta en la plataforma (es necesario un usuario de Facebook o GitHub; si el alumno no lo tiene, tendrá que crearlo).
    
    A continuación, entrar en [este enlace](https://wit.ai/getting-started) y crear la propia app haciendo Login con Facebook o GitHub:

    <img width="958" height="595" alt="image" src="https://github.com/user-attachments/assets/707d6d32-80aa-42f9-93bb-746f2cdd0540" />

2. A continuación, se creará el nuevo bot, pulsando en el botón + de la parte superior derecha.

    <img width="981" height="139" alt="image" src="https://github.com/user-attachments/assets/2d28ab18-ac2a-4842-bb6f-0c87ee5820b6" />

3. Una vez hecho esto, se puede comenzar a entrenar el sistema. Esta API, pese a ser gratuita, funciona de forma similar a las de pago. Permite entrenar al bot para detectar cuáles son las distintas intenciones del usuario que hablará con el bot. También permite extraer una serie de entidades de dichas frases.
    
    ¿Qué es una intención? Representa un tipo genérico de pregunta del cliente a detectar por el bot. Así, por ejemplo, si la app es un camarero virtual que toma nota de la comanda, básicamente habrá dos intenciones a detectar:
    1. Pedir comida.
    2. Pedir la cuenta.
    
    Por supuesto, podrán detectarse tantas intenciones como se deseen y sean necesarias. Por ejemplo, se podría añadir la intención de saludar (“hola”, “cómo estás”, “Buenos días”…) y despedirse (“adiós”, “hasta luego”, “hasta la vista”, “hasta pronto”, etc.), para que el bot sea capaz de reconocer ese tipo de frases del usuario y responder a ellas con otro saludo.

    Siguiendo con el ejemplo del camarero virtual, dentro de la intención “pedir comida”, habrá que detectar distintas entidades. Básicamente tres: la entidad “comida” (pizza, bocadillo, pasta), la entidad “ingrediente” para identificar tanto a ingredientes (chorizo, anchoas…) como a subtipos de comida (pizza “margarita”, ensalada “César”…).

4. Ahora que ya se sabe cuál es el objetivo de la práctica, hay que comenzar el entrenamiento del sistema, que consiste en introducir frases de ejemplo e indicar, por cada frase, cuál es la intención y las entidades; eso si las hubiera, ya que podría haber intenciones sin entidades. Para ello, ha de escribirse la frase y subrayar con el ratón las distintas entidades, asignando a cada entidad un nombre.

    Después, hay que pulsar en el botón verde (validar) para que la frase con las anotaciones de comida e ingredientes que se ha creado, y con la intención “pedir comida” que también se ha creado, pase a formar parte del corpus de entrenamiento del bot.

5. De esta forma, con cada ejemplo, el bot va aprendiendo a detectar con más precisión las distintas intenciones y entidades. También se permite introducir sinónimos para las entidades. Por ejemplo, “bocata” es un sinónimo de “bocadillo” y es deseable que cuando un usuario escriba “bocata” esta entidad sea identificada como “bocadillo”. Para ello, hay que pulsar sobre la entidad “comida” e introducir sinónimos:

    <img width="967" height="471" alt="image" src="https://github.com/user-attachments/assets/a9261344-694b-4eae-9548-976c1fc678a5" />

6. Después de haber realizado un entrenamiento con unas decenas de frases distintas y con diferentes comidas e ingredientes, ya se puede empezar a utilizar este bot. Para ello, hay que pulsar sobre la pestaña Settings, arriba a la derecha.

    <img width="937" height="229" alt="image" src="https://github.com/user-attachments/assets/d71474f1-12b1-4a27-85fd-bedade010e0f" />

7. Aparecerá una pantalla desde donde se podrá configurar el acceso a la API de Wit desde los servicios que se estén utilizando, que harán llamadas a Wit enviando frases de usuarios y obteniendo el resultado del análisis de este; que, como ya se ha dicho, devuelve la intención y las entidades detectadas. Se escribirá una frase de ejemplo: “Quiero una pizza con anchoas”, y se copiará la URL de curl, para lanzar el comando desde la interfaz de comandos del sistema operativo en el ordenador utilizado, y ver si la API de Wit responde.

    <img width="945" height="485" alt="image" src="https://github.com/user-attachments/assets/783886f1-06e9-4cd3-90cf-3b4cec346a2b" />

8. Esto es lo que ocurre en la consola local al ejecutar <b>curl</b>:

    <img width="971" height="76" alt="image" src="https://github.com/user-attachments/assets/bfeb95fc-9025-4ca4-9426-ee405b83f923" />

9. Como se puede observar, la API devuelve un JSON, detectando la intención (“pedir comida”) y las entidades (“comida” e “ingredientes”), junto con la probabilidad de acierto en su predicción (de 0 a 1, representando el 1 el 100 %).

    Con este servicio, está resuelta toda la parte de PLN necesaria para implementar un bot. Si se desea implementar un bot real, sería necesario programar un front-end para que el usuario pueda chatear y, además, tener una base de datos de respuestas. Ambas cosas no tienen especial dificultad y no forman parte del contenido de esta asignatura, pero, realmente, lo único que habría que hacer es reenviar las preguntas de los usuarios a la API de Wit, obtener la intención y las entidades, consultar en la base de datos qué respuesta corresponde con dicha intención y entidades, y devolver al chat del usuario dicha respuesta.

    También existe la posibilidad de reutilizar algunas API de front-end de bot, como la de Facebook o la de Skype, de forma que los usuarios pueden usar un chat de [Facebook](https://developers.facebook.com/docs/messenger-platform/submission-process) o [Skype](https://dev.skype.com/bots) para hablar con el bot que se ha creado.
