# Caso práctico con solución
## Caso práctico - Parte A
### Enunciado
El Museo de Arte desea crear una base de datos que organice semánticamente el patrimonio cultural del que dispone. Se ha recopilado información acerca de todos los recursos de los que dispone y de los autores de estos.

Los recursos pueden ser de alguno de los siguientes tipos: cuadros, manuscritos, cerámica, escultura y música. Todos los recursos han sido digitalizados y disponen de una dirección web asociada. Cada recurso, con independencia del autor al que está asociado, se puede categorizar respecto a diversos aspectos, tales como técnicas empleadas, escuela o corriente artística, periodo artístico del autor, etc.

El museo ha decidido, en una primera fase, utilizar la corriente artística a la que pertenece el recurso, que se subdivide en renacimiento, modernismo, cubismo e impresionismo. Además, de cada recurso se conocen la dirección web y la dirección física en que se encuentra localizado. Se ha decidido utilizar una base de datos en grafo para almacenar toda la información.

### Se pide
Encontrar una forma de estructurar la información de manera jerárquica, que facilite la recuperación de los recursos de una corriente artística concreta, que esté asociada a un autor.

### Solución

Para resolver el caso planteado, se pueden diseñar tres soluciones diferentes, dependiendo de la forma en la que se desee acceder a la información:

- Si se accede mediante el nombre de la corriente artística a la que pertenece la obra.
- Si se accede mediante el tipo de recurso.
- Si se accede mediante el nombre del autor.

Así, cualquiera de las soluciones planteadas requiere la construcción de un árbol de tipo multinivel, donde cada uno de los niveles del árbol representa un filtro sobre la información y permite quedarse solo con aquella que interesa y obviar el resto. Por ejemplo, si se aplica la estructura del árbol multinivel a la primera solución planteada de acceso, a través del nombre de la corriente artística a la que pertenece la obra, este primer nivel del árbol estaría formado por los nombres de las corrientes artísticas (de esta manera el nombre de la corriente artística servirá para realizar un primer filtro sobre la información). En el siguiente nivel, habría dos opciones posibles. Una sería que aparecieran los nodos que representan el tipo de recurso (este nivel sirve nuevamente como filtro final, para quedarse solamente con el tipo de recursos de la corriente artística seleccionada en el primer nivel). La opción alternativa sería representar en este nivel el nombre del autor al que pertenece el recurso. Dependiendo de la opción tomada, en el siguiente nivel aparecerían los nodos correspondientes al filtro no utilizado. Finalmente, en el último nivel, que representaría las hojas del árbol, se encontrarían las direcciones físicas o webs en que se pueden encontrar los recursos.

Obsérvese que las otras dos aproximaciones comentadas se implementan de manera análoga, basta con ir considerando los filtros en el orden adecuado.

Para ilustrar la solución planteada se va a utilizar Neo4j, así como los siguientes datos de ejemplo:
#### Corriente renacentista:
- Díptico Anunciación, de Jan van Eyck. Situado en la dirección física: Sala 3, Elemento 8.
- Manuscrito Roman de Gillion de Trazegnies, de Lieven van Lathem. Situado en la dirección física: Sala 6, Elemento 16.
- Escultura Les Mangeurs de Raisins, de Servret, Boucher y Falconet. Situada en la dirección física: Sala 4, Elemento 5.

#### Corriente impresionista:
- Cuadro Portrait, de Joaquín Sorolla. Situado en la dirección física: Sala 1, Elemento 10.
- Cuadro La mestiza, de Juan Luna Novicio. Situado en la dirección física: Sala 1, Elemento 15.
- Cuadro Lilas blancas en un vaso de cristal, de Édouard Manet. Situado en la dirección física: Sala 2, Elemento 5.
#### Corriente cubista:
- Cuadro La botella de anís, de Juan Gris. Situado en la dirección física: Sala 6, Elemento 10.
- Escultura Amantes, de Raymond Duchamp-Villon. Situada en la dirección física: Sala 11, Elemento 1.
- Escultura Maggy, de Raymond Duchamp-Villon. Situada en la dirección física: Sala 2, Elemento 6.
#### Corriente modernista:
- Escultura Circe, de Bertram Mackennal. Situada en la dirección física: Sala 9, Elemento 10.
- Cuadro Judith II (Salomé), de Gustav Klimt. Situado en la dirección física: Sala 9, Elemento 13.
- Cuadro A carta, de Eliseu Visconti. Situado en la dirección física: Sala 17, Elemento 8.

