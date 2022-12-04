FILE=$1 
if test -b $FILE
   then echo $FILE 'Es un dispositivo de bloques'
   elif test -c $FILE
        then echo $FILE 'Es un dispositivo especial de caracteres'
   elif test -d $FILE
        then echo $FILE 'Es un directorio'
   elif test -f $FILE
        then echo $FILE 'Es un fichero regular (ordinario)'
   elif test -L $FILE
        then echo $FILE 'Es un Link simbólico'
   elif test -p $FILE
        then echo $FILE 'Es un pipe con nombre'
   elif test -S $FILE
        then echo $FILE 'Es un Socket (dispositivo de comunicaciones)'
   elif test -e $FILE
        then echo $FILE 'Existe pero se desconoce que tipo de fichero es'
   else echo $FILE 'No existe o no es accesible'
fi 
