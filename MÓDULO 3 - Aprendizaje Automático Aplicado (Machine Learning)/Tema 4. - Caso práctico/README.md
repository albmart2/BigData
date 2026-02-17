# Caso práctico

## Enunciado

El archivo “myopia.csv”, disponible en esta sección, contiene los datos de un estudio llevado a cabo durante cinco años en el que se observó la salud ocular de una población. Los registros se corresponden con los valores tomados inicialmente en el mismo, y existe una variable, MYOPIC, en la que se registra si a los sujetos se les diagnosticó miopía durante el estudio.

Las variables son:

- <i>ID</i>: identificador ID.
- <i>STUDYYEAR</i>: año en el que se inició el estudio.
- <i>MYOPIC</i>: desarrollo de la miopía durante los primeros cinco años.
- <i>AGE</i>: edad en la primera visita.
- <i>GENDER</i>: sexo.
- <i>SPHEQ</i>: refracción esférica equivalente.
- <i>AL</i>: longitud axial.
- <i>ACD</i>: profundidad de cámara anterior.
- <i>LT</i>: grosor de la lente.
- <i>VCD</i>: profundidad de cámara vítrea.
- <i>SPORTHR</i>: cuántas horas a la semana, fuera de la escuela, participa el niño en deportes o actividades al aire libre.
- <i>READHR</i>: cuántas horas a la semana, fuera de la escuela, lee el niño por placer.
- <i>COMPHR</i>: cuántas horas a la semana, fuera de la escuela, pasa el niño jugando a videojuegos de ordenador o frente a la pantalla.
- <i>STUDYHR</i>: cuántas horas a la semana, fuera de escuela, dedica el niño a las tareas escolares, leyendo o estudiando.
- <i>TVHR</i>: cuántas horas a la semana, fuera de la escuela, ve la televisión el niño.
- <i>DIOPTERHR</i>: compendio de horas de actividades de trabajo que se define como:

    ```DIOPTERHR = 3 (READHR + STUDYHR) + 2 COMPHR + TVHR```

- <i>MOMMY</i>: ¿La madre del niño es miope?
- <i>DADMY</i>: ¿El padre del niño es miope?

## Se pide

A partir de este conjunto de datos, crear un modelo para predecir la aparición de miopía en el grupo de estudio.

## Solución

Inicialmente, se han de cargar los datos del archivo. Una vez hecho esto, se han de analizar los tipos de características, para lo que hay que contar el número de registros en cada nivel.

```Python
%pylab
%matplotlib inline

%config InlineBackend.figure_format = 'retina'
```

```Python
import pandas as pd

myopia = pd.read_csv('myopia.csv', sep = ';')

# Separación de la variable objetivo y las explicativas
target = 'MYOPIC'
features = list(myopia.columns)
features.remove('MYOPIC')

# Listado de variables disponibles para hacer un modelo.
for var in features:
    print (var , ':' , len(set(myopia[var])))
```

- ID : 618
- STUDYYEAR : 6
- AGE : 5
- GENDER : 2
- SPHEQ : 511
- AL : 254
- ACD : 206
- LT : 128
- VCD : 226
- SPORTHR : 40
- READHR : 16
- COMPHR : 18
- STUDYHR : 14
- TVHR : 28
- DIOPTERHR : 75
- MOMMY : 2
- DADMY : 2

```Python
from pandas.plotting import scatter_matrix
import matplotlib.pyplot as plt

scatter_matrix(myopia, figsize=(12, 12), diagonal='kde')
plt.show()
```

<img width="160" height="449" alt="image" src="https://github.com/user-attachments/assets/4b5d0a52-8bb4-4d7b-a480-1c81828debb9" />

### Eliminación de las variables que son identificadores

```Python
features.remove('ID')
features.remove('STUDYYEAR')
```

### Análisis de las variables discretas

```Python
myopia[features].head()
```

<img width="549" height="122" alt="image" src="https://github.com/user-attachments/assets/df80b1f3-52f5-4423-9c03-2cd6e8d8efcb" />

