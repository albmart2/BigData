# Caso práctico con solución
## ENUNCIADO

Se reproduce a continuación un artículo de la página web Inside Big Data, [“The Exponential Growth of Data”](insidebigdata.com), del 16 de febrero de 2017, referente al crecimiento de datos y su impacto en las tecnologías big data.

**El uso inteligente del big data a escala industrial.**

Hace varias décadas, el ministro de energía de Arabia Saudita, Sheikh Yamani, fue reconocido por su visión del desarrollo global: "La Edad de Piedra no terminó por falta de piedra, y la Edad del Petróleo terminará mucho antes de que el mundo se quede sin petróleo". Hoy vivimos en lo que muchos llaman la era de la información y no corremos ningún peligro de quedarnos sin información, especialmente en forma de datos. Existe una percepción generalizada de que estamos abrumados con datos, lo que hace que la capacidad de almacenar, procesar, analizar, interpretar, consumir y actuar sobre dichos datos sea una preocupación de primer orden. Para las organizaciones multinacionales a gran escala y en las industrias fuertemente reguladas, como pueden ser finanzas, salud o aquellas que cubren múltiples verticales de la industria, la situación se vuelve aún más compleja y desafiante. La creciente preocupación por los datos es rampante en la era del internet de las cosas (IoT), durante la cual el crecimiento de los datos supera la capacidad de la informática tradicional. La pregunta entonces es: ¿cómo consumimos esas fuentes de datos y las transformamos en información procesable?

**El crecimiento exponencial de los datos.**

Hay muchas fuentes que predicen un crecimiento exponencial de datos. Sin embargo, todos están de acuerdo en que el tamaño del universo digital se duplicará al menos cada dos años. Los datos generados por humanos y máquinas están experimentando una tasa de crecimiento general 10 veces más rápida que las empresas tradicionales datos, y los datos máquina están aumentando aún más rápidamente a 50 veces la tasa de crecimiento.

La adquisición y el análisis de datos y su posterior transformación en información procesable es un flujo de trabajo complejo que se extiende más allá de los centros de datos, incluyendo el edge computing y el cloud computing (computación en la nube). La utilización de dispositivos de edge computing, cálculo y análisis in situ, almacenamiento y análisis centralizados y metodologías de aprendizaje profundo (deep learning), que aceleran el procesamiento de datos a escala, requiere un nuevo enfoque tecnológico. Históricamente, los sistemas de procesamiento y análisis de datos tenían características especializadas para cargas de trabajo de análisis empresarial y computación de alto rendimiento (HPC). Sin embargo, con el advenimiento del big data y la informática basada en x86 estándar de la industria, estamos viendo una convergencia en la analítica de big bata, big data e IoT. La investigación de IDC clasifica esta convergencia como análisis de datos de alto rendimiento (HPDA). El mercado HPDA está en el centro de la analítica big data. El factor clave que impulsa la adopción de la informática con uso intensivo de datos es la necesidad de analizar rápidamente volúmenes de datos en aumento en el punto de creación y a escala. Una consecuencia importante de esta explosión es la necesidad de que los usuarios adopten tecnologías avanzadas de análisis de datos. Las empresas ahora tienen acceso a plataformas informáticas más económicas y potentes, y los softwares de análisis moderno, como Hadoop y Spark, permiten análisis en tiempo real para una amplia gama de casos de uso, incluida la detección de fraudes y anomalías, inteligencia empresarial, marketing de afinidad, diseño y desarrollo de productos, automatización de procesos y medicina personalizada. Además de estos marcos de software, la implementación de capacidades de almacenamiento y capacidades que mejoran el flujo de datos, el análisis en el lugar y la eficiencia del almacenamiento, como el almacenamiento de objetos y los sistemas de archivos distribuidos de alto rendimiento, es fundamental para un escalado efectivo.

Según la encuesta de IDC sobre los proyectos de transformación digital más importantes, los encuestados citaron la transformación o transición a la nube (66 %), IoT (32 %) y big data y soluciones cognitivas (27 %) como iniciativas clave para el uso y desarrollo del big data. La nube proporciona escalabilidad y el IoT constituye la base para las inversiones en big data y computación cognitiva. IDC predijo que, en menos de tres años, el 50 % de todo el software de análisis de negocios incorporaría análisis prescriptivos basados en tecnología de computación cognitiva, y la cantidad de datos de alto valor se duplicaría, haciendo que el 60 % de la información entregada a los tomadores de decisiones fuera procesable.

**Desafíos del crecimiento de datos.**

El enorme volumen y la velocidad del crecimiento de los datos presenta varios desafíos:
- Gestión del sistema y creciente complejidad del clúster.
- Limitaciones de energía, enfriamiento y espacio en los centros de datos.
- Complejidad de almacenamiento, movimiento y administración de datos.
- Falta de soporte para entornos heterogéneos.
- Gran escasez de habilidades para integrar y gestionar el ecosistema de big data.

La infraestructura impulsa la mejora.

Las organizaciones están evaluando e implementando infraestructura para impulsar las siguientes mejoras:
- Gestionar el crecimiento y el coste operativo de la infraestructura de big data.
- Proporcionar capacidad flexible y elástica.
- Garantizar el rendimiento para diversas cargas de trabajo.
- Implementar y escalar rápidamente la infraestructura.
- Simplificación de la gestión con big data as a service (BDaaS)

