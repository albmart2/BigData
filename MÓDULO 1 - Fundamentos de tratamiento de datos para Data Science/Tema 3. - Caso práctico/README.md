# Que pide

## ENUNCIADO

Considérese una base de datos para gestionar las solicitudes de acceso de estudiantes a los institutos. La información que se desea almacenar es:

- Sobre los institutos: nombre, área de la ciudad donde se encuentra y número máximo de plazas.
- Sobre los estudiantes: identificador de estudiante, nombre, puntos que tiene para acceder y un valor de corrección.
- Sobre las solicitudes: identificador de estudiante, nombre del instituto, vía solicitada y decisión sobre la solicitud.

Se van a crear tres tablas: institutos, estudiantes y solicitudes.

```SQL
CREATE TABLE Institutos(Nombre_Inst CHAR(35), Area CHAR(35), Plazas INTEGER,
PRIMARY KEY ( Nombre_Inst ),
UNIQUE ( Nombre_Inst, Area ));
CREATE TABLE Estudiantes(ID INTEGER, Nombre_Est CHAR(35), Puntos REAL, Valor INTEGER,
PRIMARY KEY ( ID ),
UNIQUE ( ID ) );
CREATE TABLE Solicitudes(ID INTEGER, Nombre_Inst CHAR(35), Via CHAR(35), Decision CHAR(35),
PRIMARY KEY ( ID, Nombre_Inst, Via ),
FOREIGN KEY ( ID ) REFERENCES Estudiantes ( ID ),
FOREIGN KEY ( Nombre_Inst ) REFERENCES
 Institutos ( Nombre_Inst ),
UNIQUE ( ID, Nombre_Inst, Via ) );
```

Hacer las siguientes consultas:
1. Obtener los nombres y notas de los estudiantes, así como el resultado de su solicitud, de manera que tengan un valor de corrección menor que 1000 y hayan solicitado la vía de “Tecnología” en el “Instituto Ramiro de Maeztu”.
2. Obtener la información sobre todas las solicitudes: ID y nombre del estudiante, nombre del instituto, puntos y plazas, ordenadas de forma decreciente por los puntos y en orden creciente de plazas.
3. Obtener todas las solicitudes a vías denominadas como “Ciencias” o “Ciencias Sociales”.
4. Obtener los estudiantes cuya puntuación ponderada cambia en más de un punto respecto a la puntuación original.
5. Borrar a todos los estudiantes que solicitaron más de dos vías diferentes.
6. Obtener las vías en las que la puntuación máxima de las solicitudes está por debajo de la media.
7. Obtener los nombres de los estudiantes y las vías que han solicitado.
8. Obtener el nombre de los estudiantes y la puntuación con valor de ponderación menor de 1000 que hayan solicitado la vía de “Tecnología” en el “Instituto San Isidro”.

## DATOS
Rellenar las tablas con los siguientes datos:

### Tabla Institutos

<img width="600" height="200" alt="image" src="https://github.com/user-attachments/assets/abfc2e44-a6e6-4d93-8df8-f02563bbee2a" />

### Tabla estudiantes

<img width="445" height="519" alt="image" src="https://github.com/user-attachments/assets/d9313136-5c2e-4059-9418-972527f21e81" />

### Tabla Solicitudes

<img width="757" height="800" alt="image" src="https://github.com/user-attachments/assets/2bfb8820-6b0a-47c2-bf8b-75d57d407200" />

# SOLUCIÓN

