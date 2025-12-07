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


