#!/usr/bin/env python
# - * - coding: latin-1 - * -

''' 
Proyecto Python y Sqlite
- Abrir asistente_
- Acceso o registro
- Registro -> crear un usuario en la base de datos 
- Acceso -> iniciar sesión & preguntará: 
- Crear nota, mostrar notas, borrarlas 
'''

import os
from usuarios import acciones

comando = 'clear'

ejecutar = acciones.Acciones()
accion = 1 

while (accion != 0):
      #os.system(comando) 
      print(''' 
      Acciones disponibles: 
      [1] Registro
      [2] Acceso al sistema 
      [0] Salir 
      ''')

      accion = int(input('¿Que desea hacer?: ')) 

      if accion == 1:
         ejecutar.registro()
      elif accion == 2:
         ejecutar.acceso() 
