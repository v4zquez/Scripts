#!/bin/bash

# Función que lista los ejecutables de un directorio
function ListaEjecutables 
{
         ls -1 $1 | while read fichero
         do
             path_fichero="$1/$fichero"
             if [ -x $path_fichero ]; then
                echo $path_fichero
             fi
         done
}

ListaEjecutables
