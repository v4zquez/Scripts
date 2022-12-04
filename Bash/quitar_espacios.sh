	# Quitar los espacios de nombres de ficheros
        directorio=$1
  
        for fichero in $directorio* 
        do
           # sed traduce el primer caracter por el segundo 
           nuevo_fichero=`echo $fichero | sed 's/ /_/g'`
           if [ "$nuevo_fichero" != "$fichero" ]; then
              # renombrar fichero 
              mv "$fichero" $nuevo_fichero 
           fi 
        done 
