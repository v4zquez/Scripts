#!/bin/bash
#
# base.sh
# Autor: Albin Vázquez Solano - 20 noviembre 2016
# Script que permite al programa interactuar con bash

function QUITAR_ESPACIOS_BASE()
{
	# Quitar los espacios de nombres de ficheros
        local DIRECTORIO
        local FICHERO
        local NUEVO_FICHERO
 
        DIRECTORIO=$1
 
        for FICHERO in $DIRECTORIO* 
        do
           # sed traduce el primer caracter por el segundo 
           NUEVO_FICHERO=`echo $FICHERO | sed 's/ /_/g'`
           if [ "$NUEVO_FICHERO" != "$FICHERO" ]; then
              # renombrar fichero 
              mv "$FICHERO" $NUEVO_FICHERO 
           fi
        done 
} 

function CTRL_C_BASE()
{
	# Invocar función salir
        SALIR_BASE
} 

function EXTRAER_CARACTER_BASE()
{
        # Seleccionar caracteres indicados 
	local CADENA 
        local N_CARACTER_INICIO
        local N_CARACTER_FINAL 
	
        CADENA=$1 
        N_CARACTER_INICIO=$2
        N_CARACTER_FINAL=$3
 
        # 'cut' divide la CADENA, seleccionando
        # solo los caracteres indicados y desechando 
        # el resto. 
        echo $CADENA | cut -c$N_CARACTER_INICIO-$N_CARACTER_FINAL 
}

function IMPRIMIR_BASE()
{
        # Imprimir lo necesario en pantalla 
        local MENSAJE

        MENSAJE=$1 
	echo -e $MENSAJE 
} 

function INFORMACION_BASE()
{ 
        # Mostrar información sobre el uso del programa
        # 'cat' muestra en pantalla el fichero pasado como argumento
        # 'less' programa de paginado y búsqueda
        cat /home/albin/Documents/ficheros/administrador_ficheros/informacion.txt | less 
        clear
}

function LIMPIAR_BASE()
{ 
        # Limpiar pantalla
	clear 
} 

function LISTAR_BASE()
{
        # Listar directorio 
        local DIRECTORIO
        
        DIRECTORIO=$1 
        # 'ls' muestra en pantalla lo contenido 
        # en dicho directorio. 
	ls --color=auto $DIRECTORIO 
}

function MENSAJE_ERROR_BASE()
{
        # Mensaje mostrado cuando el usuario seleccione
        # una opcion no disponible en el menu principal. 
        local TECLA

        echo -e "\t\t\t\t\t\t\t############################"
        echo -e "\t\t\t\t\t\t\t#      Op. Incorrecta      #"
        echo -e "\t\t\t\t\t\t\t############################"
        echo -e "\t\t\t\t\t\t\t### <ENTER> para continuar \c"
        read -n 1 TECLA 
}

function MENU_PRINCIPAL_BASE()
{
        # Menu con la opciones disponibles para el usuario 

        echo -e "\t\t\t\t\t\t\t############################"
        echo -e "\t\t\t\t\t\t\t# 1) Iniciar               #"      
        echo -e "\t\t\t\t\t\t\t# 2) Informacion           #"      
        echo -e "\t\t\t\t\t\t\t# 0) Salir                 #"      
        echo -e "\t\t\t\t\t\t\t############################" 
        echo -e "\t\t\t\t\t\t\t################### Opción \c" 
}

