#!/bin/bash
#
# apagar_sistema.sh
# Script encargado de ejecutar el comando para efectuar el apagado y reinicio del sistema 

# invocar script que contiene el password del usuario root 
source /etc/passwd_root.sh 

if [ $1 ]; then
      typeset -i tiempo=$1
      if [ $tiempo -eq 0 ]; then
            # reiniciar sistema
            echo $passwd | sudo -S reboot 
         else
            # apagar sistema tomando el parametro ingresado como tiempo
            # para realizar dicho proceso
            echo $passwd | sudo -S shutdown +$tiempo 
      fi 
   else 
      read -p "Apagar sitema? s/n: " respuesta 
      if [ $respuesta == "s" ]; then 
         # apagar sistema inmediatamente 
         echo $passwd | sudo -S shutdown now 
      else
         echo "No se apagará el sistema" 
     fi
fi
