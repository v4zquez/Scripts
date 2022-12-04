#!/bin/bash
#
# suma_numeros.sh
# Shell script para sumar los números del uno al cien

typeset -i suma=0
typeset -i i=0 
while [ $i -le 100 ] 
do
    let suma=$i+$suma
    let i=1+$i
done
echo $suma 
