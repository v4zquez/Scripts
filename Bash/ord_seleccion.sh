#!/bin/bash

typeset -i cont=0 

while [ $cont -lt 10 ]; do
      read -p "$cont: " numero
      if [ $numero ]; then #validar que elemento ingresado no sea nulo 
         let arreglo[$cont]=$numero 
         let cont++
      fi
done
echo ${arreglo[@]} 

for ((i=0; i<10; i++)); do 
    let menor=${arreglo[$i]}
    let cual=$i
    for ((j=1+$i; j<10; j++)); do
        if [ ${arreglo[$j]} -lt $menor ]; then
           let menor=${arreglo[$j]} 
           let cual=$j
        fi 
    done 
    let temp=${arreglo[$i]}
    let arreglo[$i]=$menor
    let arreglo[$cual]=$temp 
done 
echo ${arreglo[@]}
