#!/bin/bash

read -p "Introduce directorio a buscar: " directorio
read -p "Nombre de fichero a buscar:  " nombre
if [ ! -d $directorio ]; then 
   echo "$directorio no existe"
else
   find $directorio -name "*.$nombre" ls -l 
fi
