# Caso práctico
## Enunciado
Una compañía internacional de alquiler de vehículos necesita una solución de inteligencia de negocio como soporte para la toma decisiones estratégicas. Dicha compañía tiene presencia en tres países y una flota de vehículos: turismos, gran tonelaje y furgonetas.

El objetivo de la compañía es poder analizar las ventas (rentings) y su evolución histórica por zonas geográficas, para poder redistribuir su flota en función de la demanda y optimizar con ello su ratio de uso. Para ello, se dispone de las bases de datos operacionales de ventas y flotas de cada país.

## Se pide
Basándose en un sistema de inteligencia de negocio tradicional, explicar y representar gráficamente la arquitectura de solución que implementar, diferenciando herramientas o elementos para usar en <i>back-end</i> y <i>front-end</i> y teniendo en cuenta que las necesidades de la dirección de la compañía son:

- Monitorizar el estado de varios indicadores clave.
- Enviar informes detallados a cada una de las sedes de forma periódica.
- Facilitar la exploración y análisis de los datos corporativos y su posible dependencia con factores externos.

## Solución

Tal y como solicita el enunciado, hay que plantear una arquitectura de solución de inteligencia de negocio tradicional, basada en tres capas: capa de datos, de aplicación y de presentación.

Del mismo modo, el enunciado exige identificar los elementos o herramientas de la solución que conforman el <i>back-end</i> y el <i>front-end</i>.

**a. Recuérdese que en el <i>back-end</i> se identifican:**

- Fuentes de datos: los distintos orígenes de información que se deben incluir para realizar los análisis requeridos. En este caso, y con la información del enunciado, al menos, se han de identificar diez fuentes de datos:
    - Sede 1:
        - Base de datos Ventas1.
        - Base de datos de Flota1.
        - Información de Sede1 georreferenciada.
    - Sede 2:
        - Base de datos Ventas2.
        - Base de datos de Flota2.
        - Información de Sede2 georreferenciada.
    - Sede 3:
        - Base de datos Ventas3.
        - Base de datos de Flota3.
        - Información de Sede3 georreferenciada.
    - Fuente externa: análisis de posible dependencia con información climatológica.
- Procesos ETL: procesos para la extracción de los datos de los distintos orígenes, transformación para unificar, homogeneizar y consolidar la información en un mismo repositorio.
- <i>Data warehouse/datamart</i>: como repositorio destino de toda la información y que estará especialmente diseñado para contestar ciertas preguntas del negocio.
- Motor OLAP: especialmente indicado para proporcionar capacidad analítica sobre el almacén de datos.

**b. En el <i>front-end</i>:**

El propio enunciado indica qué elementos se necesitarán para la capa de explotación de la información:

- Mediante la implementación de un cuadro de mando para la dirección, se puede mantener el control y gestión de los indicadores clave KPI definidos.
- Los usuarios también demandan una capa de reporting que les permita realizar informes de un nivel de detalle alto y que la generación de información pueda ser automatizada de forma periódica y con exportación por correo electrónico.
- Por último, el enunciado indica la necesidad de explorar la información para su análisis. Como ya se sabe, esto hace referencia a los visores OLAP, herramientas especialmente diseñadas para facilitar de forma ágil y eficiente el análisis y navegación a través de la información, con procesamiento analítico online.
