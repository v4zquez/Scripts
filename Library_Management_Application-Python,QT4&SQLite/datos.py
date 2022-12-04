#!/usr/bin/env python 
# -*- coding: utf-8 -*-

import sqlite3  

def conexion(): 
    return sqlite3.connect("biblioteca.db")

class usuarioBBDD:
      def validarCuentaUsuarioBBDD(self, listaElementos):
          cnx = conexion()
          cursor = cnx.cursor()
          cursor.execute("select count(*) from usuarios where usuario=? and clave=?", listaElementos) 
          resultado = cursor.fetchone() 
          return (resultado) 
          cursor.close()
          cnx.close()

      def existeUsuarioBBDD(self, listaElementos):
          cnx = conexion()
          cursor = cnx.cursor()
          cursor.execute("select count(*) from usuarios where usuario=?", listaElementos) 
          resultado = cursor.fetchone() 
          return (resultado) 
          cursor.close()
          cnx.close()

      def registrarUsuarioBBDD(self, listaElementos):
          cnx = conexion()
          cursor = cnx.cursor() 
          # ->listaElementos<- es una lista que contiene los tres valores requeridos
          # para realizar el registro en la base de datos 
          cursor.execute("insert into usuarios values(?, ?, ?)", listaElementos) 
          cursor.close()
          cnx.commit()
          cnx.close()

      def modificarUsuarioBBDD(self, listaElementos):
          cnx = conexion()
          cursor = cnx.cursor() 
          cursor.execute("update usuarios set clave=? where usuario=?", listaElementos) 
          cursor.close()
          cnx.commit()
          cnx.close()
      
      def buscarUsuarioBBDD(self, listaElementos):
          cnx = conexion()
          cursor = cnx.cursor() 
          cursor.execute("select usuario, clave, cliente from usuarios where usuario=?", listaElementos) 
          resultado = cursor.fetchall() 
          return (resultado) 
          cursor.close()
          cnx.close()

      def mostrarUsuarioBBDD(self):
          cnx = conexion()
          cursor = cnx.cursor() 
          cursor.execute("select usuario, clave, cliente from usuarios") 
          resultado = cursor.fetchall() 
          return (resultado) 
          cursor.close()
          cnx.close()

class clienteBBDD:
      def existeClienteBBDD(self, listaElementos):
          cnx = conexion()
          cursor = cnx.cursor()
          cursor.execute("select count(*) from clientes where cedula=?", listaElementos) 
          resultado = cursor.fetchone() 
          return (resultado) 
          cursor.close()
          cnx.close()

      def registrarClienteBBDD(self, listaElementos): 
          cnx = conexion()
          cursor = cnx.cursor() 
          cursor.execute("insert into clientes values(?, ?, ?, ?, ?, ?, ?, ?, ?, ?)", listaElementos)
          cursor.close()
          cnx.commit()
          cnx.close()

      def modificarClienteBBDD(self, listaElementos): 
          cnx = conexion()
          cursor = cnx.cursor() 
          cursor.execute("update clientes set nombre=?, apellido1=?, apellido2=?, edad=?, direccion=?, telefono=?, fecha_nacimiento=?, email=?, sexo=? where cedula=?", listaElementos) 
          cursor.close()
          cnx.commit()
          cnx.close()

      def buscarClienteBBDD(self, listaElementos):
          cnx = conexion()
          cursor = cnx.cursor() 
          cursor.execute("select cedula, nombre, apellido1, apellido2, edad, direccion, telefono, fecha_nacimiento, email, sexo from clientes where cedula=?", listaElementos) 
          resultado = cursor.fetchall() 
          return (resultado) 
          cursor.close()
          cnx.close()

      def buscarCliente_UsuarioBBDD(self, listaElementos):
          cnx = conexion()
          cursor = cnx.cursor() 
          sentencia = "select cedula, nombre, apellido1, apellido2, edad, direccion, telefono, fecha_nacimiento, email, sexo, usuario, clave from clientes \
          inner join usuarios on cedula=? and cliente=?" 
          cursor.execute(sentencia, listaElementos) 
          resultado = cursor.fetchall() 
          return (resultado) 
          cursor.close()
          cnx.close()

      def mostrarClienteBBDD(self):
          cnx = conexion()
          cursor = cnx.cursor() 
          cursor.execute("select cedula, nombre, apellido1, apellido2, edad, direccion, telefono, fecha_nacimiento, email, sexo from clientes") 
          resultado = cursor.fetchall() 
          return (resultado) 
          cursor.close()
          cnx.close()

      def mostrarCliente_UsuarioBBDD(self):
          cnx = conexion()
          cursor = cnx.cursor() 
          sentencia = "select cedula, nombre, apellido1, apellido2, edad, direccion, telefono, fecha_nacimiento, email, sexo, usuario, clave from clientes \
          inner join usuarios on cedula=cliente" 
          cursor.execute(sentencia) 
          resultado = cursor.fetchall() 
          return (resultado) 
          cursor.close()
          cnx.close()

