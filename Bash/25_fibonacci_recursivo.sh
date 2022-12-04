#!/bin/bash
#
# 25_fibonacci_recursivo.sh
# Shell-script que muestra los primeros
# 25 digitos de la sucesión Fibonacci

typeset -i n=25 
function fibonacci($n)
{
  if [ $n -eq 0 || $n -eq 1 ]; then
        echo $n
     else
        echo $fibonacci($n-1)+$fibonacci($n-2) 
  fi
} 

fibonacci 
