# Caso práctico

## Cadenas de procesamiento y gramáticas JAPE. PARTE 1.
### Enunciado

A lo largo de esta práctica, se verán algunas de las posibilidades más importantes que ofrece el framework GATE, tanto para la programación de cadenas NLP como para la visualización de anotaciones. Se explicarán las gramáticas (fundamentalmente las basadas en autómatas de estados finitos) y se demostrará su utilidad mediante un ejercicio con gramáticas JAPE de GATE. El alumno deberá sencillamente sacar capturas de pantalla y pegarlas en un documento, comentando brevemente lo que se ha hecho en cada captura. El documento será único para los dos ejercicios.

Herramientas: como se ha visto, es necesario tener instalada la librería GATE.

GATE es una herramienta libre basada en Java (a diferencia de NLTK, que está programada en Python).

Sería el equivalente a NLTK + BRAT, pero en una sola herramienta. Consta de una interfaz visual que permite crear y almacenar corpus y recursos léxicos, así como procesarlos usando distintas librerías que se encadenan formado cadenas de procesamiento.

Se examinarán ahora las posibilidades que ofrece la interfaz genérica. Tal y como se ve en la figura de la herramienta GATE Developer, GATE permite guardar datos en disco (básicamente documentos de texto organizados en corpus) como datastores. Una vez que estos datos se abren, estarán cargados en memoria y se podrá hacer uso de ellos, apareciendo, por tanto, dentro de “Language Resources”. GATE viene ya con una serie de processing resources que podrá seleccionarse y cargarse haciendo clic sobre el icono del puzle verde (en este caso aparecen cargadas ya las librerías del analizador ANNIE). Con estos processing resources se podrán construir cadenas de procesamiento NLP, encadenando unos recursos con otros y aplicándolos sobre los language resources que se seleccionen.

<img width="946" height="531" alt="image" src="https://github.com/user-attachments/assets/afabb8fa-91e4-42ef-a99b-19a073b0f434" />

### Se pide

1. Cargar los PR de ANNIE (clic sobre puzle verde, seleccionar ANNIE y hacer clic sobre Apply all).
2. Crear un documento y un corpus de prueba que contenga dicho documento (clic derecho sobre Language resources y después New document o New corpus, según lo que se quiera crear. Para añadir el documento al corpus, doble clic sobre el corpus y pulsar el botón Add new document). El documento puede abrirse y editarse escribiendo un texto de prueba en inglés (ANNIE analiza en inglés).
3. Crear una cadena de procesamiento que procese el corpus (hacer clic derecho sobre Applications, después Create new application y, por último, Corpus pipeline). Los elementos del pipeline deberán ordenarse de forma lógica (si se cambia el orden de ejecución el comportamiento no será el adecuado).
4. Visualizar el resultado del proceso.
5. Probar a poner y quitar elementos del pipeline, e investigar y explicar qué funcionalidad cumple cada uno de ellos. Para ello, se deberán ejecutar distintas combinaciones del programa, pulsando el botón Run this application.

<img width="983" height="552" alt="image" src="https://github.com/user-attachments/assets/627a0afa-f005-4f43-bc3a-4928fe8c7bfb" />

Se recomienda salvar los documentos, los corpus y las applications creadas, haciendo clic derecho, después Save para que, en caso de tener problemas, se pueda volver a la última versión guardada sin comenzar todo de nuevo.

Si se desea profundizar un poco más, como tarea opcional, se puede probar a anotar textos. Ya se han visto las posibilidades para usar GATE de forma visual ejecutando cadenas de procesamiento. Pero GATE también puede usarse de un modo similar al que se llevó a cabo con INCEpTION, para anotar documentos de corpus. Los estudiantes que deseen ampliar información podrán leer la documentación correspondiente a las funcionalidades de anotación2 y, a continuación, probar a anotar distintos textos.

### Solución

GATE es una herramienta libre basada en Java, a diferencia de NLTK, que está programada en Python. Sería el equivalente a NLTK + BRAT, que se ha visto en las prácticas anteriores, pero en una sola herramienta. Consta de una interfaz visual que permite crear y almacenar corpus y recursos léxicos, y procesarlos usando distintas librerías que se encadenan formado cadenas de procesamiento.