```Python
categorical = ['AGE', 'GENDER', 'MOMMY', 'DADMY']
continuous = ['SPHEQ', 'AL', 'ACD', 'LT', 'VCD', 'SPORTHR' ,'READHR', 'COMPHR', 'TVHR', 'DIOPTERHR']

for var in categorical:
    print ("Tabla de frecuencias para:", var)
    print (pd.crosstab(myopia[target], myopia[var]))
    print
```

<img width="167" height="205" alt="image" src="https://github.com/user-attachments/assets/e9bb3452-9d62-4b0e-86ed-9ec9f9890da2" />

#### Variable: ```AGE```

```Python
def get_WoE(data, var, target):
    crosstab = pd.crosstab(data[target], data[var])
    
    print ("Obteniendo el Woe para la variable", var, ":")
    
    for col in crosstab.columns:
        if crosstab[col][1] == 0:
            print ("  El WoE para", col, "[", sum(crosstab[col]), "] es infinito")
        else:
            print ("  El WoE para", col, "[", sum(crosstab[col]), "] es", np.log(float(crosstab[col][0]) / float(crosstab[col][1])))
```

```Python
get_WoE(myopia, 'AGE', target)
```

<img width="200" height="62" alt="image" src="https://github.com/user-attachments/assets/8687a8aa-e4c3-4879-8960-9507f4f2d8b9" />

```Python
import numpy as np
myopia.loc[:, 'AGE_grp'] = None

for row in myopia.index:
    if myopia.loc[row, 'AGE'] <= 7:
        myopia.loc[row, 'AGE_grp'] = True
    else:
        myopia.loc[row, 'AGE_grp'] = False

get_WoE(myopia, 'AGE_grp', target)
```

<img width="215" height="33" alt="image" src="https://github.com/user-attachments/assets/b0b3386c-b4a4-4c19-8e56-0d373aa48bac" />

```Python
features.remove('AGE')
features.append('AGE_grp')

categorical.remove('AGE')
categorical.append('AGE_grp')
```

#### Evaluación del IV

```Python
from sklearn.linear_model import LogisticRegression

def calculateIV(data, features, target):
    result = pd.DataFrame(index = ['IV'], columns = features)
    result = result.fillna(0)
    var_target = np.array(data[target])
    
    for cat in features:
        var_values = np.array(data[cat])
        var_levels = np.unique(var_values)

        mat_values = np.zeros(shape=(len(var_levels),2))
        
        for i in range(len(var_target)):
            for j in range(len(var_levels)):
                if var_levels[j] == var_values[i]:
                    pos = j
                    break

            # Estimación del número valores en cada nivel
            if var_target[i]:
                mat_values[pos][0] += 1
            else:
                mat_values[pos][1] += 1

            # Obtención del IV
            IV = 0
            for j in range(len(var_levels)):
                if mat_values[j][0] > 0 and mat_values[j][1] > 0:
                    rt = mat_values[j][0] / (mat_values[j][0] + mat_values[j][1])
                    rf = mat_values[j][1] / (mat_values[j][0] + mat_values[j][1])
                    IV += (rt - rf) * np.log(rt / rf)
                    
        # Se agrega el IV al listado
        result[cat] = IV
        
    return result

calculateIV(myopia, categorical, target)
```

<img width="176" height="40" alt="image" src="https://github.com/user-attachments/assets/6a21b01b-512f-46c6-9b5c-25c324dccc41" />

### Análisis de las variables continuas

El resto de las variables que quedan son númericas. Se pueden analizar para ver cómo se relacionan con la variable objetivo.

```Python
import matplotlib.pyplot  as plt
for var in continuous:
    f, axarr = plt.subplots(2, sharex = True)
    
    axarr[0].hist(myopia[var][myopia[target]==0])
    axarr[1].hist(myopia[var][myopia[target]==1])
    
    axarr[0].set_ylabel('False')
    axarr[1].set_ylabel('True')
    axarr[0].set_title(var)
```

#### Variable: ```SPHEQ```

