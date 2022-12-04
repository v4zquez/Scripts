#!/bin/bash
#
# asteriscos.sh
# Shell script que muestra un determinado número de asteriscos

typeset -i i=1 
typeset -i j=1
read -p "Número: " numero

while [ $i -le $numero ] 
do
   while [ $j -le $i ]
   do
       echo -e "*\c"
       let j=1+$j
   done
   echo -e "" 
   let i=1+$i
   let j=1 
done

# ALGORITMO
# INICIO
#   Variables -> Entero: -> i<-1
#                        -> j<-1
#   Imprimir "Número: "
#   Leer numero
#   MIENTRAS $i<=$numero HACER
#          MIENTRAS $j<=$i HACER
#                   Imprimir "*\c"
#                   j<-1+$j
#          FIN_MIENTRAS
#          Imprimir ""
#          i<-1+$i
#          j<-1
#   FIN_MIENTRAS 
# FIN