La codificación en Neo4j sería la siguiente:
```cypher
CREATE
(c1:corriente {Nombre: "Renacentista"}),
(c2:corriente {Nombre: "Cubista"}),
(c3:corriente {Nombre: "Impresionista"}),
(c4:corriente {Nombre: "Modernista"}),
(a1:autor {Nombre: "Jan van Eyck"}),
(a2:autor {Nombre: "Lieven van Lathem"}),
(a3:autor {Nombre: "Boucher"}),
(a4:autor {Nombre: "Joaquín Sorolla"}),
(a5:autor {Nombre: "Juan Luna Novicio"}),
(a6:autor {Nombre: "Eduardo Manet"}),
(a7:autor {Nombre: "Juan Gris"}),
(a8:autor {Nombre: "Raymond Duchamp-Villon"}),
(a9:autor {Nombre: "Bertram Mackennal"}),
(a10:autor {Nombre: "Gustav Klimt"}),
(a11:autor {Nombre: "Eliseu Visconti"}),
(re1:recurso {Nombre: "Díptico de la Anunciación", Sala:3 ,Elemento:8 , tip
ntura",DireccionWeb: "www.museo/eyck/anunciación.png"}),
(re2:recurso {Nombre: "Roman de Gillion de Trazegnies", Sala:6 ,tipo: "Manu
", Elemento:16 ,DireccionWeb: "www.museo/lathem/roman.png"}),
(re3:recurso {Nombre: "Les Mangeurs de Raisins", Sala:4 ,Elemento:5 ,tipo:
tura", DireccionWeb: "www.museo/boucer/mangeurs.png"}),
(re4:recurso {Nombre: "Portrait", Sala:1 ,Elemento:10, tipo: "Pintura",Dire
eb: "www.museo/sorolla/portrait.png"}),
(re5:recurso {Nombre: "La mestiza", Sala:1 ,Elemento:15, tipo: "Pintura",Di
nWeb: "www.museo/novicio/mestiza.png"}),
(re6:recurso {Nombre: "Lilas blancas en un vaso de cristal", Sala:2 ,Elemen
tipo: "Pintura",DireccionWeb: "www.museo/manet/lilas.png"}),
(re7:recurso {Nombre: "La botella de anís", Sala:6 ,Elemento:10 , tipo: "Pi
,DireccionWeb: "www.museo/gris/anis.png"}),
(re8:recurso {Nombre: "Amantes", Sala:11 ,Elemento:1, tipo: "Escultura",Dir
Web: "www.museo/duchamp-villon/amantes.png"}),
(re9:recurso {Nombre: "Maggy", Sala:2 ,Elemento:6, tipo: "Escultura",Direcc
: "www.museo/duchamp-villon/amantes.png"}),
(re10:recurso {Nombre: "Circe", Sala:9 ,Elemento:10 , tipo: "Escultura",Dir
Web: "www.museo/mackennal/circe.png"}),
(re11:recurso {Nombre: "Judith II Salomé", Sala:9 ,Elemento:13, tipo: "Pint
ireccionWeb: "www.museo/klimt/salome.png"}),
(re12:recurso {Nombre: "A carta", Sala:17 ,Elemento:8, tipo: "Pintura",Dire
eb: "www.museo/visconti/acarta.png"}),
(t1:tiporecurso {TipoR: "Manuscrito"}),
(t2:tiporecurso {TipoR: "Cuadro"}),
(t3:tiporecurso {TipoR: "Escultura"}),
(t4:tiporecurso {TipoR: "Cerámica"}),
(t5:tiporecurso {TipoR: "Música"}),
(c1)-[r1:TIENE_ASOCIADO]->(a1),
(c1)-[r2:TIENE_ASOCIADO]->(a2),
(c1)-[r3:TIENE_ASOCIADO]->(a3),
(c2)-[r4:TIENE_ASOCIADO]->(a4),
(c2)-[r5:TIENE_ASOCIADO]->(a5),
(c2)-[r6:TIENE_ASOCIADO]->(a6),
(c3)-[r7:TIENE_ASOCIADO]->(a7),
(c3)-[r8:TIENE_ASOCIADO]->(a8),
(c4)-[r9:TIENE_ASOCIADO]->(a9),
(c4)-[r10:TIENE_ASOCIADO]->(a10),
(c4)-[r11:TIENE_ASOCIADO]->(a11),
(a1)-[cr1:CREO]->(re1),
(a2)-[cr2:CREO]->(re2),
(a3)-[cr3:CREO]->(re3),
(a4)-[cr4:CREO]->(re4),
(a5)-[cr5:CREO]->(re5),
(a6)-[cr6:CREO]->(re6),
(a7)-[cr7:CREO]->(re7),
(a8)-[cr8:CREO]->(re8),
(a8)-[cr9:CREO]->(re9),
(a9)-[cr10:CREO]->(re10),
(a10)-[cr11:CREO]->(re11),
(a11)-[cr12:CREO]->(re12)
```

