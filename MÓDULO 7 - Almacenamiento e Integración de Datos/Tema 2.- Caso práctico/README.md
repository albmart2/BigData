# Caso Práctico con solución

## Enunciado
 
Considérese una colección de MongoDB que contiene documentos referidos a libros en diferentes formatos.
 
## Documentos de la colección
 
**Documento 1 — libro**
```json
{
  "tipo": "libro",
  "titulo": "Python para todos",
  "ISBN": "987-1-2344-5334-8",
  "editorial": "Prentince Hall",
  "Autor": ["Isabel Carrasco", "Carlos Sanz", "Santiago Merino"],
  "capítulos": [
    { "capitulo": 1, "titulo": "Primeros pasos en Python", "longitud": 20 },
    { "capitulo": 2, "titulo": "El entorno Jupyter Notebook", "longitud": 25 }
  ]
}
```
 
**Documento 2 — ebook**
```json
{
  "tipo": "ebook",
  "titulo": "Historia de Alemania",
  "ISBN": "988-1-3444-6789-9",
  "editorial": "Alianza Editorial",
  "Autor": ["Walter House", "Bryan Reagan"],
  "capítulos": [
    { "capitulo": 1, "titulo": "Prehistoria alemana", "longitud": 40 },
    { "capitulo": 2, "titulo": "La edad media alemana", "longitud": 25 }
  ]
}
```
 
**Documento 3 — libro**
```json
{
  "tipo": "libro",
  "titulo": "El símbolo perdido",
  "ISBN": "5678-18-6784-53433-45",
  "editorial": "Planeta",
  "Autor": ["Dan Brown"],
  "capítulos": [
    { "capitulo": 1, "titulo": null, "longitud": 20 },
    { "capitulo": 2, "titulo": null, "longitud": 25 }
  ]
}
```
 
---
 
## Se Pide
 
Realizar las siguientes operaciones:
 
- **a)** Crear una base de datos denominada `Biblioteca`.
- **b)** Insertar en una colección denominada `Libros` los documentos anteriores.
- **c)** Añadir al array de autores del documento *Python para todos* al autor `Félix Sánchez`.
- **d)** Recuperar de todos los documentos todos los campos, excepto los referidos a editoriales, ISBN, identificador y capítulos.
- **e)** Añadir un campo `leídos` que inicialmente valdrá `0`.
- **f)** Incrementar en tres unidades la cantidad de veces que se ha leído el libro *Historia de Alemania*.
- **g)** En el documento de *El símbolo perdido*, eliminar el campo `editorial`.
- **h)** Añadir un array de `editoriales` al documento de *El símbolo perdido*.
- **i)** Añadir un nuevo capítulo al array de capítulos de *Historia de Alemania*: capítulo 3, título `"La unificación alemana"`, longitud `45`.
- **j)** Actualizar *Python para todos* añadiendo al array `Autor` los valores `Isabel Carrasco` y `Víctor Peña` solo si no están ya presentes.
- **k)** Eliminar el primer elemento del array `Autor` del documento *Python para todos*.
- **l)** Añadir dos veces el valor `Dan Brown` al array `Autor` de *El símbolo perdido*.
- **m)** Eliminar todas las apariciones repetidas de `Dan Brown` en el array `Autor` de *El símbolo perdido*.
- **n)** Actualizar el subdocumento *Prehistoria alemana* incrementando su `longitud` en cuatro.
- **o)** Recuperar todos los documentos de tipo `libro` cuyo autor no sea `Dan Brown`.
- **p)** Recuperar los libros escritos por `Walter House` y `Bryan Reagan` que además tengan un capítulo titulado `"La Edad Media alemana"`.
- **q)** Recuperar todos los documentos cuyo `titulo` sea `Historia de Alemania` **o** cuyo `tipo` sea `Libro`.
- **r)** Sobre *Python para todos*, recuperar del array de `Autor`:
  - Los tres primeros autores.
  - Los últimos tres autores.
  - Tres autores saltándose los dos primeros.
  - Cuatro autores saltándose los cinco últimos.
- **s)** Recuperar los documentos de tipo `libro` cuyo campo `longitud` dentro de `capítulos` sea múltiplo de 25.
---
 
## Solución
 
### a) Crear la base de datos `Biblioteca`
 
```javascript
use Biblioteca
// Switched to db Biblioteca
```
 
### b) Insertar los documentos en la colección `Libros`
 
