# CASO PRÁCTICO 1. Creación de cadenas NLP con NLTK
## Enunciado

En esta práctica se va a crear una función donde, pasándole un texto, devuelva una tabla con la cantidad de veces que se repite una palabra y la densidad que hay de esta en el texto.

El notebook base para poder resolver el ejercicio se puede descargar en el siguiente enlace.

[WXiuuSPLxvv20Mx_-Practica%20NLTK.ipynb](https://github.com/user-attachments/files/26323226/WXiuuSPLxvv20Mx_-Practica.20NLTK.ipynb)

## Se pide 

Generar una función que represente una tabla con tres columnas donde se tenga:
- Token: la palabra buscada.
- Conteo: el número de apariciones que tiene esta palabra en el texto.
- Densidad: el porcentaje (%) que representa esa palabra en el texto.

La función tendrá dos argumentos: uno donde se pasará el texto y otro argumento para activar o desactivar la lematización del texto; de esta manera se podrán comparar los resultados.

## Solución

El resultado final será algo similar a lo siguiente: 

```python
# NLTK
import nltk
    
# NLTK Word Tokenize
from nltk.tokenize import word_tokenize
    
# NLTK StopWords
from nltk.corpus import stopwords
    
# Spacy
import spacy
nlp = spacy.load('es_core_news_sm')
    
# Pandas
import pandas as pd
```

```Python
def text_density(content, clean):
      
    #Tokenizar    
    tokens = [word.lower() for word in word_tokenize(content, "spanish") if word.isalpha()]
    
    #Eliminar stopwords
    clean_tokens = tokens[:]
    for token in tokens: 
        if token in stopwords.words('spanish'): 
            clean_tokens.remove(token)
    
    # Utilizar lematización o utilizar las palabras según se introducen
    cleaned_tokens =[]
    
    if clean:
        #Realizar lematización si 'clean' es True
        separator = ' '
        for token in nlp(separator.join(clean_tokens)):
            cleaned_tokens.append(token.lemma_)
    else:
        #Sin lematización si 'clean' es False
        cleaned_tokens = clean_tokens
        
    #Generamos la tabla para representar los datos
    conteo= pd.DataFrame(columns = ['Palabra', 'Recuento', 'Densidad'])
    
    #Esta Función nos dice la frecuencia de los tokens 'cleaned_tokens' contendrá los tokens lematizados o sin lematizar
    freq_clean = nltk.FreqDist(cleaned_tokens)

    for key,val in freq_clean.items():
        #En este blucle for deberemos insertar las columnas
        dens = "{:.2%}".format(val/len(cleaned_tokens))
        fila = pd.Series([key, "{:.0f}".format(val), dens], index=conteo.columns)
        conteo = conteo.append(fila, ignore_index=True)
    
    
    #La variable result contendrá la tabla ordenada por la densidad
    result = conteo.sort_values('Densidad',ascending=False)
    
    return result
```

```Python
text = 'Me he comprado un coche rojo. Ahora tenemos que encontrar un seguro de coches a todo riesgo'

text_density(text, True)
```

<img width="203" height="205" alt="image" src="https://github.com/user-attachments/assets/0d36e989-8f32-463d-91f1-4d5ca0d32dca" />

# CASO PRÁCTICO 2. Aprendizaje automático en taggers
## Enunciado

En este ejercicio se verán de forma práctica los conocimientos teóricos adquiridos en la unidad sobre cómo funcionan los <i>taggers</i> y el <i>parser</i>. Para ello, pondrá el foco en realizar un extractor de comandas para un restaurante.

<b>Información de partida</b>:

Una importante cadena de restaurantes quiere implantar un sistema de comandas por chat, de esta forma los clientes simplemente tendrán que escribir su comanda por una <i>tablet</i> en la mesa y el asistente virtual se encargará de gestionar el pedido con la cocina y los camareros.

El restaurante necesita tener un listado de los platos y las bebidas por separado junto con el número de unidades que se piden de cada elemento.

## Se pide 

Realizar el extractor de comandas que cumpla con las necesidades del restaurante.

## Solución

### Importación de librerías

Trabajaremos con la librería NLTK, con el tokenizador incluido en la librería, el corpus cess_esp y los 4 taggers vistos en la unidad. Tendremos que importar también el RegEx Parser de NLTK.

Por último, como complementos no obligatorio pero que utilizaremos para dar formato o hacer más sencillo el trabajo, train_test_split de sklearn y pandas.

```Python
#Importamos la librería base NLTK
import nltk

#Importamos el componente de NLTK para tokenizar
from nltk.tokenize import word_tokenize

#Importamos el corpus CESS en Español
from nltk.corpus import cess_esphgbbg

#Taggers ngrams y HMM
from nltk import UnigramTagger, BigramTagger, TrigramTagger
from nltk.tag.hmm import HiddenMarkovModelTagger

#RegEx Parser
from nltk.chunk.regexp import *


#Esto nos permitirá crear los conjuntos de test y train
from sklearn.model_selection import train_test_split

#Importamos por último pands
import pandas as pd
```

Ahora ya tenemos todo lo necesario para emprezar a trabajar con los corpus y los taggers.

### Entrenamiento de los taggers

Para entrenar los <i>taggers</i> lo que tenemos que hacer es traernos el corpus taggeado en español. Antes, veamos que contiene ese <i>corpus</i>. 

```Python
import nltk
nltk.download('cess_esp')
cess_esp.sents()
```

<img width="1226" height="32" alt="image" src="https://github.com/user-attachments/assets/c73dff50-802b-443a-aedc-124eb5c6b6c7" />

```Python
cess_esp.tagged_sents()
```

<img width="878" height="46" alt="image" src="https://github.com/user-attachments/assets/d73927b5-d109-4f25-bdeb-e0f075121450" />

Como vemos con el comando `cess_esp.sents()` nos traemos un conjunto de frases tokenizadas de distintas temáticas.

Y con el comando `cess_esp.tagged_sents()` nos traemos ese mismo conjunto de frases ya taggeadas.

Ahora lo que haremos será crear 2 conjuntos de tokens taggeados. Uno que contenga el 90% de los tokens y otro que contenga el 10%, uno para train y otro para test respectivamente.

```Python
#Generamos los conjuntos de Train y Test
data_train, data_test = train_test_split(cess_esp.tagged_sents(), test_size=0.10, random_state=1)

print('Token de entrenamiento:',len(data_train),
      '\nTokens de test:    ',len(data_test))
```

<img width="173" height="36" alt="image" src="https://github.com/user-attachments/assets/9224c9b2-4dc0-4982-829c-cc64c19f6f6b" />

Teniendo los conjuntos ya creados, pasamos a entrenar los taggers. 

Para entrenar los **ngram** deberemos ejecutar el tagger con el corpus, por ejemplo `UnigramTagger(data_train)`. Veremos que los ngram pueden tener como backoff otro ngram.

En el caso de **HiddenMarkovModelTagger** deberemos ejecutar la función `.train()`.

```Python
unigram  = UnigramTagger(data_train)
bigram   = BigramTagger(data_train, backoff=unigram)
trigram  = TrigramTagger(data_train, backoff=bigram)
hmm      = HiddenMarkovModelTagger.train(data_train)
```

Una vez entrenados los taggers, vamos a evaluar cómo es el tendimiento de cada uno de ellos con el conjunto de test. Para evaluarlo tenemos que utilizar la función `train()`, para todos los taggers. Veamos qué tal funciona cada uno de ellos.

Cuando ejecutes el entrenamiento presta atención al tiempo que tarda cada uno de los taggers en mostrar la puntuación. Mientras que los ngram son bastante rápidos para extraer la información, el HMM tarda más tiempo en obtener los datos.

```Python
print ('Acierto con unigramas: %.2f %%' % (unigram.accuracy(data_test)*100))
print ('Acierto con bigramas:  %.2f %%' % (bigram.accuracy(data_test)*100))
print ('Acierto con trigramas: %.2f %%' % (trigram.accuracy(data_test)*100))
print ('Acierto con HMMs:      %.2f %%' % (hmm.accuracy(data_test)*100))
```

<img width="184" height="62" alt="image" src="https://github.com/user-attachments/assets/287f4c39-72b6-45f2-9f81-30c06ea9e456" />

Ahora, podemos volver a entrenar los taggers con los datos de test. Aunque no apreciaremos una gran mejora en terminos generales, como el volumen de datos que estamos utilizando es pequeño, nos será de ayuda.

Veremos, que si evaluamos los taggers de nuevo en el conjunto de test, obtendremos casi un 100% de acierto. Esta mejoría es mayor en los ngramas puesto que son reglas más 'logicas' por así decirlo, por lo que con pequeñs vólumenes de datos veremos mayor acierto. En cambio, en el HMM, vemos mejor mejoría en el caso de evaluar sobre los datos pero en aquellos tokens no entrenados tendremos mejor rendimiento que el resto.

```Python
unigram  = UnigramTagger(data_test)
bigram   = BigramTagger(data_test, backoff=unigram)
trigram  = TrigramTagger(data_test, backoff=bigram)
hmm      = HiddenMarkovModelTagger.train(data_test)

print ('Acierto con unigramas: %.2f %%' % (unigram.evaluate(data_test)*100))
print ('Acierto con bigramas:  %.2f %%' % (bigram.evaluate(data_test)*100))
print ('Acierto con trigramas: %.2f %%' % (trigram.evaluate(data_test)*100))
print ('Acierto con HMMs:      %.2f %%' % (hmm.evaluate(data_test)*100))
```

<img width="186" height="62" alt="image" src="https://github.com/user-attachments/assets/eafdbb2b-2968-4d3e-878c-075998ccda16" />

Como hemos visto que el HMM tiene mejor rendimiento, a priori, utilizaremos este para elaborar nuestro bot de comandas.

### Comenzar a elaborar el bot

Ahora crearemos una frase de la temática de nuestro bot para ver cómo es el rendimiento con nuestro conjunto de datos.

```Python
food_text = 'Quiero unos macarrones con queso y una cerveza'
```

El primer paso será elaborar los tokens de la frase. Para los taggers no es necesario que eliminemos las stopwords, lematicemos o derivemos, al contrario. Si hacemos todos estos pasos estaremos eliminando información que utilizarán los taggers para encontrar las etiquetas.

```Python
import nltk
nltk.download('punkt')
nltk.download('punkt_tab')

tokens = nltk.word_tokenize(food_text)
tokens
```

<img width="419" height="32" alt="image" src="https://github.com/user-attachments/assets/db944689-a025-4526-8953-c881d273ec1f" />

Una vez tengamos los tokens, utilzaremos la función `.tag()`.

```Python
food_tagged = hmm.tag(tokens)
food_tagged
```

<img width="161" height="124" alt="image" src="https://github.com/user-attachments/assets/be43b653-2236-4053-addd-e2a847002d29" />

Podemos ver que los tags obtenidos no son del todo correctos. Para comprobarlos, debemos revisar los tags EAGLES del enlace facilitado en el temario: https://www.cs.upc.edu/~nlp/tools/parole-sp.html

De forma resumida, utilizaremos estos tags, aunque podemos tener variaciones e incorporar otros;

- **ncms000** : nombre común masculino singular
- **ncfs000** : nombre común femenino singular
- **ncmp000** : nombre común masculino plural
- **ncfp000** : nombre común femenino plural

- **np0000p/np00001** : nombre propio (La incluimos porque fijandonos en como etiqueta nuestros ejemplos podemos comprobar que para algunas palabras le pone este etiquetado(ej: bocadillo de atún). Tambien podría darse el caso de que alguna comida siguiera esta estructura correctamente (ej: pizza de Toni)


- **di0ms0** : determinante indefinido masculino singular
- **di0fs0** : determinante indefinido femenino singular
- **di0mp0** : determinante indefinido masculino plural
- **di0fp0** : determinante indefinido femenino plural
- **dn0cp0** : determinante indefinido comun plural


- **sps00** : Preposición


- **da0ms0**: el
- **da0fs0**: la
- **da0mp0**: los
- **da0fp0**: las
- **da0ns0**: lo

Repasemos la frase:

 * ('Quiero', 'da0mp0') -> Taggeado como un determinante, debería ser: vmpip1s0 que corresponde a presente de indicativo
 * ('unos', 'di0mp0') -> Taggeado como determinante masculino, debería ser: mcmp00 que corresponde a un numeral ordinal masculino
 * ('macarrones', 'ncmp000'), -> **Correcto**: Taggeado como Sustantivo Común Masculino Plural
 * ('con', 'sps00'), -> **Correcto**: Taggeado como preposición
 * ('queso', 'np0000l'), -> Taggeado como Sustantivo Propio, debería ser: ncms000 sustantivo común masculino singular
 * ('y', 'cc'),-> **Correcto**: Taggeado como conjunción coordinada
 * ('una', 'di0fs0'),-> Taggeado como determinante femenino, debería ser: mcfp00 que corresponde a un numeral ordinal femenino
 * ('cerveza', 'ncfs000')-> -> **Correcto**: Taggeado como sustantivo femenino singular
 
 Como hemos visto, correctamente taggeados tendríamos 4 tokens de 8, un 50% de aciertos. Si evaluamos estos tags con el rendimiento de, por ejemplo el trigram ¿Qué % de acierto tendremos? Comprobemoslo.

 ```Pyton
print ('Acierto con unigramas: %.2f %%' % (unigram.accuracy([food_tagged])*100))
print ('Acierto con bigramas:  %.2f %%' % (bigram.accuracy([food_tagged])*100))
print ('Acierto con trigramas: %.2f %%' % (trigram.accuracy([food_tagged])*100))
print ('Acierto con HMMs:      %.2f %%' % (hmm.accuracy([food_tagged])*100))
```

<img width="188" height="66" alt="image" src="https://github.com/user-attachments/assets/30f635a3-d502-47c6-b448-277f41224193" />

Como vemos, HMM dice que su acierto es del 100%, tiene lógica puesto que es ese tagger el que ha hecho los tags. En cambio el resto de los tags, coinciden en la corrección que hemos hecho, aunque esto no quiere decir que esos tags acierten 8 de 8 etiquetas, comprobemoslo.

```Python
print ('Unigramas:', (unigram.tag(tokens)))
print ('Bigramas: ', (bigram.tag(tokens)))
print ('Trigramas: ', (trigram.tag(tokens)))
```

<img width="873" height="52" alt="image" src="https://github.com/user-attachments/assets/f4948713-c405-4a34-903f-ff65426d9a51" />

Ahora que hemos visto estos resultados, confirmamos que el que mejor rendimiento ha tenido es HMM, que ha encontrado etiquetas, que aunque no del todo correctas han sido aproximadas, en algunos casos ha confundido el género, en otros el número aunque esto no afectaría demasiado a nuestra extracción de información. Pero en general ha etiquetado en tipo de palabra 6 de los 8 tokens.

Los ngrams, no han podido identificar los tokens en el 50% de los casos. Por lo que habríamos tenido problemas a la hora de utilizarlos como taggers.

### Corregir el tagger

Ahora que hemos corregido los tags, es hora de volver a entrenar el tagger con la frase correcta, por lo que vamos a ello.

Vamos a también a trabajar con el foodTagger (es un HMM entrenado con nuestras frases de comida).

```Python
corrected_tokens = [('Quiero', 'vmpip1s0'), ('unos', 'mcmp00'), ('macarrones', 'ncmp000'), ('con', 'sps00'), ('queso', 'ncms000'), ('y', 'cc'), ('una', 'mcfp00'), ('cerveza', 'ncfs000')]

foodTagger = hmm.train([corrected_tokens])
```

Ahora, una vez entrenado el tagger, si volvemos a pasar la misma frase acertará con todos ellos puesto que está entrenado para detectar los tags.

```Python
food_tagged = foodTagger.tag(tokens)
food_tagged
```

<img width="161" height="115" alt="image" src="https://github.com/user-attachments/assets/3e28b6c2-55df-4561-ad7a-0592b0182c8c" />

La corrección del tagger es un proceso que deberemos elaborar repetidamente para conseguir mejorar los resultados. Es un proceso que podríamos acortar en gran manera si tuviesemos un corpus con miles de frases y tokens como el inicial, pero de nuestro contexto en concreto.

### Elaborar una función que reconozca las comandas

Para ello tendremos que utilizar RegEx Parser y las reglas lógicas. En nuestro caso, podemos utilizar las que hemos visto en la teoría de esta unidad.

- nombre común : *macarrones*

- nombre común + nombre (común/propio) : *pizza margarita*

- nombre común + preposición + nombre(común/propio) : *bocadillo de atún*

- nombre común + preposición + artículo + nombre(común/propio) : *lentejas a la riojana*

```Python
reglas = r'''
    cantidad: {<mccp00>}
    comida: {<ncms000|ncfs000|ncmp000|ncfp000>*<sps00>*<da0ms0|da0fs0|da0mp0|da0fp0|da0ns0>*<ncms000|ncfs000|ncmp000|ncfp000|np0000l|np0000p>}
    cantidad: {<di0ms0|di0fs0|di0mp0|di0fp0|dn0cp0|mcmp00|mcfp00> || <mcmp00>* || <mcfp00> }
      '''
```

Ahora ya tenemos la gramática creada, vamos a crear la función del regex que extraiga la información.

```Python
RegexP = nltk.RegexpParser(reglas)

def parsear(phrase):
    return RegexP.parse(phrase)
```

```Python
frase_regex = parsear(corrected_tokens)
print(frase_regex)
```

<img width="315" height="104" alt="image" src="https://github.com/user-attachments/assets/a4d52996-17fa-47f3-bf10-3c02c2b7ceec" />

#### Función para extraer los nodos clasificados

Una vez hemos conseguido identificar la comida y la cantidad de la comanda, generaremos un JSON con los datos de la comanda.

```Python
def genera_comanda(tree):
    
    result = []
    
    item = {}
    item['item'] = None
    item['cantidad'] = 0
    
    elementos = 0
    
    #En primer lugar contaremos cuantos elementos hay en el pedido
    for nodo in tree:
        if type(nodo) == tuple:
            continue
        tipo = nodo.label()
        if tipo == 'comida':
            elementos += 1
            
    #Ahora generaremos cada línea de pedido con sus cantidades
    for nodo in tree:
        if type(nodo) == tuple:
            continue
        
        count = 0
        valor = ''
        
        for elemento in nodo:
            count += 1
            palabra, categoria = elemento
                
            if count == 1:
                valor = valor + palabra
            else:
                valor = valor + ' ' + palabra
            
            if nodo.label() == 'cantidad':
                item['cantidad'] = valor
            else:
                item['item'] = valor
        
        if nodo.label() == 'comida':
            result.append(item)
            item = {}
            #print(item)
        
    return result
```

```Python
genera_comanda(frase_regex)
```

<img width="324" height="41" alt="image" src="https://github.com/user-attachments/assets/ac0b694c-52ab-43ea-bc5c-440d42f870aa" />

Ahora que la función nos genera la comada, generaremos una nueva función que lo haga desde 0.

```Python
def procesa_frase(frase):
    
    tokens = nltk.word_tokenize(frase)
    print('Tokens:')
    print(tokens)
    print('\n', '-----------------------------------------', '\n')
    tags = foodTagger.tag(tokens)
    print('TAGS:')
    print(tags)
    print('\n', '-----------------------------------------', '\n')
    parsed = parsear(tags)
    print('Parsed:')
    print(parsed)
    print('\n', '-----------------------------------------', '\n')
    
    return genera_comanda(parsed)    
```

Y por último, testeamos la función que hemos creado para analizar frases completas.

```Python
fraseTest = 'pedir dos pizzas cuatro quesos y cinco fantas'

procesa_frase(fraseTest)
```

<img width="887" height="293" alt="image" src="https://github.com/user-attachments/assets/4efafc72-6265-4e8b-9aa8-9c1226491d21" />