Hay que entrar en [este enlace](https://gate.ac.uk/download/) y proceder a la descarga e instalación del programa en el sistema.

<img width="1038" height="559" alt="image" src="https://github.com/user-attachments/assets/2a9fa6ae-ae5b-4a1a-8be4-b1705cde7467" />

Se inicia la aplicación y se realizan los siguientes pasos:

1. Cargar los processing resources (PR) de ANNIE.

    <img width="664" height="358" alt="image" src="https://github.com/user-attachments/assets/dd0f5281-fee1-4b40-844a-3f4cac559881" />

     Hacer clic sobre el icono “puzle verde” (se muestra en la imagen), seleccionar ANNIE y marcar el botón Apply all. Con estos processing resources (PR) se podrán construir cadenas de procesamiento NLP, encadenando unos recursos con otros y aplicándolos sobre la pestaña
   
    Language resources (corpus + documentos), que se procesan y seleccionan posteriormente.

   <img width="1038" height="581" alt="image" src="https://github.com/user-attachments/assets/b9ec0ea9-90b7-4625-8a3c-121ccb5b69a2" />

   Una vez cargados todos los PR de ANNIE, se pincha con el botón derecho sobre el icono Processing resources y se seleccionan los PR que se van a utilizar en este ejercicio:
    - “ANNIE POS Tagger 0002A”.
    - “ANNIE Sentence Splitter 0002B”.
    - “ANNIE Gazetteer 0002E”.
    - “ANNIE English Tokeniser 0002F”.
    - “Document Reset PR 00032”.

    <img width="1038" height="247" alt="image" src="https://github.com/user-attachments/assets/71ade57a-78a9-47ef-811c-3a2e02399988" />

    En cada ventana que se abre, hay que pinchar sobre al botón Ok para finalizar su incorporación.

2. Crear un corpus y un documento de prueba.

    <img width="1038" height="558" alt="image" src="https://github.com/user-attachments/assets/af9258aa-3bb6-4a7c-ab79-4093045e32f3" />

    Hacer clic derecho sobre Language resources y después New corpus para añadir un nuevo corpus al sistema.

   <img width="1038" height="171" alt="image" src="https://github.com/user-attachments/assets/ee847112-68ad-4460-9ff0-5854b4543b67" />

   Se nombre y se pulsa sobre el botón OK. Se crea el corpus.

   <img width="927" height="477" alt="image" src="https://github.com/user-attachments/assets/f76eedf0-1b71-4013-8fc7-72e0e5ae66fb" />

   Sobre este corpus se crea un documento que se utilizará en el proceso de análisis mediante los PR de ANNIE. Para ello, hay que hacer clic con el botón derecho sobre Language resources y después New document; se nombra y se arrastra a la parte derecha de la pantalla para añadirlo al corpus creado con anterioridad. De esta manera, se pueden incluir varios documentos en un mismo corpus.

   <img width="946" height="502" alt="image" src="https://github.com/user-attachments/assets/9654bf89-7792-4701-a2f1-1974249423cd" />

   Sobre este documento, se hace doble clic y se completa el contenido en la ventana que se abre, en inglés, ya que ANNIE realiza el análisis en este idioma. En este caso, se recoge un artículo del New York Times comentando la última visita de Donald Trump a Europa.

3. Crear una cadena de procesamiento y analizar el corpus creado

    <img width="1038" height="137" alt="image" src="https://github.com/user-attachments/assets/6ba48f52-7812-4b27-8fd0-3505c2259a90" />

    Hacer clic derecho sobre Applications, seleccionar Create new application y marcar Corpus pipeline; a continuación, se nombra y se pulsa el botón Ok.

   <img width="1038" height="478" alt="image" src="https://github.com/user-attachments/assets/f1831b08-c7f0-4eac-8654-96b9bf7b5e4d" />

   Hacer doble clic sobre Corpus pipeline y el sistema mostrará la siguiente pantalla:

   <img width="916" height="487" alt="image" src="https://github.com/user-attachments/assets/4b0ae1cd-f089-4dd5-89ce-654d7b42cf5d" />

   Ahora hay que incorporar los PR de ANNIE en el orden adecuado. Para ello, pulsando la flecha verde derecha, hay que ir agregándolos a la parte izquierda en el siguiente orden:
    - “Document Reset PR 00032”.
    - “ANNIE English Tokeniser 0002F”.
    - “ANNIE Gazetteer 0002E”.
    - “ANNIE Sentence Splitter 0002B”.
    - “ANNIE POS Tagger 0002A”.
    Cuando ya estén incorporados todos estos procesos y en este orden, el usuario deberá hacer clic sobre el botón Run this application, teniendo seleccionado el corpus anteriormente creado ("Corpus master”) para que trabaje sobre él.

4. Visualizar el resultado del proceso

    <img width="1039" height="554" alt="image" src="https://github.com/user-attachments/assets/b0d0c991-142a-4c23-ae26-fcbfb8696324" />

    Si se pincha sobre la pestaña Document..., el sistema muestra el texto contenido en el mismo. Situándose en la pestaña Annotation sets, se podrá ver el resultado del análisis generado por el proceso lanzado con anterioridad.

   <img width="946" height="583" alt="image" src="https://github.com/user-attachments/assets/bd77d61b-16c7-400a-9d72-8875c8bf2385" />

   Pinchando sobre los diferentes tipos de anotaciones que existen en ANNIE (Lookup, Sentence, SpaceToken, Split y Token), se podrá ver cómo el sistema ha realizado esa anotación sobre el texto del documento.

5. Análisis del funcionamiento de cada proceso de ANNIE

    Hay que salvar el documento, el corpus y la aplicación creada en el ordenador. El orden de ejecución de los procesos, tal y como se ha señalado antes, debe ser el siguiente, teniendo en cuenta que las acciones que realiza cada uno de ellos se definen a continuación:
    - Document Reset - Resetea el procesamiento realizado anteriormente en los documentos pertenecientes al corpus a analizar. Si se elimina de la cadena, el texto mantiene los datos que son producto del análisis anterior y se suman a los del proceso que se lanza.
    - ANNIE English Tokeniser – Tokeniza el texto (tiene que ser en inglés) contenido en el documento o documentos del corpus. Genera la marca Token y la marca SpaceToken. Si se elimina este proceso, el sistema no puede realizar los siguientes (salvo ANNIE Gazetteer), ya que se encarga de descomponer en unidades tokens y prepararlo para su análisis sintáctico y semántico.
    - ANNIE Gazetteer – Trabaja como “diccionario” y localiza en el texto los nombres de entidades tales como países, ciudades, nombre de personajes, organizaciones, días de la semana, etc. y los categoriza e incluso genera una jerarquía (major type o minor type). Crea la marca Lookup.
    - ANNIE Sentence Splitter – Divide el texto en párrafos o frases. Genera la marca Split (tipo internal o punto y seguido o aparte, o external o salto de párrafo) y la marca Sentence (frase).
    - ANNIE POS Tagger – Sobre los tokens y frases encontradas, este proceso etiqueta parte del discurso como una anotación para cada palabra o símbolo de puntuación. Además, este proceso utiliza un léxico y un conjunto de reglas predeterminado, tomados de un gran corpus procedente del periódico The Wall Street Journal. Puede ser modificado manualmente.
  
## Cadenas de procesamiento y grámaticas JAPE. PARTE 2.
### Enunciado

A continuación, se probará a añadir una gramática JAPE al pipeline. JAPE es un lenguaje basado en transductores de estados finitos que permite crear complejas expresiones regulares multicapa, muy útiles para anotar textos.

Para profundizar en las técnicas y posibilidades que ofrecen estas gramáticas, puede leerse el capítulo 8 del manual de GATE en [este enlace](https://gate.ac.uk/releases/gate-8.6.1/tao/splitch8.html).

¿En qué consiste el lenguaje JAPE? Es similar a las expresiones regulares, pero más potente. Una expresión regular permite detectar, por ejemplo, todas las palabras que empiecen por “a” o por “A”, es decir, aquellas palabras cuya primera letra es una “a” mayúscula o minúscula; el resto de caracteres serán letras minúsculas y, por tanto, se excluirán espacios y otros símbolos (expresión regular: [aA][az]*).

Una gramática JAPE permite detectar eso y mucho más. Por ejemplo, se desea detectar todos los grupos de uno o dos sustantivos consecutivos (el segundo sustantivo puede estar o no, lo cual se indica con un “?”) que empiecen por una mayúscula. Por tanto, se está accediendo tanto a la capa de las letras de la palabra como a la capa morfosintáctica (un sustantivo). Esa regla (el alumno no deberá intentar ejecutarla, es simplemente un ejemplo teórico) sería algo similar a esto:

```
Rule: UnoDosSustantivosConsecutivos
{
  {Token.POS=~”N.*”, Token.string=~”[A-Z].*”}
  ({Token.POS=~”N.*”, Token.string=~”[A-Z].*”})?
}
: SustantivosMayusculas
-->
:SustantivosMayusculas.SustMay
```

Si se ejecutara esta regla, GATE recorrería el documento, buscando todos sus tokens, e intentaría encontrar uno o dos tokens seguidos que cumplieran esta regla. Cuando los encontrara, generaría una nueva anotación denominada “SustMay”.

### Se pide

Después de haber leído el capítulo antes recomendado, deberá crearse un fichero de texto plano y renombrarse con el nombre y extensión “pruebaGramatica.jape”.

Dicho fichero contendrá el primer ejemplo del tutorial online (el que comienza por “Phase: Jobtitle... y termina por “rule = jobtitle1”):

<img width="957" height="538" alt="image" src="https://github.com/user-attachments/assets/37c9ef33-d732-47d2-86b9-936001989bc4" />

Para ejecutar la gramática JAPE, hay que cargar previamente el plugin JAPE Plus:

<img width="946" height="531" alt="image" src="https://github.com/user-attachments/assets/735bc119-ecd6-41f2-9d9d-f0380dd52ab5" />

Después, deberá añadirse un nuevo processing resource que lo contenga (clic derecho sobre Processing resources, después New, JAPE Plus Transducer, y seleccionar el fichero “pruebaGramatica.jape” creado anteriormente).

A continuación, se añadirá un nuevo elemento al final del pipeline que sea precisamente esta gramática (se entiende por pipeline la cadena NLP que se ha creado antes y que contenía procesos del plugin ANNIE). Se ejecutará el pipeline (clic sobre el botón Run this application) y se mostrará cuál es el resultado.

Los estudiantes deberán investigar y explicar cómo cambian las anotaciones del documento después de ejecutar la gramática y, si quiere, podrá probar a cambiar libremente dicha gramática para ver si se detectan nuevos patrones.

Como se ha dicho, simplemente se trata de descubrir libremente las funcionalidades de la herramienta y, si se desea, capturar en un documento, a modo de recordatorio, las pantallas que demuestren que los estudiantes han estado trabajando en ello, con algún breve comentario. Así será más fácil para los estudiantes comparar estas capturas con las capturas de la solución de la práctica.

### Solución

Una gramática JAPE consiste en un conjunto de fases, cada una de las cuales consta de un conjunto de reglas o patrones de acción. Las fases se ejecutan secuencialmente y constituyen una cascada de transductores de estados finitos sobre anotaciones. Los del lado izquierdo (LHS) de las reglas se componen de una descripción del patrón de anotación. Los del lado derecho (RHS) se componen de instrucciones de manipulación de anotación. En esta práctica hay que hacer lo siguiente:

1. Crear un fichero de texto plano y nombrarlo de la siguiente forma: “pruebaGramatica. Este fichero contendrá el primer ejemplo del tutorial online, que comienza por “Phase: Jobtitle...” y termina por “rule = jobtitle1”). A continuación, se muestra el fichero creado y su contenido.

   <img width="924" height="536" alt="image" src="https://github.com/user-attachments/assets/d2a769d2-9c00-456d-b355-f4dc86a431ab" />

2. Cargar el plugin JAPE Plus en GATE. Hacer clic sobre el icono “puzle verde”, seleccionar JAPE_Plus y marcar el botón Apply all. Con este PR se podrá añadir una gramática y aplicarla sobre los archivos de Language resources (corpus + documentos) que se procesaron y seleccionaron en el primer día del ejercicio.

    <img width="1038" height="562" alt="image" src="https://github.com/user-attachments/assets/9d7e6905-2341-4114-8c2d-94059247ca33" />

3. Con el botón derecho del ratón hay que señalar Processing resources y seleccionar JAPE-Plus Transducer.

    <img width="1038" height="558" alt="image" src="https://github.com/user-attachments/assets/e9f79ebf-d2f8-46bb-8745-7a38b7889f5e" />

4. En la ventana que se presenta a continuación, en el apartado grammarURL, hay que seleccionar el fichero que se ha creado en el paso anterior, “pruebaGramatica.jape”, y pulsar Ok para finalizar su incorporación al pipeline.

    <img width="1038" height="269" alt="image" src="https://github.com/user-attachments/assets/8693fe69-ac26-4eb1-b6b5-a6b918946ab1" />

5. A continuación, se añade este nuevo proceso al final del pipeline que se conformó en el ejercicio del primer día, se ejecuta y se analiza su resultado sobre el corpus o documento que existía previamente.

    <img width="1039" height="546" alt="image" src="https://github.com/user-attachments/assets/8219f60f-0156-427d-8d70-0916007d5b66" />

La gramática cargada contiene la siguiente sintaxis:

```
Phase: Jobtitle
Input: Lookup
Options: control = appelt debug = true
Rule: Jobtitle1
(
{Lookup.majorType == jobtitle}
(
{Lookup.majorType == jobtitle}
)?
)
:jobtitle
-->
:jobtitle.JobTitle = {rule = "JobTitle1"}
```

1. Esta gramática añade la anotación “JobTitle” (profesión) que afecta al elemento Lookup, creado anteriormente mediante el proceso ANNIE Gazetteer, identificando este elemento en el texto del documento. A continuación, se muestra el resultado y el detalle de cada elemento en la parte inferior de la pantalla (recuadro rojo).

    <img width="997" height="540" alt="image" src="https://github.com/user-attachments/assets/e9edb086-96c9-471f-960e-81bdc08dfe2f" />

2. Si el usuario desea asignar una nueva anotación de este tipo (o de cualquier otro), hay que situarse sobre la palabra en concreto y hacer un doble clic para que aparezca el menú contextual de anotación. Entonces, hay que seleccionar la anotación dentro del combo existente y definir sus atributos.

    <img width="1038" height="819" alt="image" src="https://github.com/user-attachments/assets/99c8458c-85fb-4967-93c1-fba9eec08d55" />