**Documento 1:**
```javascript
db.Libros.insert({
  "tipo": "libro",
  "titulo": "Python para todos",
  "ISBN": "987-1-2344-5334-8",
  "editorial": "Prentince Hall",
  "Autor": ["Isabel Carrasco", "Carlos Sanz", "Santiago Merino"],
  "capítulos": [
    { "capitulo": 1, "titulo": "Primeros pasos en Python", "longitud": 20 },
    { "capitulo": 2, "titulo": "El entorno Jupyter Notebook", "longitud": 25 }
  ]
})
// WriteResult({ "nInserted": 1 })
```
 
**Documento 2:**
```javascript
db.Libros.insert({
  "tipo": "ebook",
  "titulo": "Historia de Alemania",
  "ISBN": "988-1-3444-6789-9",
  "editorial": "Alianza Editorial",
  "Autor": ["Walter House", "Bryan Reagan"],
  "capítulos": [
    { "capitulo": 1, "titulo": "Prehistoria alemana", "longitud": 40 },
    { "capitulo": 2, "titulo": "La edad media alemana", "longitud": 25 }
  ]
})
// WriteResult({ "nInserted": 1 })
```
 
**Documento 3:**
```javascript
db.Libros.insert({
  "tipo": "libro",
  "titulo": "El símbolo perdido",
  "ISBN": "5678-18-6784-53433-45",
  "editorial": "Planeta",
  "Autor": ["Dan Brown"],
  "capítulos": [
    { "capitulo": 1, "titulo": null, "longitud": 20 },
    { "capitulo": 2, "titulo": null, "longitud": 25 }
  ]
})
// WriteResult({ "nInserted": 1 })
```
 
### c) Añadir autor `Félix Sánchez` a *Python para todos*
 
```javascript
db.Libros.update(
  { "titulo": "Python para todos" },
  { "$addToSet": { "Autor": "Félix Sánchez" } }
)
// WriteResult({ "nMatched": 1, "nUpserted": 0, "nModified": 1 })
```
 
> `$addToSet` añade el valor solo si no existe ya en el array.
 
### d) Recuperar todos los campos excepto `editorial`, `ISBN`, `_id` y `capítulos`
 
```javascript
db.Libros.find(
  {},
  { "editorial": 0, "ISBN": 0, "_id": 0, "capítulos": 0 }
)
```
 
### e) Añadir el campo `leídos` con valor inicial `0` a todos los documentos
 
```javascript
db.Libros.update(
  {},
  { "$set": { "leidos": 0 } },
  { "multi": true }
)
// WriteResult({ "nMatched": 3, "nUpserted": 0, "nModified": 3 })
```
 
### f) Incrementar en 3 el campo `leidos` de *Historia de Alemania*
 
```javascript
db.Libros.update(
  { "titulo": "Historia de Alemania" },
  { "$inc": { "leidos": 3 } }
)
// WriteResult({ "nMatched": 1, "nUpserted": 0, "nModified": 1 })
```
 
### g) Eliminar el campo `editorial` de *El símbolo perdido*
 
```javascript
db.Libros.update(
  { "titulo": "El símbolo perdido" },
  { "$unset": { "editorial": "" } }
)
// WriteResult({ "nMatched": 1, "nUpserted": 0, "nModified": 1 })
```
 
### h) Añadir un array `editoriales` a *El símbolo perdido*
 
```javascript
db.Libros.update(
  { "titulo": "El símbolo perdido" },
  { "$push": { "editoriales": "Booket" } }
)
// WriteResult({ "nMatched": 1, "nUpserted": 0, "nModified": 1 })
```
 
### i) Añadir capítulo 3 al array de capítulos de *Historia de Alemania*
 
```javascript
db.Libros.update(
  { "titulo": "Historia de Alemania" },
  {
    "$push": {
      "capítulos": {
        "capitulo": 3,
        "titulo": "La unificación alemana",
        "longitud": 45
      }
    }
  }
)
// WriteResult({ "nMatched": 1, "nUpserted": 0, "nModified": 1 })
```
 
### j) Añadir `Isabel Carrasco` y `Víctor Peña` a *Python para todos* solo si no existen
 
```javascript
db.Libros.update(
  { "titulo": "Python para todos" },
  {
    "$addToSet": {
      "Autor": { "$each": ["Isabel Carrasco", "Víctor Peña"] }
    }
  }
)
// WriteResult({ "nMatched": 1, "nUpserted": 0, "nModified": 1 })
```
 
> `$addToSet` con `$each` inserta cada valor solo si no está ya presente.

### k) Eliminar el primer elemento del array `Autor` de *Python para todos*
 
```javascript
db.Libros.update(
  { "titulo": "Python para todos" },
  { "$pop": { "Autor": -1 } }
)
// WriteResult({ "nMatched": 1, "nUpserted": 0, "nModified": 1 })
```
 
