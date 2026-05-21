# Caso práctico

## Enunciado
El objetivo es poner en práctica los conocimientos adquiridos sobre la herramienta para resolver el ejercicio.

## Datos
Partiendo de las letras de las siguientes canciones:

```text
Nine Inch Nails, "March of the Pigs"

step right up march push
crawl right up on your knees
please greed feed (no time to hesitate)
I want a little bit I want a piece of it I think he's losing it
I want to watch it come down
don't like the look of it don't like the taste of it don't like the smell of it
I want to watch it come down
all the pigs are all lined up
I give you all that you want
take the skin and peel it back
now doesn't that make you feel better?
shove it up inside surprise! lies
stains like the blood on your teeth
bite chew suck away the tender parts
I want to break it up I want to smash it up I want to fuck it up
I want to watch it come down
maybe afraid of it let's discredit it let's pick away at it
I want to watch it come down
now doesn't that make you feel better?
the pigs have won tonight
now they can all sleep soundly
and everything is all right
```

```text
Pink Floyd, "Pigs (Three Different Ones)"

Big man, pig man, ha ha, charade you are
You well heeled big wheel, ha ha, charade you are
And when your hand is on your heart
You're nearly a good laugh
Almost a joker With your head down in the pig bin
Saying "keep on digging" Pig stain on your fat chin
What do you hope to find?
When you're down in the pig mine
You're nearly a laugh You're nearly a laugh
But you're really a cry.
Bus stop rat bag, ha ha, charade you are
You fucked up old hag, ha ha, charade you are
You radiate cold shafts of broken glass
You're nearly a good laugh Almost worth a quick grin
You like the feel of steel You're hot stuff with a hat pin
And good fun with a hand gun
You're nearly a laugh You're nearly a laugh
But you're really a cry.
Hey you Whitehouse, ha ha, charade you are
You house proud town mouse, ha ha, charade you are
You're trying to keep our feelings off the street
You're nearly a real treat All tight lips and cold feet
And do you feel abused? .....!.....!.....!.....!
You gotta stem the evil tide
And keep it all on the inside
Mary you're nearly a treat Mary you're nearly a treat
But you're really a cry.
```

```text
Dave Matthews Band, "Pig"

Isn't it strange
How we move our lives for another day
Like skipping a beat
What if a great wave should wash us all away
Just thinking out loud
Don't mean to dwell on this dying thing
But looking at blood
It's alive right now
Deep and sweet within
Pouring through our veins
Intoxicate moving wine to tears
Drinking it deep
Then an evening spent dancing
It's you and me
This love will open our world
From the dark side we can see a glow of something bright
There's much more than we see here
Don't burn the day away
Is this not enough
This blessed sip of life
Is it not enough
Staring down at the ground
Oh then complain and pray more from above
Greedy little pig
Stop just watch your world trickle away
Oh it's your problem now
It'll all be dead and gone in a few short years
Just love will open our eyes
Just love will put the hope in our minds
Much more than we could ever know
Don't burn the day away
Come sister my brother
Shake up your bones shake up your feet
I'm saying open up
And let the rain come pouring in
Wash out this tired notion
That the best is yet to come
But while you're dancing on the ground
Don't think of when you're gone
Love love what more is there
We need the light of love in here
Don't beat your head
Dry your eyes
Let the love in there
There are bad times
But that's ok
Just look for love in it
Don't burn the day away
Look
Here are we
On this starry night staring into space
And I must say
I feel as small as dust
Lying down here
What point could there be troubling
Head down wondering what will become of me
Why concern we cannot see
But no reason to abandon it
Time is short but that's all right
Maybe I'll go in the middle of the night
Take your hands from your eyes, my love
Everything must end some time
Don't burn the day away
Come sister my brother
Shake up your bones shake up your feet
I'm saying open up
And let the rain come flooding in
Wash out this tired notion
That the best is yet to come
But while you're dancing on the ground
Don't think of when you're gone
Love love what more is there
We need the light of love in here
Don't beat your head
Dry your eyes
Let the love in there
There are bad times
But that's ok
Just look for love in it
```

