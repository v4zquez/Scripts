#!/usr/bin/env python
# - * - coding: latin-1 - * -

import usuarios.usuario as modelo
import notas.acciones

class Acciones:
      def registro(self): 
          print("Registro en el sistema") 
          nombre = input("¿Cual es tu nombre?: ")  
          apellidos = input("¿Cuales son tus apellidos?: ")  
          email = input("Introduce tu email:  ")  
          passwd = input("Introduce tu contraseña:  ")  

          usuario = modelo.Usuario(nombre, apellidos, email, passwd)
          registro = usuario.registrar()

          if registro[0] >= 1: 
             print(f'Perfecto {registro[1].nombre} te has registrado con el email {registro[1].email}') 
          else: 
             print('No te has registrado correctamente') 

      def acceso(self): 
          print("Identificación en el sistema") 
         
          '''
          try: 
             email = input("Introduce tu email:  ")  
             passwd = input("Introduce tu contraseña:  ")  
         
             usuario = modelo.Usuario('', '', email, passwd)
             acceso = usuario.identificar()

             if acceso[0] == 1:
                print(f'Bienvenido {acceso[1]}, te has registrado el {acceso[2]}') 
                self.proximasAcciones(acceso)
             else:
                print(f'Identificación incorrecta!! Intentalo más tarde') 
          except Exception as e: 
                print(type(e)) 
                print(type(e).__name__) 
                print(f'Identificación incorrecta!! Intentalo más tarde') 
          '''
        
          email = input("Introduce tu email:  ")  
          passwd = input("Introduce tu contraseña:  ")  
         
          usuario = modelo.Usuario('', '', email, passwd)
          acceso = usuario.identificar()

          if acceso[0] == 1:
             print(f'Bienvenido {acceso[1]}, te has registrado el {acceso[2]}') 
             self.proximasAcciones(acceso)
          else:
             print(f'Identificación incorrecta!! Intentalo más tarde') 

      def proximasAcciones(self, usuario): 
          print(''' 
          Acciones disponibles: 
          [1] Crear nota 
          [2] Mostrar notas 
          [3] Eliminar notas
          [0] Salir 
          ''')    

          accion = int(input('¿Que desea hacer? ')) 
          realizar = notas.acciones.Acciones()
           
          if accion == 1: 
             realizar.crear(usuario)
             self.proximasAcciones(usuario)
          elif accion == 2: 
             realizar.mostrar(usuario)
             self.proximasAcciones(usuario)
          elif accion == 3: 
             realizar.borrar(usuario)
             self.proximasAcciones(usuario)
          elif accion == 0: 
             print(f'Ok {usuario[1]}, hasta pronto!') 
             exit() 
          else:
             print('Opción incorrecta')
             self.proximasAcciones(usuario)
          
