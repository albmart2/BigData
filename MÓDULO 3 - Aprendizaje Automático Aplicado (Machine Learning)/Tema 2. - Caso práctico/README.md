# Caso práctico

## Se pide

Construir un modelo que estime la calidad de los vinos en función de propiedades físico-químicas. Para ello se han de utilizar los datos contenidos en el archivo "winequality-white.csv", disponible en esta sección.

En este archivo se puede consultar la evaluación efectuada por expertos en vino blanco y un conjunto de sus características, como la acidez y el pH.

## Solución

Para llevar a cabo el análisis, lo primero que hay que hacer es cargar los datos del archivo CSV con Pandas. En el conjunto de datos importado se encuentran juntas la variable dependiente y las independientes, por lo que es necesario separarlas en dos conjuntos: el primero, con las variables independientes, y el segundo, con la variable dependiente.

Una vez separadas las variables independientes y la dependiente, se ha de crear un conjunto de entrenamiento y test utilizando la función <i>train_test_split</i>, la cual es necesaria para identificar la existencia del posible sobreajuste en el modelo. Una vez que se ha hecho esto, se puede crear el modelo y comprobar los resultados obtenidos en ambos conjuntos de datos.

```Python
%pylab
%matplotlib inline

%config InlineBackend.figure_format = 'retina'
```

```Python
import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split

wine = pd.read_csv('winequality-white.csv', sep = ';')

# Separación de la variable objetivo y las explicativas
target = 'quality'
features = list(wine.columns)
features.remove('quality')

x = wine[features]
y = wine[target]

x_train, x_test, y_train, y_test = train_test_split(x, y)

# Creación de un modelo
model = LinearRegression()
model.fit(x_train, y_train)

predit_train = model.predict(x_train)
predit_test = model.predict(x_test)

# Evaluación de R2
print('R2 en entrenamiento es: ', model.score(x_train, y_train))
print('R2 en validación es: ', model.score(x_test, y_test))
```

<img width="472" height="24" alt="image" src="https://github.com/user-attachments/assets/6b68c8c4-0e91-466a-94d7-ec69c05274e0" />

Los resultados obtenidos son un R2 de 0,278 en entrenamiento y 0,286 en validación. Esto indica que posiblemente exista sobreajuste en el conjunto, por lo que es necesario revisar las características utilizadas. Los procedimientos para la selección de variables se verán en unidades posteriores.
