# Caso práctico con solución
## Enunciado

Se desea diseñar una aplicación que implemente un buscador de ofertas de trabajo. Cada usuario puede configurar qué portales de ofertas de empleo servirán de fuente para recuperar las ofertas y las características de las ofertas que deben recuperarse.

La aplicación se conectará a los portales de empleo y generará entradas asociadas a cada usuario.

Una entrada será esencialmente el nombre del portal web donde se ha encontrado la oferta, el contenido principal de la oferta, las características que cumple la oferta, con respecto a los requisitos impuestos por el usuario, y un enlace a esta (la aplicación guardará una copia de la oferta para asegurarse de que no sea eliminada del portal de empleo), de forma que, si el usuario desea consultar la oferta completa, puede pulsar sobre el enlace. Obsérvese que las entidades que deberán gestionarse, en cuanto al número de portales de empleo, requisitos de búsqueda, ofertas y usuarios, van a ser enormes.

## Se pide

Realizar un análisis acerca del modelo de datos y la arquitectura de distribución y replicación de los datos más adecuados para los requisitos de la aplicación descrita. En el caso del modelo de datos, se pide discutir la conveniencia de un modelo relacional o uno NoSQL, y, en este último caso, qué modelo sería el más adecuado.

## Solución

### 1. Modelo de datos
 
El modelo de datos **no debería ser relacional**, por las siguientes razones:
 
- El sistema requiere gestionar una **cantidad enorme de datos**.
- Debe soportar una **elevada concurrencia** de acceso por muchos usuarios simultáneos.
- Esta situación hace recomendable una **fragmentación horizontal** de los datos.
La mejor opción es una **base de datos NoSQL**, que ofrece:
 
- Facilidad para la fragmentación horizontal.
- **Alta disponibilidad**.
- Soporte de elevados niveles de concurrencia.
#### Tipo de modelo NoSQL recomendado
 
De entre los posibles modelos NoSQL, encajan mejor los siguientes:
 
- **Clave-valor**
- **Orientado a documentos**
- **Orientado a columnas**
> ❌ Un modelo **orientado a grafos no sería adecuado**, ya que en el sistema propuesto apenas existen relaciones entre entidades.
 
---
 
### 2. Distribución de los datos
 
La mejor estrategia de distribución es **fragmentar los datos en función de la ubicación geográfica** de los usuarios registrados. Esto se justifica porque:
 
- Los usuarios normalmente buscan ofertas en portales de sus propios países o regiones.
- Se **maximiza la localidad de los datos** y se asegura un acceso rápido.
La fragmentación horizontal aplicada cumplirá las propiedades de:
 
- **Completitud**: todos los datos pertenecen a alguna partición.
- **Reconstrucción**: la unión de todas las particiones reconstruye el conjunto de datos completo.
#### Criterios adicionales de distribución
 
- Las regiones con **pocos usuarios registrados** se almacenarán en el mismo nodo para evitar nodos desequilibrados.
- Se realizarán **redistribuciones de la fragmentación** cuando cambien significativamente el número de usuarios en las diferentes particiones, con el objetivo de mantener cargas de trabajo equilibradas.
---
 
### 3. Replicación de los datos
 
- Se realizará **al menos una réplica** para asegurar el servicio ante la caída de un nodo.
- Las réplicas se almacenarán en los **nodos geográficamente más cercanos**, aprovechando la arquitectura de distribución basada en localización, minimizando así el tiempo de acceso.
- Se utilizará un modelo de **replicación maestro-esclavo**, ya que permite garantizar un **alto rendimiento** cuando hay un elevado número de peticiones a la base de datos.
---
 
## Resumen de decisiones
 
| Aspecto | Decisión |
|---|---|
| Modelo de datos | NoSQL (no relacional) |
| Tipo de NoSQL | Clave-valor, documentos u orientado a columnas |
| Estrategia de distribución | Fragmentación horizontal por localización geográfica |
| Replicación | Mínimo 1 réplica, en nodos geográficamente cercanos |
| Modelo de replicación | Maestro-esclavo |
