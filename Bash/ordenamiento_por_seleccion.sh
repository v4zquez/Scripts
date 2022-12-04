#!/bin/bash
#
# ordenamiento_por_seleccion.sh
# Shell-script que permite ordenar x cantidad de números contenidos en un  
# arreglo mediante el método de selección. 
# El método consiste en:
# El arreglo se divide en dos partes: la parte ordenada y la que está sin
# ordenar. Se busca el menor elemento en la parte no ordenada, ese elemento
# se intercambia por el primero de la parte no ordenada. Ese elemento ya 
# pertenece a la parte ordenada.
 
typeset -i n=1
typeset -i ind=0
typeset -i i=0
typeset -i j=0
typeset -i menor=0
typeset -i cual=0 
typeset -i temp=0 
while [ $n -ne 0 ]
do
   read -p "Numero: " n
   if [ $n -ne 0 ]; then
      let arreglo[$ind]=$n 
      let ind=1+$ind 
   fi
done

while [ $i -lt $ind ]
do
   let menor=${arreglo[$i]} 
   let cual=$i
   let j=1+$j 
   while [ $j -le $ind ]
   do
      if [ ${arreglo[$j]} -lt $menor ]; then
         let menor=${arreglo[$j]}
         let cual=$j 
      fi
      let j=1+$j
   done
   let temp=${arreglo[$i]}
   let arreglo[$i]=$menor
   let arreglo[$cual]=$temp
   let i=1+$i 
done

for k in ${arreglo[*]}
do
   echo -e $k 
done 
