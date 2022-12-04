#!/bin/bash

# Para leer un fichero es necesario un bucle en la 
# primera línea mas un EOF (End Of File)
# y redireccionar la entrada para ese bucle. 

typeset -i NUM_LINEA=0 
LINEA="algo"

while [ ! -z "$LINEA" ]
do
    read LINEA
    NUM_LINEA=`expr $NUM_LINEA + 1`
    if [ ! -z "$LINEA" ]; then 
       echo "La línea número $NUM_LINEA del fichero es: $LINEA"
    fi
done < /tmp/clientes.txt 

echo "Total líneas: `expr $NUM_LINEA - 1`"
