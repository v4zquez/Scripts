#!/bin/bash 
#
# main.sh
# Autor: Albin Vázquez Solano - 20 noviembre 2016
# Script encargado de interactuar con el usuario 

# crear comunicación entre script controlador.sh y script main.sh.
source /home/albin/Documents/ficheros/administrador_ficheros/controlador.sh 

while true 
do 
    LIMPIAR_PANTALLA 
    MENU_PRINCIPAL 
    read -n 1 OPCION 
    LIMPIAR_PANTALLA 
    case $OPCION in
         0) SALIR;; 
         1) ADMINISTRADOR; 
            while true 
            do
               read ENTRADA 
               ADMINISTRADOR $ENTRADA 
	    done;; 
         2) INFORMACION;;
         *) MENSAJE_ERROR;;
    esac
done
