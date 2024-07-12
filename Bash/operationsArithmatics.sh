#!/bin/bash

variable=$1
num1=$2
num2=$3

E_BADARGS=85

if [[ "$#" -lt 3 ]] || [[ "$#" -gt 3 ]]; then
    echo "Usage: $(basename $0) number1 number2 number3"
    exit $E_BADARGS
fi

sum=$(awk -v var1=$num1 -v var2=$num2 'function sum(num1, num2)
                                       {return num1 + num2}

				       function main(num1, num2)
				       {print sum(num1, num2)}

				       BEGIN {main(var1, var2)}')
				      
result=$(awk -v var1=$sum -v var2=$variable 'function find_max(num1, num2)
                                             {
			                         if (num1 > num2) return 0 
						 else if (num1 < num2) return 1
						 else return 2
					     } 
			                    
				             function main(num1, num2)
				             {print find_max(num1, num2)}
					 
					     BEGIN {main(var1, var2)}')


if [[ $result -eq 0 ]]; then
    echo "($num1 + $num2 = $sum) > $variable"
fi

if [[ $result -eq 1 ]]; then
    echo "($num1 + $num2 = $suam) < $variable"
fi

if [[ $result -eq 2 ]]; then
    echo "($num1 + $num2 = $sum) = $variable"
fi

exit 0