Si se ejecuta la sentencia siguiente, se pueden recuperar los datos introducidos:

```cypher
MATCH (c:corriente)-[r]->(f)-[h]->(g) RETURN c,r,f,h,g LIMIT 25
```

<img width="769" height="686" alt="image" src="https://github.com/user-attachments/assets/1e654db7-04e5-492a-ae0d-bbe4d9a0607f" />

## Caso práctico - Parte B

### Enunciado

Considérese una base de datos en Neo4j con las siguientes características:
- Dispondrá de cuatro tipos de nodos: nodos de tipo autor, nodos de tipo libro, nodos de tipo género y nodos de tipo editorial.
- Se definen las siguientes relaciones:
  - La relación *ES_AUTOR_DE* une nodos de tipo escritor con nodos de tipo libro.
  - La relación *ESTÁ_PUBLICADO_EN* une nodos de tipo libro con nodos de tipo editorial.
  - La relación *ES_DE_GÉNERO* une nodos de tipo libro con nodos de tipo género.
- Los nodos de tipo autor tienen la propiedad asociada Nombre.
- Los nodos de tipo libro tienen la propiedad asociada Título.
- Los nodos de tipo editorial tienen la propiedad asociada Nombre.

1. Crear la base de datos descrita con los siguientes datos:
    1. Eduardo Mendoza, El laberinto de las aceitunas, editorial Seix Barral, policíaca.
    2. Eduardo Mendoza, La ciudad de los prodigios, editorial Seix Barral, policíaca.
    3. Eduardo Mendoza, Una comedia ligera, editorial Planeta, comedia.
    4. Dan Brown, Inferno, editorial Planeta, policíaca.
    5. Dan Brown, El símbolo perdido, editorial Anaya, misterio.
    6. Dan Brown, El código Da Vinci, editorial Alianza, misterio.
    7. Ken Follet, El umbral de la eternidad, editorial Planeta, histórica.
    8. Ken Follet, Los pilares de la Tierra, editorial Anaya, histórica.
    9. Bram Stoker, Drácula, editorial Sirio, terror.
    10. Gustavo Adolfo Bécquer, La cruz del diablo, editorial Anaya, misterio.
    11. Gustavo Adolfo Bécquer, Rimas y leyendas, editorial Alianza, romántica.
