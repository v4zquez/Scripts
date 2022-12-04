#!/bin/bash

typeset -i numero=0
typeset -i numeroGenerado=0 
typeset -i indice=0
typeset -i sumaTotal=0 
typeset -i numeroRepetido=0 
typeset -i vecesRepetido=0 
encontrado=false 

while [ $indice -lt 50 ]; do
      let numeroGenerado=$RANDOM%50 
      let arreglo[$indice]=$numeroGenerado 
      let sumaTotal+=$numeroGenerado 
      let indice+=1 
done

read -p "Numero: " numero 

let indice=0 

for i in ${arreglo[*]}; do
    if (($numero==$i)); then
       echo $indice" -> "$i 
       encontrado=true 
    fi 
    let indice+=1
done

let indice=1 

for j in ${arreglo[*]}; do
    while [ $indice -lt 50 ]; do
          if (($j==${arreglo[$indice]})); then
             let vecesRepetido+=1 
             echo $j" repetido "$vecesRepetido 
          fi 
         
          let indice+=1 
    done
done 

if [ $encontrado = false ]; then
   echo "Elemento no encontrado" 
fi

echo "Total: " $(($sumaTotal/50)) 
