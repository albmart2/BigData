#!/bin/bash
while true
do
	clear
	echo "
	Ver directorio actual.......[1]
	Copiar archivos.............[2]
	Editar archivos.............[3]
	Imprimir archivos...........[4]
	Salir del menú..............[5]"
	read i
	case $i in 
		1) ls -l|more;read z;;
		2) echo "Introduzca [desde] [hasta]"; 
		read desde hasta; 
		cp $desde $hasta; 
		echo "Archivo copiado"; 
		read z;;
		3) echo "Introduzca el nombre del archivo a editar";
		read archivo;
		vi $archivo;;
		4) echo "Introduzca el nombre del archivo a imprimir";
		read archivo;
		lpr $archivo;;
		5) clear;
		break;;
	esac
done

