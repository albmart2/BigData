# Caso práctico

## Se pide

En el archivo “<i>mammals.csv</i>”, disponible a continuación, se encuentra una lista de mamíferos con los componentes de su leche.

A partir de esta información, segmentar los mamíferos sobre la base de los componentes de las leches y obtener los valores promedio para cada grupo de animales.

## Solución

Lo primero que se ha de hacer es importar el archivo con los datos, por lo que se han de utilizar pandas. Para importar los datos se puede utilizar el comando:

```Bash
mammals = pd.read_csv('mammals.csv', sep = ',')
```
Al cargar el conjunto de datos se aprecia que existen seis variables: el nombre del animal, el agua, la proteína, la grasa, la lactosa y la ceniza. Solamente las cinco últimas variables son numéricas, por lo que son las únicas que se utilizarán para realizar la segmentación.

Para identificar el número de clústeres en los que se divide la leche de los mamíferos, se utilizará el método de la silueta. Para ello se puede emplear el código para la gráfica silhouette estudiado en la unidad:

```Python
%pylab
%matplotlib inline

%config InlineBackend.figure_format = 'retina'
```

```Python
import pandas as pd

mammals = pd.read_csv('mammals.csv', sep = ',')
mammals.head()
```

<img width="202" height="114" alt="image" src="https://github.com/user-attachments/assets/db36e804-ffc9-4ba8-a724-6e3c9ae8dfaf" />

```Python
col_names = list(mammals.columns)
col_names.remove('name')

mammals_data = mammals[col_names]
```

```Python
from sklearn.cluster import KMeans
from sklearn.metrics import silhouette_score
from scipy.spatial.distance import cdist
from threadpoolctl import threadpool_limits

def plot_sillhouette(blobs, figure_name, max_k=10, n_init=10):
    sillhouette_avgs = []

    for k in range(2, max_k):
        with threadpool_limits(limits=1):
            kmean = KMeans(n_clusters=k, n_init=n_init).fit(blobs)
        sillhouette_avgs.append(silhouette_score(blobs, kmean.labels_))

    plt.figure()
    plt.plot(range(2, max_k), sillhouette_avgs)
    plt.title(figure_name)
    plt.xlabel("Número de clusters (k)")
    plt.ylabel("Silhouette score")
    plt.show()
    
plot_sillhouette(mammals_data, 'Mammals')
```

<img width="232" height="181" alt="image" src="https://github.com/user-attachments/assets/feb4ca75-7120-4f54-a320-172449e71062" />

```Python
kmeans = KMeans(n_clusters = 3, n_init = 10).fit(mammals_data)
kmeans.cluster_centers_
```

<img width="328" height="36" alt="image" src="https://github.com/user-attachments/assets/c3d42406-c3b5-44a1-b9f5-2821e17595de" />

```Python
clust = kmeans.predict(mammals_data)

for i in range(max(clust) + 1):
    print ("Cluster", i)
    print (mammals["name"][clust == 0])
```

<img width="94" height="370" alt="image" src="https://github.com/user-attachments/assets/887367b3-4204-465d-884c-9d6001e8b529" />
