#!/bin/bash
#
# tabla.sh
# Shell script que muestra los números de 1 a 100 en 
# una tabla de 10 x 10

typeset -i numero=1 
typeset -i i=1
typeset -i j=1

while [ $i -le 10 ]
do
    while [ $j -le 10 ]
    do
       if [ $j -le 9 ]; then
             if [ $numero -le 10 ]; then
                   echo -e $numero"  \c"
                else
                   echo -e $numero" \c" 
             fi 
          else
             echo -e $numero
       fi
       let numero=1+$numero
       let j=1+$j 
    done
    let i=1+$i
    let j=1
done 

# ALGORITMO
# INICIO 
#      Variables -> Entero -> numero<-1 
#                          -> i<-1
#                          -> j<-1
#      MIENTRAS $i<=10 HACER
#               MIENTRAS $j<=10 HACER
#                        SI $j<=9 ENTONCES
#                              SI $numero<=10 ENTONCES
#                                   Imprimir $numero"  \c" 
#                                 SINO
#                                   Imprimir $numero" \c"
#                              FIN_SI
#                           SINO
#                              Imprimir $numero
#                        FIN_SI
#                        numero<-1+$numero
#                        j<-1+$j
#               FIN_MIENTRAS
#               i<-1+$i
#               j<-1
#      FIN_MIENTRAS
# FIN