2. Mostrar el grafo donde aparecen autores, libros y editoriales.
3. Mostrar el grafo donde aparecen autores, libros y géneros.
4. Recuperar todas las obras de Dan Brown.
5. Recuperar los libros que están publicados por la editorial Alianza.
6. Recuperar los autores que han escrito para Alianza y Anaya.
7. ¿Cuántos libros ha escrito Ken Follet?
8. ¿Qué libros ha escrito Dan Brown y de qué género es cada uno?
9. Eliminar el nodo referido a Bram Stoker.

### Solución

#### Consulta 1

```cypher
CREATE (:Autor {Nombre : "Eduardo Mendoza"})
CREATE (:Autor {Nombre : "Dan Brown"})
CREATE (:Autor {Nombre : "Ken Follet"})
CREATE (:Autor {Nombre : "Bram Stocker"})
CREATE (:Autor {Nombre : "Gustavo Adolfo Becquer"})
CREATE (:Libro {Titulo : "El laberinto de las aceitunas" })
CREATE (:Libro {Titulo : "La ciudad de los prodigios"})
CREATE (:Libro {Titulo : "Una comedia ligera" })
CREATE (:Libro {Titulo : "Inferno" })
CREATE (:Libro {Titulo : "El símbolo perdido" })
CREATE (:Libro {Titulo : "El código Da Vinci" })
CREATE (:Libro {Titulo : "El umbral de la eternidad"})
CREATE (:Libro {Titulo : "Los pilares de la Tierra" })
CREATE (:Libro {Titulo : "Drácula"})
CREATE (:Libro {Titulo : "La cruz del diablo" })
CREATE (:Libro {Titulo : "Rimas y leyendas" })
CREATE (:Editorial {Nombre : "Seix Barral"})
CREATE (:Editorial {Nombre : "Planeta"})
CREATE (:Editorial {Nombre : "Alianza"})
CREATE (:Editorial {Nombre : "Anaya"})
CREATE (:Editorial {Nombre : "Sirio"})
CREATE (:Genero { Nombre: "Policiaco"})
CREATE (:Genero { Nombre : "Comedia"})
CREATE (:Genero { Nombre: "Misterio"})
CREATE (:Genero {Nombre : "Histórica"})
CREATE (:Genero {Nombre : "Terror"})
CREATE (:Genero {Nombre : "Romántica"});
Match (a:Autor {Nombre : "Eduardo Mendoza"}),(l:Libro {Titulo : "El laberin
las aceitunas"}) WITH a,l CREATE (a)-[:ES_AUTOR_DE]->(l)
Match (a:Autor {Nombre : "Eduardo Mendoza"}),(l:Libro {Titulo : "La ciudad
prodigios"}) WITH a,l CREATE (a)-[:ES_AUTOR_DE]->(l)
Match (a:Autor {Nombre : "Eduardo Mendoza"}),(l:Libro {Titulo : "Una comedi
ra"}) WITH a,l CREATE (a)-[:ES_AUTOR_DE]->(l)
Match (a:Autor {Nombre : "Dan Brown"}),(l:Libro {Titulo : "Inferno"}) WITH
EATE (a)-[:ES_AUTOR_DE]->(l)
Match (a:Autor {Nombre : "Dan Brown"}),(l:Libro {Titulo : "El símbolo perdi
WITH a,l CREATE (a)-[:ES_AUTOR_DE]->(l)
Match (a:Autor {Nombre : "Dan Brown"}),(l:Libro {Titulo : "El código Da Vin
WITH a,l CREATE (a)-[:ES_AUTOR_DE]->(l)
Match (a:Autor {Nombre : "Ken Follet"}),(l:Libro {Titulo : "El umbral de la
idad"}) WITH a,l CREATE (a)-[:ES_AUTOR_DE]->(l)
Match (a:Autor {Nombre : "Ken Follet"}),(l:Libro {Titulo : "Los pilares de
rra"}) WITH a,l CREATE (a)-[:ES_AUTOR_DE]->(l)
Match (a:Autor {Nombre : "Bram Stoker"}),(l:Libro {Titulo : "Drácula"}) WIT
CREATE (a)-[:ES_AUTOR_DE]->(l)
Match (a:Autor {Nombre : "Gustavo Adolfo Becquer"}),(l:Libro {Titulo : "La
del diablo"}) WITH a,l CREATE (a)-[:ES_AUTOR_DE]->(l)
Match (a:Autor {Nombre : "Gustavo Adolfo Becquer"}),(l:Libro {Titulo : "Rim
leyendas"}) WITH a,l CREATE (a)-[:ES_AUTOR_DE]->(l)
Match (l:Libro {Titulo : "El laberinto de las aceitunas"}),(e:Editorial {No
"Seix Barral"}) CREATE (l)-[:ESTÁ_PUBLICADO_EN]->(e)
Match (l:Libro {Titulo : "La ciudad de los prodigios"}),(e:Editorial {Nombr
eix Barral"}) WITH l,e CREATE (l)-[:ESTÁ_PUBLICADO_EN]->(e)
Match (l:Libro {Titulo : "Una comedia ligera"}),(e:Editorial {Nombre : "Pla
) WITH l,e CREATE (l)-[:ESTÁ_PUBLICADO_EN]->(e)
Match (l:Libro {Titulo : "Inferno"}),(e:Editorial {Nombre : "Planeta"}) WIT
CREATE (l)-[:ESTÁ_PUBLICADO_EN]->(e)
Match (l:Libro {Titulo : "El símbolo perdido"}),(e:Editorial {Nombre : "Ana
WITH l,e CREATE (l)-[:ESTÁ_PUBLICADO_EN]->(e)
Match (l:Libro {Titulo : "El código Da Vinci"}),(e:Editorial {Nombre : "Ali
) WITH l,e CREATE (l)-[:ESTÁ_PUBLICADO_EN]->(e)
Match (l:Libro {Titulo : "El umbral de la eternidad"}),(e:Editorial {Nombre
aneta"}) WITH l,e CREATE (l)-[:ESTÁ_PUBLICADO_EN]->(e)
Match (l:Libro {Titulo : "Los pilares de la Tierra"}),(e:Editorial {Nombre
ya"}) WITH l,e CREATE (l)-[:ESTÁ_PUBLICADO_EN]->(e)
Match (l:Libro {Titulo : "Drácula"}),(e:Editorial {Nombre : "Sirio"}) WITH
EATE (l)-[:ESTÁ_PUBLICADO_EN]->(e)
Match (l:Libro {Titulo : "La cruz del diablo"}),(e:Editorial {Nombre : "Ana
WITH l,e CREATE (l)-[:ESTÁ_PUBLICADO_EN]->(e)
Match (l:Libro {Titulo : "Rimas y leyendas"}),(e:Editorial {Nombre : "Alian
WITH l,e CREATE (l)-[:ESTÁ_PUBLICADO_EN]->(e)
Match (l:Libro {Titulo : "El laberinto de las aceitunas"}),(g:Genero {Nombr
oliciaco"}) WITH l,g CREATE (l)-[:ES_DE_GENERO]->(g)
Match (l:Libro {Titulo : "La ciudad de los prodigios"}), (g:Genero {Nombre
iciaco"}) WITH l,g CREATE (l)-[:ES_DE_GENERO]->(g)
Match (l:Libro {Titulo : "Una comedia ligera"}) ,(g:Genero {Nombre : "Comed
WITH l,g CREATE (l)-[:ES_DE_GENERO]->(g)
Match (l:Libro {Titulo : "Inferno"}) ,(g:Genero {Nombre : "Policiaco"}) WIT
CREATE (l)-[:ES_DE_GENERO]->(g)
Match (l:Libro {Titulo : "El símbolo perdido"}) ,(g:Genero {Nombre : "Miste
WITH l,g CREATE (l)-[:ES_DE_GENERO]->(g)
Match (l:Libro {Titulo : "El código Da Vinci"}) ,(g:Genero {Nombre : "Miste
WITH l,g CREATE (l)-[:ES_DE_GENERO]->(g)
Match (l:Libro {Titulo : "El umbral de la eternidad"}) ,(g:Genero {Nombre
erio"}) WITH l,g CREATE (l)-[:ES_DE_GENERO]->(g)
Match (l:Libro {Titulo : "Los pilares de la Tierra"}) ,(g:Genero {Nombre :
rica"}) WITH l,g CREATE (l)-[:ES_DE_GENERO]->(g)
Match (l:Libro {Titulo : "Drácula"}),(g:Genero {Nombre : "Terror"}) WITH l,
TE (l)-[:ES_DE_GENERO]->(g)
Match (l:Libro {Titulo : "La cruz del diablo"}),(g:Genero {Nombre : "Mister
WITH l,g CREATE (l)-[:ES_DE_GENERO]->(g)
Match (l:Libro {Titulo : "Rimas y leyendas"}),(g:Genero {Nombre : "Romántic
WITH l,g CREATE (l)-[:ES_DE_GENERO]->(g)
```