- La inserción de datos se haría de la siguiente manera:
  - Tabla Institutos

    ```SQL
    insert into Institutos values ('Instituto San Isidro', 'Centro', 150);
    insert into Institutos values ('Instituto Ramiro de Maeztu', 'Salamanca', 360);
    insert into Institutos values ('Instituto Arturo Soria', 'Hortaleza', 100);
    insert into Institutos values ('Instituto Torres Quevedo', 'Moncloa', 210);
    ```
    
  - Tabla Estudiantes
    ```SQL
    insert into Estudiantes values (123, 'Antonio', 8.9, 1000);
    insert into Estudiantes values (234, 'Juan', 8.6, 1500);
    insert into Estudiantes values (345, 'Isabel', 8.5, 500);
    insert into Estudiantes values (456, 'Doris', 7.9, 1000);
    insert into Estudiantes values (567, 'Eduardo', 6.9, 2000);
    insert into Estudiantes values (678, 'Carmen', 5.8, 200);
    insert into Estudiantes values (789, 'Isidro', 8.4, 800);
    insert into Estudiantes values (987, 'Elena', 6.7, 800);
    insert into Estudiantes values (876, 'Irene', 6.9, 400);
    insert into Estudiantes values (765, 'Javier', 7.9, 1500);
    insert into Estudiantes values (654, 'Alfonso', 7.9, 1000);
    insert into Estudiantes values (543, 'Pedro', 5.4, 2000);
    ```
  - Tabla Solicitudes
    ```SQL
    insert into Solicitudes values (123, 'Instituto Ramiro de Maeztu', 'Tecnologia', 'Si');
    insert into Solicitudes values (123, 'Instituto Ramiro de Maeztu', 'Ciencias Sociales', 'No');
    insert into Solicitudes values (123, 'Instituto San Isidro', 'Tecnologia', 'Si');
    insert into Solicitudes values (123, 'Instituto Torres Quevedo', 'Ciencias Sociales', 'Si');
    insert into Solicitudes values (234, 'Instituto San Isidro', 'Ciencias', 'No');
    insert into Solicitudes values (345, 'Instituto Arturo Soria', 'Tecnologia', 'Si');
    insert into Solicitudes values (345, 'Instituto Torres Quevedo', 'Tecnologia', 'No');
    insert into Solicitudes values (345, 'Instituto Torres Quevedo', 'Ciencias', 'Si');
    insert into Solicitudes values (345, 'Instituto Torres Quevedo', 'Ciencias Sociales', 'No');
    insert into Solicitudes values (678, 'Instituto Ramiro de Maeztu', 'Ciencias Sociales', 'Si');
    insert into Solicitudes values (987, 'Instituto Ramiro de Maeztu', 'Tecnologia', 'Si');
    insert into Solicitudes values (987, 'Instituto San Isidro', 'Tecnologia', 'Si');
    insert into Solicitudes values (876, 'Instituto Ramiro de Maeztu', 'Tecnologia', 'No');
    insert into Solicitudes values (876, 'Instituto Arturo Soria', 'Ciencias', 'Si');
    insert into Solicitudes values (876, 'Instituto Arturo Soria', 'Ciencias Sociales', 'No');
    insert into Solicitudes values (765, 'Instituto Ramiro de Maeztu', 'Ciencias Sociales', 'Si');
    insert into Solicitudes values (765, 'Instituto Torres Quevedo', 'Ciencias Sociales', 'No');
    insert into Solicitudes values (765, 'Instituto Torres Quevedo', 'Ciencias', 'Si');
    insert into Solicitudes values (543, 'Instituto Arturo Soria', 'Tecnologia', 'No');
    ```
- La resolución de las consultas se haría de la siguiente forma:
  1. Consulta 1:

     ```SQL
     SELECT Nombre_Est, Decision FROM Estudiantes,Solicitudes
     WHERE Estudiantes.ID = Solicitudes.ID
     AND Valor < 1000 AND Via = 'Tecnologia' AND Nombre_Inst = 'Instituto Ramiro de Maeztu';
     ```

  2. Consulta 2:
  
     ```SQL
     SELECT Estudiantes.ID, Nombre_Est, Puntos, Solicitudes.Nombre_Inst, Plazas FROM Estudiantes, Institutos, Solicitud;
     ```

  3. Consulta 3:

     ```SQL
     SELECT * FROM Solicitudes WHERE Via like '%Ciencias%';
     ```

  4. Consulta 4:

     ```SQL
     SELECT ID, Nombre_Est, Puntos, Puntos * Valor / 1000.0 AS Ponderada FROM Estudiantes WHERE ABS( Puntos * (Valor / 1000.0) - Puntos ) > 1;
     ```
     
  5. Consulta 5:

     ```SQL
     SELECT * FROM Solicitudes WHERE ID IN (SELECT ID FROM Solicitudes GROUP BY ID HAVING COUNT (Via) >2);
     ```
     
  6. Consulta 6:

     ```SQL
     SELECT Via FROM Estudiantes, Solicitudes WHERE Estudiantes.ID = Solicitudes.ID GROUP BY Via HAVING MAX(Puntos) < (SELECT AVG(Puntos) FROM Solicitudes);
     ```
     
  7. Consulta 7:

     ```SQL
     SELECT DISTINCT Nombre_Est, Via FROM Estudiantes JOIN Solicitudes ON Estudiantes.ID = Solicitudes.ID;
     ```

  8. Consulta 8:
 
     ```SQL
     SELECT Nombre_Est, Puntos FROM Estudiantes JOIN Solicitudes ON Estudiantes.ID = Solicitudes.ID AND Valor < 1000 AND Via = 'Tecnología' AND Instituto = 'Instituto San Isidro';
     ```