class autorBBDD:
      def registrarAutorBBDD(self, listaElementos): 
          cnx = conexion()
          cursor = cnx.cursor() 
          cursor.execute("insert into autores values(?, ?, ?, ?)", listaElementos) 
          cursor.close()
          cnx.commit()
          cnx.close()

      def modificarAutorBBDD(self, listaElementos): 
          cnx = conexion()
          cursor = cnx.cursor() 
          cursor.execute("update autores set nombre=?, apellido1=?, apellido2=? where cod_autor=?", listaElementos) 
          cursor.close()
          cnx.commit()
          cnx.close()

      def buscarAutorBBDD(self, listaElementos):
          cnx = conexion()
          cursor = cnx.cursor() 
          cursor.execute("select cod_autor, nombre, apellido1, apellido2 from autores where cod_autor=?", listaElementos) 
          resultado = cursor.fetchall() 
          return (resultado) 
          cursor.close()
          cnx.close()

      def mostrarAutorBBDD(self):
          cnx = conexion()
          cursor = cnx.cursor() 
          cursor.execute("select cod_autor, nombre, apellido1, apellido2 from autores") 
          resultado = cursor.fetchall() 
          return (resultado) 
          cursor.close()
          cnx.close()

class categoriaBBDD:
      def registrarCategoriaBBDD(self, listaElementos): 
          cnx = conexion()
          cursor = cnx.cursor() 
          cursor.execute("insert into categorias values(?, ?, ?)", listaElementos) 
          cursor.close()
          cnx.commit()
          cnx.close()

      def modificarCategoriaBBDD(self, listaElementos): 
          cnx = conexion()
          cursor = cnx.cursor() 
          cursor.execute("update categorias set nombre=?, descripcion=? where cod_categoria=?", listaElementos) 
          cursor.close()
          cnx.commit()
          cnx.close()

      def buscarCategoriaBBDD(self, listaElementos):
          cnx = conexion()
          cursor = cnx.cursor() 
          cursor.execute("select cod_categoria, nombre, descripcion from categorias where cod_categoria=?", listaElementos) 
          resultado = cursor.fetchall() 
          return (resultado) 
          cursor.close()
          cnx.close()

      def mostrarCategoriaBBDD(self):
          cnx = conexion()
          cursor = cnx.cursor() 
          cursor.execute("select cod_categoria, nombre, descripcion from categorias") 
          resultado = cursor.fetchall() 
          return (resultado) 
          cursor.close()
          cnx.close()

