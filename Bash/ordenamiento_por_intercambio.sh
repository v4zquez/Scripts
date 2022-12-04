#!/bin/bash
#
# ordenamiento_por_intercambio.sh
# Shell-script que permite ordenar x cantidad de números contenidos en un  
# arreglo mediante el método de intercambio o también llamado método burbuja. 
# El método consiste en:
# Recorrer todo el arreglo, intercambiando todo par de elementos consecutivos
# dejando de primero el menor. Al final de la iteración el mayor elemento
# del arreglo queda ordenado. Cada iteración se repite hasta que todos los 
# elementos del arreglo queden ordenados, de atrás para adelante. 

typeset -i n=1
typeset -i i=0
typeset -i j=0
typeset -i l=0 
typeset -i temp=0
while [ $n -ne 0 ]
do
   read -p "Numero: " n
   if [ $n -ne 0 ]; then
      let elementos[$i]=$n 
      let i=1+$i 
   fi
done
while [ $j -lt $i ]
do
   let k=$j+1
   while [ $k -lt $i ]
   do 
      if [ ${elementos[$j]} -lt ${elementos[$k]} ]; then 
         let temp=${elementos[$j]}
         let elementos[$j]=${elementos[$k]}
         let elementos[$k]=$temp 
      fi 
      let k=1+$k 
   done
   let j=1+$j 
done
for l in ${elementos[*]}
do
   echo -e $l 
done 
