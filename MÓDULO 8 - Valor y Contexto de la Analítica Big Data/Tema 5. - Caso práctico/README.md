# Caso práctico con solución

## Enunciado

Spain Bike, S. A. es una empresa española que se dedica a la venta de bicicletas de montaña por internet, con la peculiaridad de que no dispone de almacén para el stock. Todo el proceso lo hacen directamente con el proveedor y, por ello, necesitan crear un sistema informático que gestione sus pedidos por internet. La empresa depende mucho, en consecuencia, de tener un sistema de pedidos y transacciones sano, capaz de sincronizarse de forma eficiente con los proveedores. Esto les permite gestionar de forma adecuada cada una de las peticiones de bicicletas nuevas que los clientes puedan hacer online.

Tras un par de reuniones iniciales de los responsables de la cuenta con el CEO de Spain Bike, estos nos han transmitido la preocupación del CEO por tener una aplicación que permita una gestión eficiente del producto, pues no quieren fallos en la tramitación de pedidos entre los clientes y los proveedores.

También nos han hecho llegar la necesidad del director general de implementar informes analíticos sobre la gestión de stock, un sistema de reportes que les permita comprender mejor cómo evoluciona el stock y poder predecir la futura demanda para obtener descuentos en los proveedores y tener un margen mayor en el precio final.

Por otro lado, parece que también tienen la idea de proporcionar a sus clientes imágenes y especificaciones técnicas para navegar con una experiencia de usuario óptima cuando estén buscando un producto en su página.

Tras haber mostrado al CEO la propuesta de requisitos que los gestores de la cuenta le han planteado, nos ha transmitido su satisfacción para llevar a cabo el proyecto. Está un poco preocupado por el precio final del producto y nos ha pedido que le pasemos una estimación y unos presupuestos para ver si cuadran con la idea que tiene en mente.

Asimismo, en nuestra empresa de desarrollo informático ha quedado libre un grupo de desarrolladores de cuatro personas con experiencia en Scrum, que se pueden utilizar para trabajar con este cliente, y el equipo de recursos humanos nos ha hecho llegar dos personas recién tituladas sin experiencia alguna.

Los costes asociados a estos roles son los siguientes:
- Scrum master: 22 €/hora.
- Arquitecto técnico: 40 €/hora.
- Programadores experimentados: 30 €/hora.
- Programadores noveles: 10 €/hora.

El equipo experimentado ha trabajado siempre haciendo sprints de tres semanas.

## Se pide

Partiendo de estos hechos, y sabiendo que nos han nombrado responsables de llevar a cabo este
proyecto siguiendo la metodología Scrum, se solicita lo siguiente:
Describir los pasos para planificar el proyecto, así como calcular el tiempo y los costes asociados a la implementación del proyecto.
<ol type="a">
  <li>Identificar al product owner.</li>
  <li>Formalizar los requisitos del sistema.</li>
  <li>Definir el backlog (a nivel ejecutivo).</li>
  <li>Calcular la estimación inicial de la velocidad del equipo.</li>
  <li>Estimar el tiempo necesario para la entrega del product backlog.</li>
  <li>Calcular el coste final del proyecto.</li>
</ol>

## Solución

**Se busca un product owner adecuado dentro de la organización:**

Lo primero que se ha de hacer como responsables del proyecto es buscar en la empresa Spain Bikes SA a la persona que vaya a ejercer el rol de product owner. Probablemente el CEO pueda aportar información sobre quién puede ser, pero lo mejor es comprender cómo funciona internamente la empresa con el conocimiento que seguro tiene el responsable de la cuenta.

Hay que buscar a aquella persona que tenga el poder político suficiente para poder manejar al CEO, el conocimiento adecuado del negocio para comprender las prioridades en el producto y la cercanía necesaria para facilitar el contacto con los usuarios en los momentos adecuados del desarrollo.

Es muy importante hacerse con la persona adecuada, que se vea responsable del producto, que el CEO le conceda el poder de decisión suficiente para ser completamente independiente y que conozca el negocio y a sus gentes en profundidad para poder orientar el producto al máximo beneficio para el negocio.

**Se formalizan los requisitos del sistema:**
Al leer el enunciado del problema, las necesidades que tiene el CEO de la empresa parecen bastante obvias:
- Sistema de altas, bajas y modificaciones de pedidos.
- Integración directa con los proveedores.
- Sistema de informes y consulta de datos.
- Cálculo analítico sobre los datos históricos.
- Mejora de la página web para los usuarios que navegan por ella.

