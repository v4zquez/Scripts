#!/bin/bash
#
# rango_numeros_pares.sh
# Shell script que muestra los números pares contenidos dentro de un 
# rango de dos números dados

read -p "Primer Número: " num1
read -p "Segundo Número: " num2

if [ $num1 -ge $num2 ]; then 
      echo "El primer número debe ser menor que el segundo número" 
   else
      typeset -i i=$num1
      typeset -i j=0 
      while [ $i -le $num2 ]
      do
         let operacion="$i % 2" 
         if [ $operacion -eq 0 ]; then 
            if [ $j -lt 10 ]; then 
                  echo -e $i"-\c" 
               else
                  echo -e $i 
                  let j=0
            fi
            let j=1+$j 
         fi
         let i=1+$i 
      done 
fi
