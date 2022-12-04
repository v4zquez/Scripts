#!/usr/bin/env python
# - * - coding: latin-1 - * -

import datetime
import usuarios.conexion as conexion 

connect = conexion.conectar() 
database = connect[0] 
cursor = connect[1] 

class Nota:
      def __init__(self, usuarioId, titulo = '' , descripcion = ''): 
          self.usuarioId = usuarioId 
          self.titulo = titulo 
          self.descripcion = descripcion 
      
      def guardar(self): 
          fecha = datetime.datetime.now()

          sql = "INSERT INTO notas VALUES(null, ?, ?, ?, ?)" 
          nota = (self.usuarioId, self.titulo, self.descripcion, fecha) 

          cursor.execute(sql, nota) 
          database.commit()
          result = [cursor.rowcount, self] 

          return result 

      def listar(self):
          sql = f'SELECT * FROM notas WHERE usuarioId = {self.usuarioId}' 
          
          cursor.execute(sql)
          result = cursor.fetchall() 

          return result 

      def eliminar(self):
          sql = f"DELETE FROM notas WHERE usuarioId = {self.usuarioId} AND titulo LIKE '%{self.titulo}%'" 
          
          cursor.execute(sql)
          database.commit() 

          return [cursor.rowcount, self] 