> `-1` elimina el primer elemento; `1` eliminaría el último.
 
### l) Añadir `Dan Brown` dos veces al array `Autor` de *El símbolo perdido*
 
```javascript
db.Libros.update(
  { "titulo": "El símbolo perdido" },
  {
    "$push": {
      "Autor": { "$each": ["Dan Brown", "Dan Brown"] }
    }
  }
)
// WriteResult({ "nMatched": 1, "nUpserted": 0, "nModified": 1 })
```
 
> A diferencia de `$addToSet`, `$push` permite duplicados.
 
### m) Eliminar todas las apariciones repetidas de `Dan Brown` en *El símbolo perdido*
 
```javascript
db.Libros.update(
  { "titulo": "El símbolo perdido" },
  { "$pullAll": { "Autor": ["Dan Brown"] } }
)
// WriteResult({ "nMatched": 1, "nUpserted": 0, "nModified": 1 })
```
 
> `$pullAll` elimina **todas** las ocurrencias del valor indicado del array.
 
### n) Aumentar en 4 la `longitud` del subdocumento *Prehistoria alemana*
 
```javascript
db.Libros.update(
  { "capítulos.titulo": "Prehistoria alemana" },
  { "$inc": { "capítulos.$.longitud": 4 } }
)
// WriteResult({ "nMatched": 1, "nUpserted": 0, "nModified": 1 })
```
 
> El operador posicional `$` referencia el elemento del array que cumplió la condición del filtro.
 
### o) Recuperar todos los libros cuyo autor no sea `Dan Brown`
 
```javascript
db.Libros.find(
  { "tipo": "libro", "Autor": { "$ne": "Dan Brown" } }
)
```
 
### p) Recuperar los libros de `Walter House` y `Bryan Reagan` con capítulo *"La Edad Media alemana"*
 
```javascript
db.Libros.find({
  "tipo": "libro",
  "Autor": { "$all": ["Walter House", "Bryan Reagan"] },
  "capítulos.titulo": "La Edad Media alemana"
})
```
 
> `$all` exige que **todos** los valores indicados estén presentes en el array.
 
### q) Recuperar documentos cuyo título sea *Historia de Alemania* **o** tipo sea *Libro*
 
```javascript
db.Libros.find({
  "$or": [
    { "titulo": "Historia de Alemania" },
    { "tipo": "libro" }
  ]
})
```
 
### r) Proyecciones sobre el array `Autor` de *Python para todos*
 
**Los tres primeros autores:**
```javascript
db.Libros.find(
  { "titulo": "Python para todos" },
  { "Autor": { "$slice": 3 } }
)
```
 
**Los últimos tres autores:**
```javascript
db.Libros.find(
  { "titulo": "Python para todos" },
  { "Autor": { "$slice": -3 } }
)
```
 
**Tres autores saltándose los dos primeros:**
```javascript
db.Libros.find(
  { "titulo": "Python para todos" },
  { "Autor": { "$slice": [2, 3] } }
)
```
 
**Cuatro autores saltándose los cinco últimos:**
```javascript
db.Libros.find(
  { "titulo": "Python para todos" },
  { "Autor": { "$slice": [-5, 4] } }
)
```
 
> La sintaxis de `$slice` con dos parámetros es `[elementos_a_saltar, elementos_a_devolver]`. Con valor negativo en el primero, se salta desde el final.

### s) Recuperar libros con `longitud` de capítulo múltiplo de 25
 
```javascript
db.Libros.find({
  "tipo": "libro",
  "capítulos.longitud": { "$mod": [25, 0] }
})
```
 
> `$mod: [divisor, resto]` filtra documentos donde el campo sea divisible por `25` con resto `0`.
 
## Resumen de operadores utilizados
 
| Operador | Función |
|---|---|
| `$set` | Establece el valor de un campo |
| `$unset` | Elimina un campo del documento |
| `$inc` | Incrementa el valor numérico de un campo |
| `$push` | Añade un elemento a un array (permite duplicados) |
| `$addToSet` | Añade un elemento a un array solo si no existe |
| `$pop` | Elimina el primer (`-1`) o último (`1`) elemento de un array |
| `$pullAll` | Elimina todas las ocurrencias de un valor en un array |
| `$each` | Permite operar con múltiples valores en `$push` / `$addToSet` |
| `$ne` | Filtro: distinto de |
| `$all` | Filtro: el array contiene todos los valores indicados |
| `$or` | Filtro: al menos una condición es verdadera |
| `$mod` | Filtro: el campo es divisible por un número dado |
| `$slice` | Proyección: devuelve un subconjunto de un array |
| `$` | Operador posicional: referencia el elemento que cumplió el filtro |
