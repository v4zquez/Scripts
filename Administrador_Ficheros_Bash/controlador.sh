#!/bin/bash
# 
# controlador.sh
# Autor: Albin Vázquez Solano - 20 noviembre 2016 
# Script encargado de procesar todas las peticiones por parte del usuario 

# crear comunicación entre script base.sh y script controlador.sh.  
# controlador.sh podrá usar todas las funciones que contiene base.sh 
source /home/albin/Documents/ficheros/administrador_ficheros/base.sh 

# controlador.sh toma control de todo lo contenido en base.sh 

# Atrapar ctrl-c y llamar a ctrl_c()
trap CTRL_C_BASE INT 

INFORMACION()
{
	INFORMACION_BASE 
} 

LIMPIAR_PANTALLA()
{
        LIMPIAR_BASE 
} 

MENSAJE_ERROR()
{
	MENSAJE_ERROR_BASE 
} 

MENU_PRINCIPAL()
{
        MENU_PRINCIPAL_BASE 
}

PAUSA()
{
	PAUSA_BASE 
} 

SALIR()
{
	SALIR_BASE 
}

# funcion encargada de realizar todas la tareas correspondientes al programa principal 
# indica el inicio de la funcion ADMINISTRADOR 
INICIO=true 
# indica la posicion del vector UBICACIONES
typeset -i IND=0 
ADMINISTRADOR()
{
    LIMPIAR_PANTALLA  
    if [ $INICIO = true ]; then 
           # arreglo para guardar las distintas ubicaciones 
           declare -a UBICACIONES[$IND]=~/ 
           # variable que toma la primera ubicacion 
           UBICACION=${UBICACIONES[$IND]} 
           ULTIMA_UBICACION=$UBICACION 
           LISTAR_BASE $UBICACION 
           # variable que indica que la ubicacion es correcta
           OK=true 
           # indicar que el inicio de la funcion ha terminado
           INICIO=false 
       else 
           # recibir parametro ingresado por el usuario 
           RECIBIDO=$1
           # validar que el parametro no sea nulo
           if [ $RECIBIDO ]; then 
                 # ubicarse en el directorio raiz 
                 if [ $RECIBIDO = "/" ]; then 
                        IND=0
                        UBICACIONES[$IND]=/ 
                        UBICACION=${UBICACIONES[$IND]} 
                        LISTAR_BASE $UBICACION  
                        ULTIMA_UBICACION=$UBICACION 
                        OK=true  
                    # administrar ficheros
                    elif [ $RECIBIDO = "aqui" ]; then 
                       	UBICACION=$ULTIMA_UBICACION
                        if [ $NO_VALIDAR_FICHERO = true ]; then
                             ADMINISTRAR_FICHERO_BASE $DIRECTORIO_FICHEROS $UBICACION $CADENA_ELEMENTOS $NO_VALIDAR_FICHERO $COMANDO 
                          else
                             if [ $FICHERO_PERMITIDO = true ]; then
                                ADMINISTRAR_FICHERO_BASE $DIRECTORIO_FICHEROS $UBICACION $TP_FICHERO $NO_VALIDAR_FICHERO $COMANDO 
                             fi
                        fi
	                LISTAR_BASE $UBICACION 
                        ULTIMA_UBICACION=$UBICACION 
                        OK=false 
                    # mostrar información sobre el funcionamiento del programa 
                    elif [ $RECIBIDO = "ayuda" ]; then
                        INFORMACION
                        UBICACION=$ULTIMA_UBICACION
                        LISTAR_BASE $UBICACION
                        ULTIMA_UBICACION=$UBICACION
                        OK=false
                    # situarse en el directorio principal
                    elif [ $RECIBIDO = "cd" ]; then 
                        IND=0
                        UBICACIONES[$IND]=~/ 
                        UBICACION=${UBICACIONES[$IND]} 
                        LISTAR_BASE $UBICACION  
                        ULTIMA_UBICACION=$UBICACION 
                        OK=true  
                    # retornar a la UBICACION anterior
                    elif [ $RECIBIDO = "cd.." ]; then 
                        # validar que la ubicación actual sea el directorio principal 
                        if [ $UBICACION = ${UBICACIONES[0]} ]; then 
                               IND=0 
                               UBICACION=${UBICACIONES[0]}
                               LISTAR_BASE $UBICACION
                               ULTIMA_UBICACION=$UBICACION
                               OK=true 
                           else 
                               let IND-=1 
                               UBICACION=${UBICACIONES[$IND]} 
                               LISTAR_BASE $UBICACION
                               ULTIMA_UBICACION=$UBICACION
                               OK=true
                        fi 
                    # seleccionar ficheros a copiar 
                    elif [ $(EXTRAER_CARACTER_BASE $RECIBIDO 1 6) = "copiar" ]; then
                         if [ $(EXTRAER_CARACTER_BASE $RECIBIDO 7 7) ]; then
                            if [ $(EXTRAER_CARACTER_BASE $RECIBIDO 7 7) = "," ]; then
                                 CADENA_ELEMENTOS=$(EXTRAER_CARACTER_BASE $RECIBIDO 8 100)
                                 DIRECTORIO_FICHEROS=$ULTIMA_UBICACION
                                 NO_VALIDAR_FICHERO=true
                                 IMPRIMIR_BASE "FICHEROS SELECCIONADOS"
                               else
                                NO_VALIDAR_FICHERO=false
                                FICHERO_PERMITIDO=true
                                TIPO_FICHERO=$(EXTRAER_CARACTER_BASE $RECIBIDO 7 15)
                                if [ $(VALIDAR_TIPO_FICHERO_BASE $TIPO_FICHERO) = "error_fichero" ]; then
                                     FICHERO_PERMITIDO=false
                                   elif [ $(VALIDAR_TIPO_FICHERO_BASE $TIPO_FICHERO) = "todo" ]; then
                                     TP_FICHERO="todo"
                                   elif [ $(VALIDAR_TIPO_FICHERO_BASE $TIPO_FICHERO) = $TIPO_FICHERO ]; then 
                                     TP_FICHERO=$TIPO_FICHERO 
                                   else
                                       FICHERO_PERMITIDO=false 
                                fi 
                                if [ $FICHERO_PERMITIDO = true ]; then
			              DIRECTORIO_FICHEROS=$ULTIMA_UBICACION 
                                      IMPRIMIR_BASE "FICHEROS SELECCIONADOS"
                                   else
                                      IMPRIMIR_BASE "FICHEROS NO PERMITIDOS" 
                                fi 
                           fi
                        fi
                        UBICACION=$ULTIMA_UBICACION
                        LISTAR_BASE $UBICACION 
                        ULTIMA_UBICACION=$UBICACION 
                        COMANDO="cp" 
                        OK=false  
                    # modificar los nombres de ficheros que contengan espacios 
                    elif [ $RECIBIDO = "espacios" ]; then
                        UBICACION=$ULTIMA_UBICACION
                        QUITAR_ESPACIOS_BASE $UBICACION
                        LISTAR_BASE $UBICACION 
                        ULTIMA_UBICACION=$UBICACION 
                        OK=false 
                    # mostrar menu principal
                    elif [ $RECIBIDO = "menu" ]; then
                        IND=0
                        UBICACION=${UBICACIONES[$IND]} 
                        LISTAR_BASE $UBICACION  
                        ULTIMA_UBICACION=$UBICACION 
                        OK=true  
                        break 
                    # seleccionar ficheros a mover 
                    elif [ $(EXTRAER_CARACTER_BASE $RECIBIDO 1 5) = "mover" ]; then 
                        if [ $(EXTRAER_CARACTER_BASE $RECIBIDO 6 6) ]; then
                           if [ $(EXTRAER_CARACTER_BASE $RECIBIDO 6 6) = "," ]; then
                                 CADENA_ELEMENTOS=$(EXTRAER_CARACTER_BASE $RECIBIDO 7 100) 
                                 DIRECTORIO_FICHEROS=$ULTIMA_UBICACION
                                 NO_VALIDAR_FICHERO=true
                                 IMPRIMIR_BASE "FICHEROS SELECCIONADOS"
                              else 
                                 NO_VALIDAR_FICHERO=false
                                 FICHERO_PERMITIDO=true 
                                 TIPO_FICHERO=$(EXTRAER_CARACTER_BASE $RECIBIDO 6 15)
                                 if [ $(VALIDAR_TIPO_FICHERO_BASE $TIPO_FICHERO) = "error_fichero" ]; then
                                       FICHERO_PERMITIDO=false
                                    elif [ $(VALIDAR_TIPO_FICHERO_BASE $TIPO_FICHERO) = "todo" ]; then
                                       TP_FICHERO="todo"
			            elif [ $(VALIDAR_TIPO_FICHERO_BASE $TIPO_FICHERO) = $TIPO_FICHERO ]; then 
                                       TP_FICHERO=$TIPO_FICHERO
                                    else
                                       FICHERO_PERMITIDO=false 
                                 fi 
                                 if [ $FICHERO_PERMITIDO = true ]; then
			               DIRECTORIO_FICHEROS=$ULTIMA_UBICACION 
                                       IMPRIMIR_BASE "FICHEROS SELECCIONADOS"
                                    else
                                       IMPRIMIR_BASE "FICHEROS NO PERMITIDOS" 
                                 fi 
                           fi
                        fi
                        UBICACION=$ULTIMA_UBICACION
                        LISTAR_BASE $UBICACION 
                        ULTIMA_UBICACION=$UBICACION 
                        COMANDO="mv" 
                        OK=false  
                    # finalizar programa 
                    elif [ $RECIBIDO = "salir" ]; then
                        SALIR 
                    else 
                        # verificar que directorio este compuesto por mas de una palabra 
                        if [ $(EXTRAER_CARACTER_BASE $RECIBIDO 1 1) = "_" ]; then 
                              _DIRECTORIO=$(EXTRAER_CARACTER_BASE $RECIBIDO 2 100)
                              UBICACION=$UBICACION$(RENOMBRAR_DIRECTORIO_BASE $ULTIMA_UBICACION $_DIRECTORIO)/ 
                           else 
	                      UBICACION=$UBICACION$RECIBIDO/
                        fi 
                        # validar directorio 
                        if [ -d $UBICACION ]; then 
                               let IND+=1 
	                       LISTAR_BASE $UBICACION 
                               ULTIMA_UBICACION=$UBICACION 
                               UBICACIONES[$IND]=$UBICACION
                               OK=true 
                           else 
                               LISTAR_BASE $ULTIMA_UBICACION 
                               UBICACION=$ULTIMA_UBICACION 
                               UBICACIONES[$IND]=$UBICACION 
                               OK=false 
                        fi
                 fi
              # si parametro ingresado es nulo 
              else
                 # verificar que el directorio actual sea el directorio personal 
                 if [ "$UBICACION" = "${UBICACIONES[0]}" ]; then 
                       UBICACION=${UBICACIONES[0]} 
                       LISTAR_BASE $UBICACION 
                       OK=true 
                    else 
                       LISTAR_BASE $ULTIMA_UBICACION 
                       OK=false 
                 fi 
           fi        
    fi  
    # verificar cambio de UBICACION
    if [ $OK = true ]; then  
          IMPRIMIR_BASE "\n$UBICACION\c" 
       else 
          IMPRIMIR_BASE "\n$ULTIMA_UBICACION\c"
    fi
    OK=false 
}
