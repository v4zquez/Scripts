#!/bin/bash
#
# factorial.sh
# Shell-script para calcular el factorial de un número cualquiera. 
# Factorial de un número es multiplicar dicho número por todos sus anteriores hasta llegar a 1. 

typeset -i factorial=1
read -p "Digite un número: " numero
typeset -i i=$numero 
while [ $i -ge 1 ]
do
   factorial=$i*$factorial
   let i=$i-1 
done
echo $numero"!="$factorial 
