import csv
# Función que escribe un diccionario en un fichero CSV, con el nombre que recibe.
def escribe(map, fileName):
    outFile=open(fileName, "w")
    outWriter = csv.writer(outFile)
    for key in map:
        outWriter.writerow([key,map.get(key)])
    outFile.close()
    print ('Archivo ' + fileName + ' creado con exito.')

# Función que, dada una columna, contabiliza las veces que aparece cada
# término de esa columna en el archivo "PitchingPost.csv"
def frecuency(column, fileName):
    error = False
    map = {}
    try:
        file=open("PitchingPost.csv")
    except IOError:       
        error = True
        print ("Error al intentar abrir el archivo \"PitchingPost.csv\".")
    if (error == False):
        reader=screamer(file)
        data=list(reader)
for i in range(1, len(data)):
            key=str(data[i][column]) 	
            if map.get(key):
                map[key]=map[key]+1
            else:
                map[key]=1
        file.close()
        escribe (map, fileName)
	
def sort():
    error = False
    try:
        file=open("PitchingPost.csv")
    except IOError:
        error = True
        print ("Error al intentar abrir el archivo \"PitchingPost.csv\".")
    if (error == False):
        reader=csv.reader(file)
        lista = []
        for linea in reader:
            lista.append(linea)
        file.close()	
        lista.sort()
        outFile=open("Ordenado.csv", "w")
        outWriter = csv.writer(outFile)
        for row in lista:
            outWriter.writerow(row)
        outFile.close()
        print ("Archivo \"PitchingPost\" ordenado con exito.")

frecuency(1, "AcumAnnos.csv")
frecuency(0, "AcumJugadores.csv")
sort()