#### Consulta 2

```cypher
Match (a)-[:ES_AUTOR_DE]->(f)-[:ESTÁ_PUBLICADO_EN]->(g) return a,f,g
```

<img width="685" height="680" alt="image" src="https://github.com/user-attachments/assets/fb3df149-0a01-433a-b4bc-cfaa646a1b5b" />

#### Consulta 3

```cypher
Match (a)-[:ES_AUTOR_DE]->(f)-[:ES_DE_GENERO]->(g) return a,f,g
```

<img width="724" height="806" alt="image" src="https://github.com/user-attachments/assets/a38383d3-d35e-43ad-b807-b803551d76cb" />

#### Consulta 4

```cypher
MATCH (n:Autor {Nombre:"Dan Brown"})-[:ES_AUTOR_DE]-(f) RETURN n,f
```

<img width="258" height="167" alt="image" src="https://github.com/user-attachments/assets/77408693-69f2-40fe-b19a-ce7bfcd448af" />

#### Consulta 5

```cypher
MATCH (l:Libro) -[:ESTÁ_PUBLICADO_EN]->(e:Editorial {Nombre: "Alianza"}) RETURN 1,e;
```

<img width="163" height="176" alt="image" src="https://github.com/user-attachments/assets/16b219b3-681d-41d5-8f5e-599612fa2a72" />

