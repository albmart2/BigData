# Caso práctico con solución

## Enunciado

Crear una base de datos en Cassandra para gestionar las prácticas de una asignatura en la que los estudiantes pueden pertenecer a diferentes grupos.

Se sabe que las consultas se realizarán con base en el grupo al que pertenecen.

La información para gestionar consiste en nombre y apellidos del estudiante, correo electrónico del estudiante y nombre del grupo al que pertenece.

## Solución

Para resolverlo, hay que tener en cuenta varios aspectos:

<ol type="a">
  <li>En Cassandra no es posible repartir la información en varias familias de columnas y luego usar un join para recuperar la información. Es decir, que no sirve una solución normalizada del tipo:</li>
    <br><table>
          <tr>
          <td>
          <pre>
          CREATE TABLE estudiantes (
              idestudiante uuid,
              nombre text,
              email text,
              apellido text,
              PRIMARY KEY (idestudiante)
          );
          </pre>
          </td>
          <td>
          <pre>
          CREATE TABLE grupos (
              idgrupo uuid,
              nombreGrupo text,
              PRIMARY KEY (idgrupo)
          );
          </pre>
          </td>
          <td>
          <pre>
          CREATE TABLE grupEst (
              idgrupo uuid,
              idestudiante uuid,
              PRIMARY KEY (idgrupo, idestudiante)
          );
          </pre>
          </td>
          </tr>
      </table>
  Este tipo de solución haría necesario realizar un join entre todas las familias de columnas.
  
  <br>Por esta razón, se necesita disponer de toda la información que se desea consultar en una única familia de columnas. Por lo que una primera aproximación a la solución consistiría en lo siguiente:

  ```sql
  CREATE TABLE estudiantes (
    idestudiante uuid,
    nombre text,
    email text,
    apellido text,
    nombre_grupo text,
    PRIMARY KEY(XXXXXX)
  )
  ```
<li>El siguiente problema que surge es elegir la clave primaria adecuada. Lo ideal sería elegir como clave de partición la columna nombre_grupo, dado que se va a buscar por el grupo. De esta forma, se podría buscar por el nombre del grupo y recuperar todos los estudiantes que se encuentren en dicho grupo. Sin embargo, esta opción no garantiza la unicidad y habría problemas con las inserciones cada vez que se insertara un nuevo usuario en un grupo.</li>
  <br><p>Para resolver este problema, se puede añadir a la clave primaria la columna nombre de usuario, para que actúe como columna de agrupamiento. De esta forma se resuelve el problema de la sobreescritura, y sigue permitiendo buscar por el nombre del grupo.</p>
<li>La solución planteada resuelve el problema del acceso, sin embargo, se plantea un problema en cuanto al equilibrado de datos almacenados en los nodos, puesto que podría haber grupos con más estudiantes que otros. Para solucionar este problema, se puede añadir una nueva columna a la clave de partición para que se obtenga como un valor hash calculado con base en la inicial de los nombres de los estudiantes, lo que ayudaría a repartir mejor los datos de los estudiantes de aquellos grupos que son excesivamente grandes.</li>
  <br>Por tanto, la solución final sería la siguiente:

  ```sql
  CREATE TABLE estudiantes (
    idestudiante uuid,
    nombre text,
    email text,
    apellido text,
    nombre_grupo text,
    PRIMARY KEY((nombre_grupo, idestudiante), nombre )
  );
  ```

  <img width="876" height="185" alt="image" src="https://github.com/user-attachments/assets/45b794b3-6f87-4142-8afb-09aedd369b0d" />

</ol>