```Python
myopia.loc[:, 'SPHEQ_grp'] = myopia['SPHEQ'].map(lambda x: 'n0' if x < 0.05 else 'n1' if x < 0.6 else 'n2')
get_WoE(myopia, 'SPHEQ_grp', target)
calculateIV(myopia, ['SPHEQ_grp'], target)
```

<img width="212" height="41" alt="image" src="https://github.com/user-attachments/assets/7b448a0b-0311-45e0-93c3-a8823465fa33" />

Eliminación de las variables modificadas.

```Python
features.remove('SPHEQ')
features.append('SPHEQ_grp')

continuous.remove('SPHEQ')
categorical.append('SPHEQ_grp')
```

### Creación de un modelo

```Python
use_features = features[:]
use_features.remove('SPHEQ_grp')

data_model = pd.concat([myopia[use_features], pd.get_dummies(myopia['SPHEQ_grp'], prefix = 'pclass')], axis = 1)
```

#### Eliminación de variables colineales

```Python
from sklearn.linear_model import LinearRegression
import numpy as np
import pandas as pd

def calculateVIF(data):
    features = list(data.columns)
    num_features = len(features)
    
    model = LinearRegression()
    
    result = pd.DataFrame(index=['VIF'], columns=features, dtype=float)
    result = result.fillna(0.0)
    
    for ite in range(num_features):
        x_features = features[:]
        y_featue = features[ite]
        x_features.remove(y_featue)
        
        X = data[x_features]
        y = data[y_featue]
        
        model.fit(X, y)
        r2 = model.score(X, y)
        
        if r2 >= 0.999999:   # R² ≈ 1 -> VIF infinito
            vif = np.inf
        else:
            vif = 1.0 / (1.0 - r2)
        
        result[y_featue] = vif
    
    return result
```

```Python
calculateVIF(data_model)
```

<img width="673" height="47" alt="image" src="https://github.com/user-attachments/assets/96cdfc71-3a3a-4455-9b8f-ecf4d89983a2" />

```Python
model_vars = selectDataUsingVIF(data_model)
calculateVIF(model_vars)
```

<img width="610" height="38" alt="image" src="https://github.com/user-attachments/assets/9051a2bf-54cf-4da8-ae03-12f2e576d06d" />

#### Separación de las variables en conjunto de muestra y validación

```Python
from sklearn.model_selection import train_test_split

x_train, x_test, y_train, y_test = train_test_split(model_vars, myopia[target])
```

### Creación de un modelo y validación de un modelo

```Python
from sklearn.metrics import accuracy_score, auc, confusion_matrix, f1_score, precision_score, recall_score, roc_curve

def metricas_modelos(y_true, y_pred):
    from sklearn.metrics import accuracy_score, auc, confusion_matrix, f1_score, precision_score, recall_score, roc_curve

    # Obtención de matriz de confusión
    confusion_matrix = confusion_matrix(y_true, y_pred)

    print ("La matriz de confusión es ")
    print (confusion_matrix)

    print ('Precisión:', accuracy_score(y_true, y_pred))
    print ('Exactitud:', precision_score(y_true, y_pred))
    print ('Exhaustividad:', recall_score(y_true, y_pred))
    print ('F1:', f1_score(y_true, y_pred))

    false_positive_rate, recall, thresholds = roc_curve(y_true, y_pred)
    roc_auc = auc(false_positive_rate, recall)

    print ('AUC:', auc(false_positive_rate, recall))

    plot(false_positive_rate, recall, 'b')
    plot([0, 1], [0, 1], 'r--')
    title('AUC = %0.2f' % roc_auc)
```

```Python
metricas_modelos(y_test, y_pred_test)

model = LogisticRegression().fit(x_train, y_train)
y_pred_train = model.predict(x_train)
y_pred_test = model.predict(x_test)

metricas_modelos(y_train, y_pred_train)
```

<img width="158" height="82" alt="image" src="https://github.com/user-attachments/assets/4f9e6de4-6ead-41ce-86ec-b9fcaec4b5c9" />

```Python
metricas_modelos(y_test, y_pred_test)
```
<img width="162" height="85" alt="image" src="https://github.com/user-attachments/assets/1b6441bc-afc9-4257-bea9-1cdbebd7f811" />