En este documento, nuestro enfoque está en "industrializar" la infraestructura de big data: brindar madurez operativa al ecosistema de datos de Hadoop, hacer que la implementación a escala empresarial sea más fácil y rentable, y hacer que las empresas pasen de la etapa de prueba de concepto (PoC) a desarrollos en producción.

## Se pide

Tras la lectura del texto, responder a las siguientes preguntas:
1. En este artículo se habla de un crecimiento exponencial de los datos. ¿Cuáles son los factores que pueden llevar a este rápido incremento de los datos?
2. En este artículo, las tecnologías big data se incluyen dentro del ámbito de high-performance data analytics (HPDA). ¿Por qué las tecnologías big data son la clave para poder manejar este volumen de crecimiento acelerado de datos?
3. En el texto se habla de tecnologías HPDA y tecnologías cloud. ¿Cuándo debería una empresa optar por una compra de infraestructura propia (on-premise), y cuándo debería moverse hacia cloud?

## Solución

1. **En este artículo se habla de un crecimiento exponencial de los datos. ¿Cuáles son los factores que pueden llevar a este rápido incremento de los datos?**

    El creciente volumen de información se debe a varios factores. Por ejemplo:

    - **Web.** Toda la información de comportamiento del usuario en medios digitales —cada clic, cada acción— se mide y se recoge y, con ella, es posible conocer el comportamiento digital de los usuarios y, por tanto, hacerlo más eficiente para maximizar el retorno obtenido de ellos.
    - **Redes sociales.** Uno de los medios que hoy proporcionan mayor volumen de información son las redes sociales. Todos los días se generan ingentes cantidades de información que, con una correcta explotación, muestran de forma clara las tendencias en opinión y comportamiento colectivo de sus usuarios.
    - **Internet of things.** Hoy en día, la gran mayoría de los dispositivos del hogar tienen una IP. Las ciudades inteligentes, los coches inteligentes… Todos ellos son fuentes de información que vuelcan datos en tiempo real a grandes centros de información, donde, con un procesamiento eficiente, pueden mostrar pautas de comportamiento para optimizar su eficiencia, reducir la tasa de fallos y, en definitiva, optimizar su operativa.
    - **M2M.** En este caso, se hace referencia a toda la información generada por los logs de sistemas e infraestructuras. Un procesamiento inteligente de esta información permite hacer más eficiente la operativa diaria de estos sistemas en tiempo real, calcular indicadores tempranos de fallos y maximizar la utilización de estos sistemas.
    - **Información no estructurada.** Hoy en día se estima que más del 80 % de la información disponible es no estructurada, ya sean texto, grabaciones de audio, imágenes, vídeos, etc. Ser capaces de procesar esta información y extraer indicadores de valor abre un abanico de nuevas posibilidades y capacidades para las empresas.
  
2. **En este artículo, las tecnologías big data se incluyen dentro del ámbito de highperformance data analytics (HPDA). ¿Por qué las tecnologías big data son la clave para poder manejar este volumen de crecimiento acelerado de datos?**

    El principal elemento que hace que las tecnologías big data sean una solución para la necesidad de procesamiento masivo de datos es la relación potencia/coste.

    El big data es una tecnología paralelizable, es decir, el escalado es horizontal. El escalado horizontal consiste en añadir infraestructura en paralelo. Con este esquema el incremento en potencia es lineal con respecto al coste. Por ejemplo, si se tiene un clúster de diez máquinas, con un coste por máquina de 5000 euros, y se precisa duplicar la potencia, se añadirían diez máquinas más al clúster, con un coste total de 50 000 € extra. Si se necesita volver a duplicar lo potencia, se haría otra vez lo mismo.

    Otro tipo de tecnologías, con escalado horizontal, necesitan aumentar la potencia de los servidores. Y un servidor con potencia N y coste Y no sigue la norma de potencia 2*N es igual a 2*Y de coste, sino que el coste, habitualmente, es K*Y, donde K es un valor mayor de 2. Por tanto, la relación potencia/coste en un escalado vertical sigue una curva exponencial, no lineal, como en el caso del big data.

    Además, los sistemas de almacenamiento de big data se basan en la premisa de usar muchos discos, pero de bajo coste, replicando la información entre ellos. Esto hace que el coste de almacenamiento de información decrezca considerablemente.

    Todo esto, unido, hace que el coste de almacenamiento y procesamiento haya bajado drásticamente, permitiendo, con el mismo presupuesto, procesar y trabajar sobre un volumen mucho mayor de información.

3. **En el texto se habla de tecnologías HPDA y tecnologías cloud. ¿Cuándo debería una empresa optar por una compra de infraestructura propia (on-premise) y cuándo debería moverse hacia cloud?**

    Uno de los puntos principales de decisión cuando se trabaja con tecnologías HPDA es si realizar una compra de infraestructura u optar por una aproximación cloud. En función del tipo de proyecto y necesidades de procesamiento, es mejor optar por una u otra solución. A continuación, se detallan algunas de sus características:

    <img width="1382" height="713" alt="image" src="https://github.com/user-attachments/assets/20c75f65-365c-4679-b985-0876604b092e" />

    <img width="921" height="736" alt="image" src="https://github.com/user-attachments/assets/9eb7f460-752e-431d-b9ad-8695b5d710ef" />
