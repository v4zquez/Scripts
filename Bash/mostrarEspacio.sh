#!/bin/bash
#
# mostrarEspacio.sh
# Script que muestra el espacio ocupado por cada subdirectorio de un directorio.
# El comando du muestra el tamaño ocupado por cada subdirectorio de un directorio. 

# Comprueba argumento
if [ -z $1 ]; then
   echo "Use: ocupa <directorio>"
   exit 1
fi

# Obtiene los directorios y su tamaño en una lista  
lista=$(du -k $1)

# Ya que por defecto este delimitador es el espacio, y no se desea que el
# espacio se considere cambio de palabra, sino que lo sea el
# cambio de línea.
IFS='
'

for fila in $lista
do
    dir=$(echo $fila|cut -f 2) # obtener columna 2 
    let kb=$(echo $fila|cut -f 1) # obtener columna 1 
    let b=1024*$kb
    let mb=$kb/1024
    echo "$mb MB,    $kb KB,   $b B   $dir"
done 
