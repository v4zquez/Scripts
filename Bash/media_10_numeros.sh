#!/bin/bash
#
# media_10_numeros.sh
# Shell-script para calcular la media de 10 números

typeset -i n=0 
typeset -i i=1 
typeset -i suma=0

while [ $i -le 10 ]
do
   read -p "Digite un número: " n 
   let suma=$n+$suma 
   let i=1+$i
done
echo "La media es "$(($suma/10)) 