## Se pide
1. Crear ficheros de texto en la máquina Ubuntu.
2. Subir los ficheros a HDFS.
3. Ejecutar un job wordcounty resolver las siguientes cuestiones:
    1. Acceder al “jobhistory” e indicar el valor de Status del job con el nombre "word count".
    2. ¿Qué palabra se repite más veces?
    3. ¿Qué palabra se repite seis veces?
    4. ¿Cuántas veces aparece la palabra “eyes”?

## Solución

1. Crear ficheros de texto en la máquina Ubuntu:

   Crear un directorio nuevo para la práctica 1:

   ```bash
   mkdir hadoop/practica1
   ```

   Crear los ficheros con la letra de las canciones:

   ```bash
   cd hadoop/practica1
   sudo nano cancion1.txt
   sudo nano cancion2.txt
   sudo nano cancion3.txt
   ```

   <img width="732" height="493" alt="image" src="https://github.com/user-attachments/assets/e540f25c-e454-4022-abb0-9fee49f80f9d" />

   <img width="727" height="534" alt="image" src="https://github.com/user-attachments/assets/b7967def-ae14-4aa5-a470-3be78c350437" />

   <img width="668" height="526" alt="image" src="https://github.com/user-attachments/assets/ed436dfc-da2d-4055-a180-b5215afd8cd1" />

2. Subir los ficheros a HDFS.

   Añadir los ficheros a HDFS:

   ```bash
   hdfs dfs -mkdir /practica1
    hdfs dfs -put *.txt /practica1
   ```

   Comprobar si se han añadido correctamente:

   ```bash
   hdfs dfs -ls /practica1
   ```

3. Ejecutar un <i>wordcount</i> y resolver las siguientes cuestiones:

   Ejecutar <i>wordcount</i>:

   ```bash
   hadoop jar /home/bigdata/hadoop/share/hadoop/mapreduce/hadoop-mapreduceexamples-3.3.1.jar wordcount /practica1 /outcanciones
   ```

   1. Acceder al “jobhistory” e indicar el valor de Status del job con el nombre "word count".

      Acceder al “jobhistoy” (es necesario que antes se haya levantado el demonio MrJobHistory) “http://localhost:8088”.

      <img width="1680" height="397" alt="image" src="https://github.com/user-attachments/assets/39f17b7a-d80e-41f1-aed2-9ccdede6ca3d" />

      Se puede comprobar que el Status es exitoso.

      <img width="1452" height="753" alt="image" src="https://github.com/user-attachments/assets/44097afa-0602-4752-b4b5-4e4e87dce0e4" />

   2. ¿Qué palabra se repite más veces?

      Revisar la salida:

      ```bash
      hdfs dfs -ls -R /outcanciones
      hdfs dfs -cat /outcanciones/part-r-00000
      ```

      Para obtener la palabra que más se repite, ordenar la salida por la segunda columna numérica en orden descendente y quedarse con la primera:

      ```bash
      hdfs dfs -cat /outcanciones/* | sort -k2nr | head -1
      ```

      El resultado es la palabra “<b>the</b>”, con <b>34 apariciones</b>.

   3. ¿Qué palabra se repite seis veces?

      Para obtener las palabras que se repiten seis veces, usar el comando grep:

      ```bash
      hdfs dfs -cat /outcanciones/* | grep '6'
      ```

      Se obtienen las palabras: “You”, “charade”, “ha”, “laugh”, “our” y “we”.

      Nota: al ser casesensitive, aparece también “16”.

   4. ¿Cuántas veces aparece la palabra “eyes”?

      Se obtienen las veces que aparece la palabra “eyes” con el siguiente comando:
  
      ```bash
      hdfs dfs -cat /outcanciones/* | grep '\<eyes.*\>'
      ```
      
      Y se observa que aparece cuatro veces.