Esta primera iteración proporcionada por el responsable de la cuenta puede servir de guía, pero nunca debe ser la representación formal de las historias de usuario del proyecto. Los detalles están a muy alto nivel. Representan más las épicas del producto que las propias historias de usuario.

Es necesario profundizar mucho más en todas ellas y desgranarlas para comprender perfectamente cuáles son las tareas que desempeñar en cada una de ellas. No hay por qué bajar al detalle para la propuesta inicial, pero sí pensar en riesgos y problemas que se pueden encontrar por la falta de conocimiento sobre el negocio de un cliente en el que se acaba de aterrizar.

Por ello, la primera relación con la empresa como responsables deberá ser con el product owner y con el equipo mediante una reunión de planificación y estimación Scrum. Se ha de iterar sobre cada una de las ideas proporcionadas por el CEO, profundizar en su contenido hasta donde sea posible, comprendiendo siempre que nunca se tendrá el conocimiento suficiente para detallar plenamente cada una de ellas en esta primera etapa del proyecto.

Durante la reunión de planificación, los roles de product owner, equipo de desarrollo Scrum y Scrum master trabajarán sobre las ideas proporcionadas por el CEO y formalizarán un product backlog que profundizará hasta que se tengan historias de usuario comprensibles, que puedan tener un tamaño limitado con una estimación más o menos razonable.

Al finalizar la reunión de planificación, el product owner debería tener una tabla como la mostrada a continuación:

<img width="976" height="1223" alt="image" src="https://github.com/user-attachments/assets/5e4b2bac-f5fe-4b8f-a546-5b3beeee0260" />

En esta tabla, se muestra lo siguiente:
1. El ID de la historia de usuario.
2. La descripción de la historia de usuario.
3. El tema de la historia de usuario: en el ejemplo mostrado se ha desglosado la épica del sistema de altas, bajas y modificaciones solicitadas por el CEO de la empresa.
4. Prioridad (MoSCoW): prioridad otorgada por el product owner a cada una de las historias de usuario.
5. Metadatos: información adicional necesaria que las describa.
6. Los puntos por historia que el equipo ha otorgado a cada una de ellas tras haber llevado a cabo la planning poker durante la reunión.

La tabla no tiene que limitar su contenido únicamente a historias de usuario que representen requisitos del CEO. Hay que agregar en ella cualquier otra necesidad que pueda surgir durante la implementación del producto solicitado:

1. **Riesgos.** Problemas que es posible encontrar, pero que aún no son impedimentos reales: el coste de los servidores en cloud puede ser elevado, la integración con los proveedores puede no ser estándar, la base de datos MongoDB puede no escalar como se desea, etc.
2. **Impedimentos.** Bloqueos que se sabe que existen actualmente y que no es posible evitar. Pueden ser ordenadores sin potencia, falta de licencias de software, necesidad de cursos para los desarrolladores, etc.

**Definición ejecutiva del product backlog:**

El product backlog generado durante las reuniones de planificación y estimación suele estar a bajo nivel.

Los CEO y directivos de las empresas no suelen estar interesados en tanto detalle. Generalmente, buscan un nivel superior de abstracción que les permita ver cuál es la planificación general del proyecto y el esfuerzo que este pueda llevar.

Es tarea del product owner agrupar las historias de usuario en épicas y agregar en una única tabla las historias de usuario necesarias y sus puntos por historia asociados para dar una información de más alto nivel a este tipo de cargos en la empresa. En el ejemplo, el CEO solicitaba implementar el proyecto en dos olas:
- Una básica, con el producto mínimo necesario para ejecutar el negocio con éxito.
- Otra posterior, que mejore el producto mínimo y proporcione capacidades de reporting y analíticas.

Con ello, se podría configurar una **tabla de épicas** similar a la siguiente:

<img width="702" height="285" alt="image" src="https://github.com/user-attachments/assets/e9ecbf2f-e338-4226-af57-9d90b4cdf7aa" />

En este nivel, es posible agregar también todos los riesgos e impedimentos identificados durante la planificación y estimación del proyecto con el equipo de Scrum y el product owner. Esta vista será la base para formalizar el resto de las medidas que se vayan a compartir en la estimación final que se suministre al CEO al presentar el proyecto.

**Se calcula la estimación inicial de la velocidad del equipo:**