class editorialBBDD:
      def registrarEditorialBBDD(self, listaElementos): 
          cnx = conexion()
          cursor = cnx.cursor() 
          cursor.execute("insert into editoriales values(?, ?, ?, ?, ?)", listaElementos) 
          cursor.close()
          cnx.commit()
          cnx.close()

      def modificarEditorialBBDD(self, listaElementos): 
          cnx = conexion()
          cursor = cnx.cursor() 
          cursor.execute("update editoriales set nombre=?, descripcion=?, direccion=?, email=? where cod_editorial=?", listaElementos) 
          cursor.close()
          cnx.commit()
          cnx.close()

      def buscarEditorialBBDD(self, listaElementos):
          cnx = conexion()
          cursor = cnx.cursor() 
          cursor.execute("select cod_editorial, nombre, descripcion, direccion, email from editoriales where cod_editorial=?", listaElementos) 
          resultado = cursor.fetchall() 
          return (resultado) 
          cursor.close()
          cnx.close()

      def mostrarEditorialBBDD(self):
          cnx = conexion()
          cursor = cnx.cursor() 
          cursor.execute("select cod_editorial, nombre, descripcion, direccion, email from editoriales") 
          resultado = cursor.fetchall() 
          return (resultado) 
          cursor.close()
          cnx.close()

class libroBBDD:
      def registrarLibroBBDD(self, listaElementos): 
          cnx = conexion()
          cursor = cnx.cursor() 
          cursor.execute("insert into libros values(?, ?, ?, ?, ?, ?)", listaElementos) 
          cursor.close()
          cnx.commit()
          cnx.close()

      def modificarLibroBBDD(self, listaElementos): 
          cnx = conexion()
          cursor = cnx.cursor() 
          cursor.execute("update libros set nombre=?, descripcion=?, autor=?, categoria=?, editorial=? where cod_libro=?", listaElementos) 
          cursor.close()
          cnx.commit()
          cnx.close()

      def buscarLibroBBDD(self, listaElementos):
          cnx = conexion()
          cursor = cnx.cursor() 
          cursor.execute("select cod_libro, nombre, descripcion, autor, categoria, editorial from libros where cod_libro=?", listaElementos) 
          resultado = cursor.fetchall() 
          return (resultado) 
          cursor.close()
          cnx.close()

      def buscarLibro_nombreBBDD(self, listaElementos):
          cnx = conexion()
          cursor = cnx.cursor() 
          cursor.execute("select * from vistaLibros where nombre=?", listaElementos) 
          resultado = cursor.fetchall() 
          return (resultado) 
          cursor.close()
          cnx.close()

      def mostrarLibroBBDD(self):
          cnx = conexion()
          cursor = cnx.cursor() 
          cursor.execute("select cod_libro, nombre, descripcion, autor, categoria, editorial from libros") 
          resultado = cursor.fetchall() 
          return (resultado) 
          cursor.close()
          cnx.close()

      def mostrarLibro_CantidadBBDD(self):
          cnx = conexion()
          cursor = cnx.cursor() 
          sentencia = "select * from vistaLibros" 
          #sentencia = "select l.cod_libro, l.nombre, l.descripcion, a.nombre, c.nombre, e.nombre, cd.cantidad from autores a, categorias c, editoriales e, cantidades cd \
          #inner join libros l on l.autor=a.cod_autor and l.categoria=c.cod_categoria and l.editorial=e.cod_editorial and cd.libro=l.cod_libro"
          cursor.execute(sentencia) 
          resultado = cursor.fetchall() 
          return (resultado) 
          cursor.close()
          cnx.close()

      def mostrarInformacion_LibroBBDD(self, listaElementos):
          cnx = conexion()
          cursor = cnx.cursor() 
          sentencia="select l.cod_libro, l.nombre, l.descripcion, a.nombre, c.nombre, e.nombre from autores a, categorias c, editoriales e \
          inner join libros l on l.autor=a.cod_autor and l.categoria=c.cod_categoria and l.editorial=e.cod_editorial where l.nombre=?"
          cursor.execute(sentencia, listaElementos) 
          resultado = cursor.fetchall() 
          return (resultado) 
          cursor.close()
          cnx.close()

      def consultaExistencia_LibroBBDD(self, listaElementos):
          cnx = conexion()
          cursor = cnx.cursor() 
          cursor.execute("select cod_libro, nombre, descripcion, autor, categoria, editorial from libros where nombre=?", listaElementos) 
          resultado = cursor.fetchall() 
          return (resultado) 
          cursor.close()
          cnx.close()