#### Consulta 6

```cypher
MATCH (a:Autor)- [:ES_AUTOR_DE]-> (l:Libro) -[:ESTÁ_PUBLICADO_EN] -

( e:Editorial {Nombre: "Anaya"})
WITH a
MATCH (a:Autor)- [:ES_AUTOR_DE]-> (l:Libro) -[:ESTÁ_PUBLICADO_EN] -

( e:Editorial {Nombre: "Alianza"})
return a.Nombre
```

<img width="1298" height="332" alt="image" src="https://github.com/user-attachments/assets/985d636f-5907-4efd-8519-57f15dbecd33" />

#### Consulta 7

```cypher
MATCH (a:Autor{Nombre:"Ken Follet"})- [:ES_AUTOR_DE]-> (l) return a , count
```

<img width="1300" height="493" alt="image" src="https://github.com/user-attachments/assets/105ee873-aa25-40dd-ab5d-c5c8f5b697eb" />

#### Consulta 8

```cypher
MATCH (a:Autor{Nombre:"Dan Brown"})- [:ES_AUTOR_DE]-> (l)-

[:ES_DE_GENERO]->(g) return l , g
```

<img width="1299" height="717" alt="image" src="https://github.com/user-attachments/assets/b16a0691-52db-48c8-af50-a7ef9ac0d136" />

#### Consulta 9

Primero hay que eliminar sus relaciones:

```cypher
MATCH (a:Autor{Nombre: "Bram Stoker"})-[r:ES_AUTOR_DE]->(f)
DELETE r;
```

A continuación, se elimina el nodo:

```cypher
MATCH (a:Autor{Nombre: "Bram Stoker"})
DELETE a;
```
