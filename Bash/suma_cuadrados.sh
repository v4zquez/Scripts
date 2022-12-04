#!/bin/bash
# 
# suma_cuadrados.sh
# Shell-script para sumar los cuadrados de los primeros
# 100 números

typeset -i suma=0
typeset -i i=0 
while [ $i -le 100 ] 
do
   let suma=($i*$i)+$suma 
   let i=1+$i 
done
echo "Total "$suma
