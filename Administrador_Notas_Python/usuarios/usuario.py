#!/usr/bin/env python
# - * - coding: latin-1 - * -

import datetime, hashlib 
import usuarios.conexion as conexion 

connect = conexion.conectar() 
database = connect[0] 
cursor = connect[1] 

class Usuario:
      def __init__(self, nombre, apellidos, email, passwd): 
          self.nombre = nombre 
          self.apellidos = apellidos 
          self.email = email  
          self.passwd = passwd 
      
      def registrar(self): 
          fecha = datetime.datetime.now()

          # Cifrar contraseña
          cifrado = hashlib.sha256() 
          cifrado.update(self.passwd.encode('utf8')) 

          sql = "INSERT INTO usuarios VALUES(null, ?, ?, ?, ?, ?)" 
          usuario = (self.nombre, self.apellidos, self.email, cifrado.hexdigest(), fecha) 

          try:
             cursor.execute(sql, usuario) 
             database.commit()
             result = [cursor.rowcount, self] 
          except: 
             result = [0, self]

          return result 

      def identificar(self): 
          # Consulta para comprobar si existe el usuario
          sql = 'SELECT COUNT(*), nombre, fecha FROM usuarios WHERE email=? AND passwd=?;' 

          # Cifrar contraseña
          cifrado = hashlib.sha256() 
          cifrado.update(self.passwd.encode('utf8')) 

          # Datos para la consulta 
          usuario = (self.email, cifrado.hexdigest()) 

          cursor.execute(sql, usuario) 
          result = cursor.fetchone() 

          return result 
