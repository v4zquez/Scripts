#!/bin/bash
#
# tabla_multiplicar.sh
# Shell script que muestra la tabla de 
# multiplicar de 1 a 10 

typeset -i n=1 
typeset -i i=1
typeset -i j=1

while [ $i -le 10 ]
do
    while [ $j -le 10 ]
    do
       n=$i*$j
       if [ $j -le 9 ]; then
               if [ $i -le 9 ]; then
                       if [ $n -le 9 ]; then
                             echo -e $j"*"$i"="$n"   \c" 
                          else
                             echo -e $j"*"$i"="$n"  \c" 
                       fi
                    else
                       echo -e $j"*"$i"="$n" \c" 
               fi 
               else
                  echo -e $j"*"$i"="$n
       fi
       let j=1+$j 
    done
    let i=1+$i
    let j=1
done 

# ALGORITMO
# INICIO 
#      Variables -> Entero -> n<-1 
#                          -> i<-1
#                          -> j<-1
#      MIENTRAS $i<=10 HACER
#               MIENTRAS $j<=10 HACER
#                        n<-$i*$j
#                        SI $j<=9 ENTONCES
#                               SI $i<=9 ENTONCES
#                                  SI $n<=9 ENTONCES
#                                        Imprimir $j"*"$i"="$n"   \c"
#                                  SINO
#                                        Imprimir $j"*"$i"="$n"  \c" 
#                                  FIN_SI
#                               SINO
#                                  Imprimir $j"*"$i"="$n" \c"
#                               FIN_SI
#                         SINO 
#                             Imprimir $j"*"$i"="$n 
#                         FIN_SI 
#                         j<-1+$j 
#               FIN_MIENTRAS 
#               i<-1+$i
#               j<-1
#      FIN_MIENTRAS
# FIN 
