# Tema 2. Caso práctico.
## Enunciado
Una compañía del sector financiero realiza el scoring de numerosos clientes y entidades, a partir de los datos e información que recibe de numerosas entidades y fuentes de datos externas.

A diario, esta compañía recibe miles de ficheros que son depositados por fuentes externas en repositorios para ser procesados a continuación y cargarlos en el data warehouse corporativo de la compañía.

Sin embargo, la compañía pretende diseñar un proceso de data quality que permita descartar de forma automática los ficheros fuentes que tengan algún error y cargar únicamente la información que sea correcta.

## Se pide

Realizar el diseño e implementación de una solución sencilla de proceso de data quality que permita verificar, en un proceso previo a la carga en el DW, que la información que se carga cumple unas reglas de formato y negocio definidas por la compañía. En concreto, se solicita:

- Proceso automatizado de data quality.
- Lectura periódica de fichero en formato Excel, .XLS.
- Notificación de error de lectura de fichero o no existencia de fichero en repositorio de destino.
- Aplicación de cuatro reglas de negocio definidas por la compañía.
- Cargar únicamente la información válida en el DW corporativo.
- Enviar notificación a la compañía origen del fichero, para reenvío de información errónea.

Así como la definición de las reglas que deben cumplirse:

- Regla 1:
    - Que CL_RAMO_MOD contenga alguno de estos valores: “14A”, “14D”, “14E”, “14H”, “14L”, “14M”, “14P”, “14R”, “14T”, “14U”, “14Z”.
- Regla 2:
    - Que FECHA_EFECTO sea mayor que FECHA_CALCULO.
- Regla 3:
    - En los casos en los que el campo AGE_AT_ENTRY < 14 -> hay que realizar un recálculo del campo AGE_AT_ENTRY == ROUND((FECHA_EFECTO - FECHA_NACIMIENTO) / 365.25)
- Regla 4:
    - El campo POLIZA debe tener una longitud igual a 9.
 
<img width="1128" height="294" alt="image" src="https://github.com/user-attachments/assets/51ec5d8d-a3fc-45b7-96dc-857ec54c8487" />