function ADMINISTRAR_FICHERO_BASE()
{
        # administrar fichero 
        
        local RUTA_INICIO
        local RUTA_DESTINO
        local CADENA
        local OPCION
        local COMANDO

        # recibir parametros 
        RUTA_INICIO=$1
        RUTA_DESTINO=$2 
        CADENA=$3 
        OPCION=$4
        COMANDO=$5
        
        QUITAR_ESPACIOS_BASE $RUTA_INICIO 

        if [ $OPCION = true ]; then
               # Dividir CADENA en elementos para moverlos 
               # sed traduce el primer caracter por el segundo 
               declare -a ELEMENTOS=($(echo $CADENA | sed 's/,/ /g')) 
      
               IMPRIMIR_BASE ""
               for FICHERO in ${ELEMENTOS[*]} 
               do
                  # cambiar de directorio 
                  $COMANDO $RUTA_INICIO$FICHERO $RUTA_DESTINO 2> /dev/null 
                  # mostrar proceso realizado
                  IMPRIMIR_BASE "Fichero $RUTA_INICIO$FICHERO ha sido procesado a $RUTA_DESTINO" 
               done
            else
               TIPO_FICHERO=$CADENA 
               if [ $TIPO_FICHERO = "todo" ]; then
                    LISTAR_FICHEROS=$RUTA_INICIO"*" 
                 else
                    LISTAR_FICHEROS=$RUTA_INICIO"*"$TIPO_FICHERO 
               fi 

               IMPRIMIR_BASE ""
               for FICHERO in $LISTAR_FICHEROS 
               do
                   $COMANDO $FICHERO $RUTA_DESTINO 2> /dev/null
                   # mostrar proceso realizado
                   IMPRIMIR_BASE "Fichero $FICHERO ha sido procesado a $RUTA_DESTINO" 
               done
        fi 
        PAUSA_PROCESO_BASE 
        clear
}

function PAUSA_BASE_BASE()
{
        # Mensaje mostrado cuando el usuario decida pausar el programa 
        local TECLA 

        echo -e "\t\t\t\t\t\t\t############################"
        echo -e "\t\t\t\t\t\t\t#           PAUSA          #"
        echo -e "\t\t\t\t\t\t\t############################"
        echo -e "\t\t\t\t\t\t\t### <ENTER> para continuar \c"
        read -n 1 TECLA 
}

function PAUSA_PROCESO_BASE()
{
        # Mensaje mostrado cuando algún proceso haya finalizado 
        local TECLA 

        echo -e "\nPresione <ENTER> para continuar \c"
        read -n 1 TECLA 
}

function RENOMBRAR_DIRECTORIO_BASE()
{
        # Modificar nombre de DIRECTORIO
        local UBICACION
        local NOMBRE_DIRECTORIO
        local A
        local B

        UBICACION=$1
        NOMBRE_DIRECTORIO=$2 
        # sed traduce el primer caracter por el segundo 
        A=`echo $NOMBRE_DIRECTORIO | sed 's/_/ /g'` 
        B=`echo $A | sed 's/ /_/g'` 
        # 'mv' cambia nombre de DIRECTORIO 
        mv $UBICACION"$A" $UBICACION$b | echo $B 
}

function VALIDAR_TIPO_FICHERO_BASE()
{
        # Tipo de fichero ingresado por el usuario debe coincidir con algun elemento 
        # del arreglo que contiene los tipos de ficheros permitidos.  
        local TP_FICHERO
        local TP 

        TP_FICHERO=$1 
	typeset -i LOCALIZAR_TIPO_FICHERO=0 
        declare -a FICHEROS_PERMITIDOS=('.deb' '.doc' '.gif' '.iso' '.jpg' '.jpeg' '.mp3' '.mp4' '.pdf' '.png' '.rar' '.sh' '.tar' '.txt' '.zip') 
        # comprobar que parametro no sea nulo
        if [ $TP_FICHERO ]; then      
             if [ $TP_FICHERO = ".todo" ]; then 
                     echo "todo"
                  else
                     for TP in ${FICHEROS_PERMITIDOS[*]}
                     do
                        # buscar parametro ingresado en arreglo 
                        if [ $TP_FICHERO = $TP ]; then 
                           let LOCALIZAR_TIPO_FICHERO+=1 
                        fi
                     done
      
                     # parametro no localizado en arreglo
                     if [ $LOCALIZAR_TIPO_FICHERO -eq 0 ]; then 
                          echo "error_fichero"
                        else
                          echo $TP_FICHERO 
                     fi
             fi
           else
              echo "vacio" 
       fi
} 

function SALIR_BASE()
{
        # Finalizar programa 
	exit 0 
}
