#!/bin/bash
#
# tojpg.sh 
# Script que convierte ficheros de imagen al formato .jpg

for fichero in "$@"
do
    fichero_ppm=${fichero%.*}.ppm
    case $fichero in
         *.jpg) exit 0;;
         *.tga) tgatoppm $fichero > $fichero_ppm;;
         *.xpm) xpmtoppm $fichero > $fichero_ppm;;
         *.pcx) pcxtoppm $fichero > $fichero_ppm;;
	 *.tif) tifftopnm $fichero > $fichero_ppm;;
	 *.gif) figtoppm $fichero > $fichero_ppm;;
	 *.pnm|*.ppm) ;;
	 *) echo "Formato .${fichero##*.} no soportado"
	 exit 1;;
    esac
    fichero_salida=${fichero_ppm%.ppm}.jpg
    pnmtojpeg $fichero_ppm > $fichero_salida
    if ! [ $fichero = $fichero_ppm ]; then
       rm $fichero_ppm
    fi
done