El problema indica que se va a disponer de un equipo de seis personas en total, en el que cuatro tienen experiencia en proyectos anteriores y dos son recién titulados sin experiencia. Esta información suele estar disponible en empresas de desarrollo medianamente maduras y resulta clave para comprender la velocidad de desarrollo del futuro equipo:

1. Del equipo con experiencia en Scrum, se puede deducir fácilmente su velocidad de entrega por sprint. Si han trabajado juntos en proyectos anteriores, esta velocidad estará basada en hechos reales y puede ayudar mucho a la hora de la estimación final de proyecto que se va a hacer.
2. De las dos personas sin experiencia no se puede deducir tanto. Nunca se ha trabajado con ellas y no se sabe si serán inicialmente un freno a la velocidad del equipo experimentado. Por ello, hay que hacer uso de la velocidad de los primeros y de una velocidad menor en los segundos para estimar la futura velocidad de entrega del nuevo equipo.

Si la velocidad del equipo experimentado era de 32 puntos por sprint, se podría suponer que la velocidad de entrega de cada individuo es de siete puntos por sprint, aproximadamente. Con estos datos, sabiendo que los recién llegados tendrán una curva de aprendizaje inicial, es posible estimar una velocidad de dos puntos para ellos para el cálculo final de la velocidad del equipo:

<p align="center">
  Velocidad = 32 + 2 + 2 = 36 puntos por sprint.
</p>

**Se estima el coste total del equipo por horas:**

Sabiendo que el product owner pertenece al cliente y no imputará costes en nuestro lado y que se dispone de los siguientes miembros del equipo:
- Un Scrum master a un coste de 22 €/hora.
- Un arquitecto a un coste de 40 €/hora.
- Cuatro programadores experimentados a un coste de 30 €/ hora.
- Dos programadores noveles a un coste de 10 €/hora.

Se puede deducir la siguiente tabla de costes por hora:

<img width="654" height="189" alt="image" src="https://github.com/user-attachments/assets/3fc726c7-44f9-4118-8e4f-0fa3ab36379b" />

**Se estima ahora el tiempo necesario para el product backlog:**

Para calcular el tiempo que puede llevar la entrega del product backlog estimado, se han de tener en cuenta los siguientes factores:
1. Los puntos totales estimados por el equipo para cada ola: 95 y 115.
2. El número total de personas: seis. Se dividirán en dos equipos de tres personas cada uno para difuminar la falta de experiencia de los recién titulados y facilitarles la curva de aprendizaje al rodearlos de los más experimentados.
3. La velocidad de las seis personas, que se ha estimado anteriormente en 36 puntos por sprint.
4. La duración del sprint del equipo: tres semanas.

Con estos valores, el cálculo de tiempos quedaría de la siguiente manera:

<img width="619" height="132" alt="image" src="https://github.com/user-attachments/assets/9a260763-57cd-4a28-9812-3f8a3d3390a0" />

Cada ola del proyecto propuesta tiene un total de puntos por el que puede ser entregada en dos sprints si el equipo mantiene una velocidad de entrega de 36 puntos por sprint. Con sprints de tres semanas, se necesitaría un total de seis semanas de trabajo para cada ola. El CEO puede optar por hacer una de las olas o las dos, sabiendo que cada una de ellas llevará seis semanas de trabajo.

**Se calcula el coste final del proyecto:**
Se calcula, primero, cuánto cuesta cada miembro del equipo por hora:

|Miembro|€ · h|
|-------|-----|
|Scrum Master|22 × 0,33 = 7,26 €/hora|
|Arquitecto|40 × 0,33 = 13 €/hora|
|Desarrollador con exp.|30 × 4 = 120 €/hora|
|Desarrollador novel|10 × 2 = 20 €/hora|

Ahora, se calcula el total del equipo por hora: 

<p align="center">
  7,26 € + 13 € + 120 € + 20 € = 161 €/hora
</p>

Sabiendo que cada ola llevará seis semanas de trabajo:

<p align="center">
  40 horas/semana × 6 = 240 horas/ola
</p>

Se puede calcular que el total del coste por ola será el siguiente:

<p align="center">
  240 horas/ola × 161 €/hora = 38 640 €/ola
</p>

Llegados a este punto, el cliente tendrá la información necesaria para poder tomar las decisiones pertinentes sobre la duración del proyecto que desea (una ola o las dos) y comprender cuál será su coste asociado.
