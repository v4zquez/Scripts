#!/bin/bash

# Program to print the value of parameters passed to the bash script 

echo "Number of parameters: $#"

lastId=$#
parametersNumber=${@:lastId}

if [[ $# -le 4 ]]; then
    echo "The number of parameters must be greater than 4"
    exit 1
fi

if [[ $parametersNumber -gt $# ]]; then
    echo "The required quantity exceeds the number of parameters"
    exit 2
fi

if [[ $# -eq $parametersNumber ]]; then
    let parametersNumber=$parametersNumber-1
fi

declare -i i=1

while [[ $i -le $parametersNumber ]]; do
    var=""; var="$"; var+="$i"
    echo -n "Value of parameter $i is: "
    outputMessage=$(eval $var 2>&1) # The eval statement tells the shell to take eval's arguments as commands and 
                                    # run them through the command-line
    echo $outputMessage | awk '{print $4}' | tr -d ":" 
    let i=1+$i
done