class cantidadBBDD:
      def verificarExistenciaBBDD(self, listaElementos):
          cnx = conexion()
          cursor = cnx.cursor()
          cursor.execute("select cantidad from cantidades where libro=?", listaElementos) 
          resultado = cursor.fetchone() 
          return (resultado) 
          cursor.close()
          cnx.close()

      def agregarDevolucionBBDD(self, listaElementos): 
          cnx = conexion()
          cursor = cnx.cursor() 
          cursor.execute("select cantidad from cantidades where libro=(select cod_libro from libros where nombre=?)", listaElementos)
          _nombreLibro = listaElementos[0]
          _cantidad = int(cursor.fetchone()[0])+1 
          datos = [_cantidad, _nombreLibro] 
          cursor.execute("update cantidades set cantidad=? where libro=(select cod_libro from libros where nombre=?)", datos) 
          cursor.close()
          cnx.commit()
          cnx.close()

      def registrarCantidadBBDD(self, listaElementos): 
          cnx = conexion()
          cursor = cnx.cursor() 
          cursor.execute("insert into cantidades values(?, ?)", listaElementos) 
          cursor.close()
          cnx.commit()
          cnx.close()

      def modificarCantidadBBDD(self, listaElementos): 
          cnx = conexion()
          cursor = cnx.cursor() 
          cursor.execute("update cantidades set cantidad=? where libro=?", listaElementos) 
          cursor.close()
          cnx.commit()
          cnx.close()

      def buscarCantidadBBDD(self, listaElementos):
          cnx = conexion()
          cursor = cnx.cursor() 
          cursor.execute("select libro, cantidad from cantidades where libro=?", listaElementos) 
          resultado = cursor.fetchall() 
          return (resultado) 
          cursor.close()
          cnx.close()

      def mostrarCantidadBBDD(self):
          cnx = conexion()
          cursor = cnx.cursor() 
          cursor.execute("select libro, cantidad from cantidades") 
          resultado = cursor.fetchall() 
          return (resultado) 
          cursor.close()
          cnx.close()

class prestamoBBDD:
      def registrarPrestamoBBDD(self, listaElementos): 
          cnx = conexion()
          cursor = cnx.cursor() 
          cursor.execute("insert into prestamos (cliente, libro, fecha_prestamo, fecha_devolucion)values(?, ?, ?, ?)", listaElementos) 
          cursor.close()
          cnx.commit()
          cnx.close()

      def modificarPrestamoBBDD(self, listaElementos): 
          cnx = conexion()
          cursor = cnx.cursor() 
          cursor.execute("update prestamos set cliente=?, libro=?, fecha_prestamo=?, fecha_devolucion=? where cod_prestamo=?", listaElementos) 
          cursor.close()
          cnx.commit()
          cnx.close()

      def buscarPrestamoBBDD(self, listaElementos):
          cnx = conexion()
          cursor = cnx.cursor() 
          cursor.execute("select cod_prestamo, cliente, libro, fecha_prestamo, fecha_devolucion from prestamos where cod_prestamo=?", listaElementos) 
          resultado = cursor.fetchall() 
          return (resultado) 
          cursor.close()
          cnx.close()

      def buscarPrestamo_clienteBBDD(self, listaElementos):
          cnx = conexion()
          cursor = cnx.cursor() 
          cursor.execute("select * from vistaPrestamos where cliente=?", listaElementos) 
          resultado = cursor.fetchall() 
          return (resultado) 
          cursor.close()

      def buscarPrestamo_codPrestamoBBDD(self, listaElementos):
          cnx = conexion()
          cursor = cnx.cursor() 
          cursor.execute("select * from vistaPrestamos where cod_prestamo=?", listaElementos) 
          resultado = cursor.fetchall() 
          return (resultado) 
          cursor.close()

      def mostrarPrestamoBBDD(self):
          cnx = conexion()
          cursor = cnx.cursor() 
          cursor.execute("select cod_prestamo, cliente, libro, fecha_prestamo, fecha_devolucion from prestamos") 
          resultado = cursor.fetchall() 
          return (resultado) 
          cursor.close()
          cnx.close()

      def eliminarPrestamoBBDD(self, listaElementos):
          cnx = conexion()
          cursor = cnx.cursor()
          cursor.execute("delete from prestamos where cod_prestamo=?", listaElementos) 
          cursor.close()
          cnx.commit()
          cnx.close()
          

