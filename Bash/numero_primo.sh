#!/bin/bash
#
# numero_primo.sh
# Shell script que indica si un número es primo o no. 

read -p "Numero:" numero 

# variables
typeset -i contador=1
typeset -i divisores=0
typeset -i numero_=0 
typeset -i suma=0

let numero_=$numero+1

while test $contador -le $numero_
do
  let operacion="$numero % $contador"
  if [ $operacion -eq 0 ]; then
     let divisores+=1
     let suma+=$contador
  fi
  let contador+=1
done

let final=$numero+1
if [ $suma -eq $final ]; then
      echo "Es un número primo" 
   else
      echo "No es un número primo" 
fi
exit 0

# ALGORITMO
# Dato de entrada -> Entero: numero
# Leer numero
# Variables -> Entero: 
#                   -> contador<-1
#                   -> divisores<-0
#                   -> suma<-0
#                   -> numero_<-0 
# numero_<-$numero+1
# MIENTRAS $contador<=$numero_ HACER
#          operacion<-$numero%$contador
#          SI $operacion=0 ENTONCES
#             divisores<-1+$divisores
#             suma<-$contador+$suma
#          FIN_SI
#          contador<-1+$contador
# FIN_MIENTRAS
# final<-1+$numero
# SI $suma=$final ENTONCES 
#       Imprimir "Es un número primo" 
#    SINO
#       Imprimir "No es un número primo"
# FIN_SI 
