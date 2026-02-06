# Caso práctico
## Se pide

Utilizar la clase RadiusNeighborsClassifier para crear un clasificador que permita identificar la especie del conjunto de datos Iris en base al largo y al ancho de los sépalos. Probar el funcionamiento con los radios de 0,3; 0,5; 0,7; 0,9 y 1,1.

## Solución

A la hora de utilizar el algoritmo indicado en el enunciado, se ha de tener en cuenta que, además de las tres categorías, se puede obtener un valor indeterminado cuando no existe ningún registro en el radio indicado. En estos puntos se ha de utilizar un color diferente. Para ello se puede añadir un nuevo color a <i>cmap_light</i>, que puede ser un gris como, por ‘#AAAAAA’.

Para la carga de los datos se pueden utilizar las mismas líneas de código empleadas anteriormente. 

Ahora se ha de importar <i>RadiusNeighborsClassifier</i> y asignar un valor a los outliers. Como hay tres valores en el conjunto de datos se le puede asignar el 3, ya que 0,1 y 2 son los utilizados en las categorías para el primer radio.

```Python
from sklearn.neighbords import RadiusNeighborsClassifier

knn = RadiusNeighborsClassifier (0.3, outlier_label = 3)
knn.fit (X,y)
```

Esto da lugar a una gráfica como la que se muestra en la imagen, en la que se puede observar que las fronteras son más irregulares que en el caso anterior, además de que en la mayoría del plano no hay solución.

### Código general

```Python
%pylab
%matplotlib inline

%config InlineBackend.figure_format = 'retina'
```

```Python
from sklearn.datasets import load_iris

iris = load_iris()

# Se utilizan la primera y segunda columna con el largo y ancho de los sépalos  
X = iris.data[:, 0:2]
y = iris.target
```

```Python
from sklearn.neighbors import RadiusNeighborsClassifier

knn = RadiusNeighborsClassifier(0.3, outlier_label = 3)
knn.fit(X, y)
```

```Python
from matplotlib.colors import ListedColormap

# Version clara y oscura de los coloes
cmap_light = ListedColormap(['#FFAAAA', '#AAFFAA', '#AAAAFF', '#AAAAAA'])
cmap_bold = ListedColormap(['#FF0000', '#00FF00', '#0000FF'])

# Creación de un conjunto de datos para 
x_min, x_max = X[:, 0].min() - 1, X[:, 0].max() + 1
y_min, y_max = X[:, 1].min() - 1, X[:, 1].max() + 1

xx, yy = np.meshgrid(np.arange(x_min, x_max, 0.05),
                     np.arange(y_min, y_max, 0.05))

Z = knn.predict(np.c_[xx.ravel(), yy.ravel()])
Z = Z.reshape(xx.shape)

pcolormesh(xx, yy, Z, cmap = cmap_light)
scatter(X[:, 0], X[:, 1], c=y, cmap = cmap_bold)
xlim(xx.min(), xx.max())
ylim(yy.min(), yy.max())
```

```Python
import matplotlib.pyplot as plt
def modelRadius(X, y, r):
    # Creación del modelo
    knn = RadiusNeighborsClassifier(r, outlier_label = 2)
    knn.fit(X, y)

    # Version clara y oscura de los coloes
    cmap_light = ListedColormap(['#FFAAAA', '#AAFFAA', '#AAAAFF', '#AAAAAA'])
    cmap_bold = ListedColormap(['#FF0000', '#00FF00', '#0000FF'])

    # Creación de un conjunto de datos para 
    x_min, x_max = X[:, 0].min() - 1, X[:, 0].max() + 1
    y_min, y_max = X[:, 1].min() - 1, X[:, 1].max() + 1

    xx, yy = np.meshgrid(np.arange(x_min, x_max, 0.05),
                         np.arange(y_min, y_max, 0.05))

    Z = knn.predict(np.c_[xx.ravel(), yy.ravel()])
    Z = Z.reshape(xx.shape)

    plt.pcolormesh(xx, yy, Z, cmap = cmap_light)
    plt.scatter(X[:, 0], X[:, 1], c=y, cmap = cmap_bold)
    plt.xlim(xx.min(), xx.max())
    plt.ylim(yy.min(), yy.max())
    plt.show()
```

El resto de las figuras se puede obtener repitiendo este proceso con diferentes valores para el radio.

### Gráficas
```Python
modelRadius(X, y, 0.5)
```

<img width="329" height="250" alt="image" src="https://github.com/user-attachments/assets/8b128a3e-2f92-436f-8f1c-5726e5ca02ef" />

```Python
modelRadius(X, y, 0.7)
```

<img width="331" height="244" alt="image" src="https://github.com/user-attachments/assets/f929a591-81f7-4e43-a6a3-e2e019f0a83c" />

```Python
modelRadius(X, y, 0.9)
```

<img width="335" height="245" alt="image" src="https://github.com/user-attachments/assets/bea13c9d-7774-4f89-81fd-fb84d2c517de" />

```Python
modelRadius(X, y, 1.1)
```

<img width="329" height="249" alt="image" src="https://github.com/user-attachments/assets/0142d2df-360b-41cf-814e-569227aab1df" />