class variosBBDD:
      def solicitarDatosBBDD(self, columna, tabla): 
          cnx = conexion()
          cursor = cnx.cursor() 
          cursor.execute("select "+columna+" from "+tabla+"") 
          resultado = cursor.fetchall() 
          return (resultado) 
          cursor.close()
          cnx.close()

      def solicitarDatos_prestamoBBDD(self, listaElementos): 
          cnx = conexion()
          cursor = cnx.cursor() 
          cursor.execute("select cod_prestamo from prestamos where cliente = ?", listaElementos) 
          resultado = cursor.fetchall() 
          return (resultado) 
          cursor.close()
          cnx.close()

      def busquedaAvanzadaBBDD(self, tabla, columna, parametro):
          cnx = conexion()
          cursor = cnx.cursor() 
          cursor.execute("select * from "+tabla+" where "+columna+" like '%"+parametro+"%'") 
          resultado = cursor.fetchall() 
          return (resultado) 
          cursor.close()
          cnx.close()

      def busquedaAvanzadaLibro_nombreBBDD(self, parametro):
          cnx = conexion()
          cursor = cnx.cursor() 
          sentencia = "select * from vistaLibros where nombre like '%"+parametro+"%'" 
          #sentencia = "select l.cod_libro, l.nombre, l.descripcion, a.nombre, c.nombre, e.nombre, cd.cantidad from autores a, categorias c, editoriales e, cantidades cd \
          #inner join libros l on l.autor=a.cod_autor and l.categoria=c.cod_categoria and l.editorial=e.cod_editorial and cd.libro=l.cod_libro where l."+c+" like '%"+p+"%'" 
          cursor.execute(sentencia) 
          resultado = cursor.fetchall() 
          return (resultado) 
          cursor.close()
          cnx.close()

      def busquedaAvanzadaLibro_autorBBDD(self, parametro):
          cnx = conexion()
          cursor = cnx.cursor() 
          sentencia = "select l.cod_libro, l.nombre, l.descripcion, a.nombre, c.nombre, e.nombre, cd.cantidad from autores a, categorias c, editoriales e, cantidades cd \
          inner join libros l on l.autor=a.cod_autor and l.categoria=c.cod_categoria and l.editorial=e.cod_editorial and cd.libro=l.cod_libro where a.nombre like '%"+parametro+"%'" 
          cursor.execute(sentencia) 
          resultado = cursor.fetchall() 
          return (resultado) 
          cursor.close()
          cnx.close()

      def busquedaAvanzadaLibro_categoriaBBDD(self, parametro):
          cnx = conexion()
          cursor = cnx.cursor() 
          sentencia = "select l.cod_libro, l.nombre, l.descripcion, a.nombre, c.nombre, e.nombre, cd.cantidad from autores a, categorias c, editoriales e, cantidades cd \
          inner join libros l on l.autor=a.cod_autor and l.categoria=c.cod_categoria and l.editorial=e.cod_editorial and cd.libro=l.cod_libro where c.nombre like '%"+parametro+"%'" 
          cursor.execute(sentencia) 
          resultado = cursor.fetchall() 
          return (resultado) 
          cursor.close()
          cnx.close()

      def llavePrimariaBBDD(self, columna, tabla): 
          cnx = conexion()
          cursor = cnx.cursor() 
          cursor.execute("select max("+columna+") from "+tabla+"") 
          resultado = cursor.fetchone() 
          return (resultado) 
          cursor.close()
          cnx.close()

      def obtenerClienteBBDD(self, usuario):
          cnx = conexion()
          cursor = cnx.cursor()
          cursor.execute("select cedula, nombre, apellido1 from clientes where cedula=(select cliente from usuarios where usuario='"+usuario+"')") 
          resultado = cursor.fetchall()
          return (resultado)
          cursor.close()
          cnx.close() 
