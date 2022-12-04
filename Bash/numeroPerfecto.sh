#!/bin/bash

if [ $# -lt 1 ]; then
   echo "$0 [número]" 
   exit 1
fi

typeset -i n=$1
typeset -i i=1
typeset -i suma=0 
typeset -i resultado=0

while [ $i -lt $n ]; do
      let resultado=$n%$i
      if [ $resultado -eq 0 ]; then  
         let suma=$i+$suma 
      fi
      let i=1+$i 
done

if [ $suma -eq $n ]; then
   printf "%i es un número perfecto\n" $n 
else
   printf "%i no es un número perfecto\n" $n 
fi
exit 0
