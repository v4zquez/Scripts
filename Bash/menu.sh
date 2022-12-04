#!/bin/bash
#
# menu.sh
# menu del tipo "desea salir(s/n)" y el
# programa no termina hasta que se teclee "s"

opcion="n"
while [ $opcion != "s" ] 
do
   read -p "¿Desea salir (s/n)?" opcion 
done
