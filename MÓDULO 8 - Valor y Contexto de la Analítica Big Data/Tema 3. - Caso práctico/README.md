# Caso práctico con solución

## Enunciado

Este caso está extraído del libro *Big Data in Practice*, de Bernard Marr (John Wiley & Sons, 2016). Los estudiantes deberán leer el siguiente extracto y reflexionar acerca de los conceptos más importantes.

“Facebook se ha convertido en uno de los repositorios de datos personales más grandes del mundo, con una gama cada vez mayor de usos potenciales. Por eso, la monetización de datos en la red social se ha convertido en primordial. Puede, por un lado, comercializar estos datos colectivamente para proporcionar análisis predictivos, por ejemplo, del comportamiento del comprador. Dado que los datos son consolidados y anónimos, el sistema no plantea ningún problema importante de privacidad de datos.

Las empresas necesitan vender productos y servicios para sobrevivir. Para hacer esto, necesitan encontrar clientes para vender. Tradicionalmente, esto se ha hecho publicitando de forma ‘televisiva’: los periódicos, la televisión, la radio y la publicidad visual funcionan con el principio de que si coloca su anuncio en el lugar más destacado puede permitirse que un gran número de personas lo vea y algunos de ellos probablemente estén interesados en lo que está ofreciendo.

Sin embargo, esto es obviamente un enfoque de prueba y error. Para una gran compañía multinacional, puede estar claro que un anuncio durante un gran evento televisivo aumentará su exposición y pondrá su marca frente a los clientes potenciales. Pero una pequeña empresa que acaba de comenzar tiene que pensar mucho más cuidadosamente sobre la manera más eficiente de gastar su presupuesto de marketing limitado. Estas empresas no pueden darse el lujo de cubrir todas las bases, por lo que las herramientas que pueden ayudarlas a determinar quiénes son sus clientes y dónde encontrarlos pueden ser sumamente beneficiosas.

La rápida expansión del mundo digital en las últimas dos décadas ha proporcionado a los anunciantes una forma sencilla de hacerlo. Debido a que los sitios web están alojados en computadoras, no en periódicos o vallas publicitarias, cada visitante puede ser identificado independientemente por el software que ejecuta el sitio web. Y Facebook, con 2700 millones de usuarios mensuales activos, tiene acceso a muchos más datos de usuario que cualquier otra persona.

Sus datos también son más personales. Mientras que los servicios como Google pueden rastrear nuestras visitas a las páginas web (cosa que, por cierto, Facebook también puede hacer) e inferir mucho sobre nosotros a partir de nuestros hábitos de navegación, Facebook a menudo tiene acceso completo a datos demográficos directos sobre nosotros, como dónde vivimos, trabajamos, jugamos, cuántos amigos tenemos, qué hacemos en nuestro tiempo libre y las películas, libros y músicos que nos gustan en particular.

Un editor de libros, por ejemplo, puede pagar a Facebook para que coloque sus anuncios frente a un millón de personas a las que les gustan libros similares, y que coincidan con los perfiles demográficos de sus clientes.

Los datos recopilados por los usuarios mientras navegan en Facebook se utilizan para unirlos con empresas que ofrecen productos y servicios que, estadísticamente, probablemente les interesen. Facebook, sin duda, posee una de las bases de datos personales más grandes y completas jamás recopiladas, y se está expandiendo cada segundo de cada día.

Además de una plataforma para compartir mensajes, Facebook también es una plataforma para ejecutar software. Hasta ahora, se han creado más de medio millón de aplicaciones para Facebook, la mayoría de las cuales aprovechan la ventaja del acceso que tienen, a través de las amplias API (interfaces de programas de aplicaciones), a los datos de los usuarios de Facebook. Estas aplicaciones, a su vez, recopilan datos sobre cómo se utilizan que sus desarrolladores usan para orientar los anuncios a sus propios clientes. Facebook también se expande al comprar otras compañías y servicios y agregar sus datos a los suyos.

En los últimos años, la compañía ha adquirido los servicios de Instagram y WhatsApp, poniendo más datos sobre cómo compartimos imágenes y mensajes instantáneos a su disposición. Más intrigante, también adquirieron los fabricantes de auriculares de realidad virtual Oculus. Algunos comentaristas han dicho que esto muestra que Facebook está interesado en desarrollar servicios para permitirnos interactuar entre nosotros en realidad virtual, en lugar de simplemente en pantallas planas. Controlar nuestro comportamiento en estos mundos virtuales nuevos e inmersivos será, sin duda, una fuente muy valiosa de nuevos datos en el futuro cercano.

En línea con la mayoría de los grandes proveedores de servicios en línea, el mayor desafío de Facebook ha ido ganando nuestra confianza. Al principio, no era inusual encontrar personas que fueran muy escépticas a proporcionar detalles personales en cualquier sistema en línea, ya que era imposible saber con certeza qué se haría con ellos. Incluso si todas las empresas del mundo respetan estrictamente los términos de sus políticas de privacidad y uso compartido de datos, las políticas más impermeables en el mundo son impotentes ante la pérdida de datos o el robo, como los ataques de piratería.

Desde el comienzo, Facebook intentó ganar nuestra confianza mostrándonos que se tomaron en serio la privacidad. Tan llenas de agujeros y referencias a “terceros” misteriosos y no especificados como pudieron haber sido, sus características de privacidad estuvieron a años luz por encima de los ofrecidos por sus contemporáneos, como Myspace.

