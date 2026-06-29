# Caso práctico con solución

## Enunciado

Resolver las siguientes sentencias en Redis:
1. **Guardar los siguientes datos en claves de tipo nombrei, emaili, con i=1,2,3.**
    1. Juan Gallardo López, con *e-mail* jgl@gmail.com
    2. Isabel Sanz Alonso, con *e-mail* isa10@hotmail.com
    3. Pepe Azul Téllez, con *e-mail* pazte@gmail.com
2. **Obtener el e-mail 2 y el nombre 3 de los anteriores registros.**
    1. Juan Gallardo López, con *e-mail* jgl@gmail.com
    2. Isabel Sanz Alonso, con *e-mail* isa10@hotmail.com
    3. Pepe Azul Téllez, con *e-mail* pazte@gmail.com
3. **Añadir tres nuevos registros para las edades, que son, respectivamente, 34, 36 y 40, usando claves de tipo edadi con *i=1,2,3*.**
4. **Decrementar la edad 2 en cuatro unidades.**
5. **Crear una lista que contenga las siguientes cadenas: Identificador:3434, Nombre: *Antonio Sancho García* y Edad: 34.**
6. **Considerar los datos de la película siguiente (se pide almacenar los datos usando una hash).**
    1. Nombre: ET. El extraterrestre.Año: 1982.
    2. Género: ciencia ficción.
    3. Duración: 115 minutos.
7. **Del anterior agregado, hay que recuperar solo los valores y las claves utilizadas.**
8. **Crear los conjuntos de valores *Colores1={Azul, Amarillo, Rojo, Verde, Gris, Negro}* y *Colores2={Marrón, Negro, Rosa, Azul, Blanco}*. Encontrar la intersección de ambos conjuntos.**
9. **Obtener la unión y la diferencia de los conjuntos anteriores.**
10. **Crear un conjunto ordenado con los siguientes valores: 100, 90, 23, 300, 99, 12.**
