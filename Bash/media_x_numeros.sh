#!/bin/bash
#
# media_x_numeros.sh
# Shell-script para calcular la media de x números

typeset -i n=1 
typeset -i i=0 
typeset -i suma=0

while [ $n -ne 0 ]
do
   read -p "Digite un número: " n 
   let suma=$n+$suma 
   let i=1+$i
done
echo "La media es "$(($suma/$i)) 
