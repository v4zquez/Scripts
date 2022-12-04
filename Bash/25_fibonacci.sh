#!/bin/bash
#
# 25_fibonacci.sh
# Shell-script que muestra los primeros
# 25 digitos de la sucesión Fibonacci

typeset -i a=0
typeset -i b=0
typeset -i i=0 

while [ $i -le 25 ]
do
   if [ $i -le 1 ]; then
         echo $i"-> "$i
         let b=$a
         let a=$i 
      else
         let c=$a+$b
         let b=$a
         let a=$c
         echo $i"-> "$c 
   fi 
   let i=1+$i
done