El hecho de que hubiera al menos una ilusión de privacidad fue suficiente para atraer a muchas personas a bordo de la revolución de las redes sociales. De forma predeterminada, todo lo que compartía un usuario se compartía solo con un grupo de amigos de confianza, a diferencia de Myspace, donde inicialmente las publicaciones se compartían de forma predeterminada con el mundo. También ofreció interruptores que permiten que los aspectos individuales de los datos de una persona se hagan públicos o privados. Sin embargo, siempre ha habido quejas de que estas opciones son confusas o difíciles de encontrar”.7
_______________________________________
7 Marr, B. *Big Data in Practice*. John Wiley & Sons; 2016.

## Se pide

1. Existe un dicho en el ámbito de big data y analytics que indica: “Cuando el servicio es gratuito, el producto somos nosotros”. Este término se refiere a que cuando el uso de un servicio no conlleva un coste, la monetización habitualmente viene propiciada por la venta de los datos, de forma directa o indirecta, que genera la actividad de los usuarios con el servicio. En el caso de Facebook, se pide enumerar los potenciales usos que pueden darse a la información disponible en la red social.
2. En la actualidad, está aumentando la controversia dentro del ámbito del uso de información de usuarios como medio de monetización y venta a terceros. ¿Qué elementos crees que son limitantes a la hora de explotar la información de comportamiento en una plataforma como Facebook?
3. Para su plataforma de anuncios, analiza el caso de uso y los potenciales beneficios que aporta a Facebook la creación de esta plataforma. ¿Lo consideras un movimiento acertado?

## Solución

1. **Existe un dicho en el ámbito de *big data* y *analytics* que indica: “Cuando el servicio es gratuito, el producto somos nosotros”. Este término se refiere a que cuando el uso de un servicio no conlleva un coste, la monetización habitualmente viene propiciada por la venta de los datos, de forma directa o indirecta, que genera la actividad de los usuarios con el servicio. En el caso de Facebook, se pide enumerar los potenciales usos que pueden darse a la información disponible en la red social.**

    Cuando una compañía no cobra de forma directa por su producto o servicio, es necesario buscar nuevas formas de monetizar sus activos. En el caso de empresas basadas en los datos, esos activos son los datos, y, por tanto, el objetivo es monetizar o vender de forma directa o indirecta la información extraída. De esta forma, algunos de los potenciales uso de los datos son los siguientes:
    - Encuestas de opinión. En Facebook se vuelcan todos nuestros gustos, opiniones e intereses. De forma segmentada y anonimizada, son una fuente muy interesante para realizar estudios de mercado. Es importante tener en cuenta el alto número de noticias falsas que se propagan por la red, por lo tanto, es necesario siempre validar que las opiniones son reales.
    - Comportamiento e intereses. La información agregada por área o zona de interés, donde se puedan ver tendencias de moda, opinión de lugares públicos/privados, o, sencillamente, hábitos sociales, ayuda a las empresas a mejorar sus servicios.
    - Publicidad. Facebook es un canal de consumo de información. Es, por tanto, un canal óptimo para vender espacios publicitarios a diferentes agentes que quieran introducir su publicidad y cobrar por ese espacio.
    - Segmentación. En el ámbito de la publicidad, Facebook no solo ofrece esos espacios publicitarios, sino una plataforma completa para segmentar y microsegmentar los públicos objetivo de las campañas y asegurar que los usuarios que reciben la publicidad son aquellos que tienen el perfil exacto generado. Cuanta más información se utiliza para segmentar, mayor coste tiene para el agente publicitario cada anuncio mostrado.

2. **En la actualidad, está aumentando la controversia dentro del ámbito del uso de información de usuarios como medio de monetización y venta a terceros. ¿Qué elementos crees que son limitantes a la hora de explotar la información de comportamiento en una plataforma como Facebook?**

    Actualmente, el derecho al uso de la información generada ha entrado en controversia con la privacidad de los usuarios. Sin entrar en un debate sobre el GDPR, es importante resaltar que la nueva ley de protección de datos marca algunos puntos clave:
    - Consentimiento. El consentimiento expreso de los usuarios es necesario para usar la información en campañas publicitarias o de marketing.
    - Derecho al borrado. Los usuarios tienen derecho a que se borre toda la información disponible en los sistemas.
    - Derecho de obtención de datos. Los usuarios tienen derecho a obtener todos los datos que la plataforma tenga recopilados sobre ellos.

    Como se comentaba, aparte de la ley de protección de datos, es muy importante que todo uso de la información sea anonimizado y agregado. Vender datos personales debería estar fuera de la mente de cualquier empresa. El agregado, anonimización y venta de información de tendencias es una línea que, si no se usa para fines comerciales y de contacto con el usuario, no debe dar problemas, mientras que la venta de información con un fin comercial sí ha de estar reglada y recibir el consentimiento expreso.

    Esto no hace que, en caso de una petición de borrado, esos datos no puedan ser utilizados siquiera para análisis estadísticos.

3. **Para su plataforma de anuncios, analiza el caso de uso y los potenciales beneficios que aporta a Facebook la creación de esta plataforma. ¿Lo consideras un movimiento acertado?**

La creación de la plataforma de venta de anuncios programática ha sido uno de los movimientos más acertados de Facebook. Facebook no vende solamente datos, sino que ha puesto a disposición de anunciantes y propietarios de espacios publicitarios una plataforma que cambia el modelo de ingresos de valor por cantidad, es decir, el valor del espacio publicitario varía en función del número de usuarios que lo ven, al valor por la calidad, es decir, se vende la capacidad de tener perfiles cualificados, según la información que Facebook recolecta de cada usuario. Con ello, los anunciantes pueden perfilar su público objetivo y crear microsegmentos de nicho para ajustar la publicidad a estos microsegmentos, obteniendo un mejor y mayor retorno de su inversión en publicidad, mientras que Facebook recibe una línea de ingresos enorme, por disponer de los espacios publicitarios dentro de Facebook.

