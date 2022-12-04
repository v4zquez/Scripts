#!/usr/bin/env python 
# -*- coding: utf-8 -*-

from datos import usuarioBBDD, clienteBBDD, autorBBDD, categoriaBBDD, editorialBBDD, libroBBDD, cantidadBBDD, prestamoBBDD, variosBBDD

class usuario:
      def validarCuentaUsuario(self, listaElementos):
          _usuario = usuarioBBDD() 
          return _usuario.validarCuentaUsuarioBBDD(listaElementos)

      def existeUsuario(self, listaElementos):
          _usuario = usuarioBBDD() 
          return _usuario.existeUsuarioBBDD(listaElementos)

      def registrarUsuario(self, listaElementos):
          _usuario = usuarioBBDD() 
          _usuario.registrarUsuarioBBDD(listaElementos) 

      def modificarUsuario(self, listaElementos):
          try:
            _usuario = usuarioBBDD() 
            _usuario.modificarUsuarioBBDD(listaElementos) 
            return "Usuario Modificado"
          except Exception, e:
            return "Error al modificar datos"
      
      def buscarUsuario(self, listaElementos):
          _usuario = usuarioBBDD() 
          return _usuario.buscarUsuarioBBDD(listaElementos)

      def mostrarUsuario(self):
          _usuario = usuarioBBDD() 
          return _usuario.mostrarUsuarioBBDD()

class cliente:
      def existeCliente(self, listaElementos):
          _cliente = clienteBBDD() 
          return _cliente.existeClienteBBDD(listaElementos) 

      def registrarCliente(self, listaElementos): 
          _cliente = clienteBBDD()
          _cliente.registrarClienteBBDD(listaElementos) 
  
      def registrarClienteUsuario(self, listaElementos_cliente, listaElementos_usuario):
          # seleccionar cedula
          self.cedula = listaElementos_cliente[0]
          # seleccionar nombre de usuario 
          self.nombreUsuario = listaElementos_usuario[0]

          # registrar datos al no existir la cedula digitada
          if (not (cliente().existeCliente([self.cedula])[0])):
             # registrar datos al no existir nombre de usuario 
             if (not (usuario().existeUsuario([self.nombreUsuario])[0])):
                try:
                    cliente().registrarCliente(listaElementos_cliente)
                    usuario().registrarUsuario(listaElementos_usuario)
                    return "Usuario Registrado"
                except Exception, e:
                   return "Error al registrar datos"
             else:
               return "Nombre de usuario ya existente"
          else:
             return "Cedula ya existente"

      def modificarCliente(self, listaElementos): 
          _cliente = clienteBBDD()
          _cliente.modificarClienteBBDD(listaElementos) 

      def modificarClienteUsuario(self, listaElementos_cliente, listaElementos_usuario):
          # seleccionar cedula
          self.cedula = listaElementos_cliente[9]
          # seleccionar nombre de usuario 
          self.nombreUsuario = listaElementos_usuario[1]

          #registrar datos al existir la cedula digitada
          if (cliente().existeCliente([self.cedula])[0]):
             #registrar datos al existir nombre de usuario 
             if (usuario().existeUsuario([self.nombreUsuario])[0]):
                try:
                   cliente().modificarCliente(listaElementos_cliente)
                   usuarioBBDD().modificarUsuarioBBDD(listaElementos_usuario)
                   return "Usuario Modificado"
                except Exception, e:
                   return "Error al modificar datos"
             else:
                return "Nombre de usuario no existente"
          else:
             return "Cedula no existente"

      def buscarCliente(self, listaElementos):
          _cliente = clienteBBDD() 
          return _cliente.buscarClienteBBDD(listaElementos) 

      def buscarCliente_Usuario(self, listaElementos):
          _cliente = clienteBBDD() 
          return _cliente.buscarCliente_UsuarioBBDD(listaElementos) 

      def mostrarCliente(self):
          _cliente = clienteBBDD() 
          return _cliente.mostrarClienteBBDD() 

      def mostrarCliente_Usuario(self):
          _cliente = clienteBBDD() 
          return _cliente.mostrarCliente_UsuarioBBDD() 

class autor:
      def registrarAutor(self, listaElementos): 
          try:
            _autor = autorBBDD()
            _autor.registrarAutorBBDD(listaElementos) 
            return "Datos registrados"
          except Exception, e:
            return "Error al registrar datos"

      def modificarAutor(self, listaElementos): 
          try: 
             _autor = autorBBDD()
             _autor.modificarAutorBBDD(listaElementos) 
             return "Datos modificados"
          except Exception, e:
             return "Error al modificar datos"

      def buscarAutor(self, listaElementos):
          _autor = autorBBDD() 
          return _autor.buscarAutorBBDD(listaElementos) 

      def mostrarAutor(self):
          _autor = autorBBDD() 
          return _autor.mostrarAutorBBDD() 

class categoria:
      def registrarCategoria(self, listaElementos): 
          try:
            _categoria = categoriaBBDD() 
            _categoria.registrarCategoriaBBDD(listaElementos) 
            return "Datos registrados"
          except Exception, e:
            return "Error al registrar datos"

      def modificarCategoria(self, listaElementos): 
          try:
            _categoria = categoriaBBDD() 
            _categoria.modificarCategoriaBBDD(listaElementos) 
            return "Datos modificados"
          except Exception, e:
             return "Error al modificar datos"

      def buscarCategoria(self, listaElementos):
          _categoria = categoriaBBDD() 
          return _categoria.buscarCategoriaBBDD(listaElementos) 

      def mostrarCategoria(self):
          _categoria = categoriaBBDD() 
          return _categoria.mostrarCategoriaBBDD() 

class editorial:
      def registrarEditorial(self, listaElementos): 
          try:
            _editorial = editorialBBDD()
            _editorial.registrarEditorialBBDD(listaElementos) 
            return "Datos registrados"
          except Exception, e:
            return "Error al registrar datos"

      def modificarEditorial(self, listaElementos): 
          try:
            _editorial = editorialBBDD()
            _editorial.modificarEditorialBBDD(listaElementos) 
            return "Datos modificados"
          except Exception, e:
             return "Error al modificar datos"

      def buscarEditorial(self, listaElementos):
          _editorial = editorialBBDD()
          return _editorial.buscarEditorialBBDD(listaElementos) 

      def mostrarEditorial(self):
          _editorial = editorialBBDD()
          return _editorial.mostrarEditorialBBDD() 

class libro:
      def registrarLibro(self, listaElementos): 
          _libro = libroBBDD()
          _libro.registrarLibroBBDD(listaElementos)
          return "Datos registrados"

      def modificarLibro(self, listaElementos): 
          try:
            _libro = libroBBDD()
            _libro.modificarLibroBBDD(listaElementos)
            return "Datos modificados"
          except Exception, e:
            return "Error al modificar datos"

      def buscarLibro(self, listaElementos):
          _libro = libroBBDD()
          return _libro.buscarLibroBBDD(listaElementos)

      def buscarLibro_nombre(self, listaElementos):
          _libro = libroBBDD()
          return _libro.buscarLibro_nombreBBDD(listaElementos)

      def mostrarLibro(self):
          _libro = libroBBDD()
          return _libro.mostrarLibroBBDD()

      def mostrarInformacion_Libro(self, listaElementos):
          _libro = libroBBDD()
          return _libro.mostrarInformacion_LibroBBDD(listaElementos)

      def mostrarLibro_Cantidad(self):
          _libro = libroBBDD()
          return _libro.mostrarLibro_CantidadBBDD()

      def consultaExistencia_Libro(self, listaElementos):
          _libro = libroBBDD()
          return _libro.consultaExistencia_LibroBBDD(listaElementos)

class cantidad:
      def verificarExistencia(self, listaElementos):
          _cantidad = cantidadBBDD()
          return _cantidad.verificarExistenciaBBDD(listaElementos)

      def agregarDevolucion(self, listaElementos): 
          _cantidad = cantidadBBDD()
          _cantidad.agregarDevolucionBBDD(listaElementos) 

      def registrarCantidad(self, listaElementos): 
          _cantidad = cantidadBBDD()
          _cantidad.registrarCantidadBBDD(listaElementos)

      def modificarCantidad(self, listaElementos): 
          _cantidad = cantidadBBDD()
          _cantidad.modificarCantidadBBDD(listaElementos)
          return "Datos modificados" 

      def buscarCantidad(self, listaElementos):
          _cantidad = cantidadBBDD()
          return _cantidad.buscarCantidadBBDD(listaElementos)

      def mostrarCantidad(self):
          _cantidad = cantidadBBDD()
          return _cantidad.mostrarCantidadBBDD()

class prestamo:
      def registrarPrestamo(self, listaElementos): 
          try:
            _prestamo = prestamoBBDD() 
            _prestamo.registrarPrestamoBBDD(listaElementos)
            return "Prestamo efectuado"
          except Exception, e:
            return "Error en el prestamo"

      def modificarPrestamo(self, listaElementos): 
          _prestamo = prestamoBBDD() 
          _prestamo.modificarPrestamoBBDD(listaElementos)

      def buscarPrestamo(self, listaElementos):
          _prestamo = prestamoBBDD() 
          return _prestamo.buscarPrestamoBBDD(listaElementos)

      def buscarPrestamo_cliente(self, listaElementos):
          _prestamo = prestamoBBDD() 
          return _prestamo.buscarPrestamo_clienteBBDD(listaElementos)

      def buscarPrestamo_codPrestamo(self, listaElementos):
          _prestamo = prestamoBBDD() 
          return _prestamo.buscarPrestamo_codPrestamoBBDD(listaElementos)

      def mostrarPrestamo(self):
          _prestamo = prestamoBBDD() 
          return _prestamo.mostrarPrestamoBBDD()

      def eliminarPrestamo(self, listaElementos):
          _prestamo = prestamoBBDD()
          _prestamo.eliminarPrestamoBBDD(listaElementos) 

class varios:
      def solicitarDatos(self, columna, tabla): 
          _varios = variosBBDD()
          return _varios.solicitarDatosBBDD(columna, tabla)

      def solicitarDatos_prestamo(self, listaElementos): 
          _varios = variosBBDD()
          return _varios.solicitarDatos_prestamoBBDD(listaElementos)

      def busquedaAvanzada(self, tabla, columna, parametro):
          _varios = variosBBDD()
          return _varios.busquedaAvanzadaBBDD(tabla, columna, parametro)

      def busquedaAvanzadaLibro_nombre(self, parametro):
          _varios = variosBBDD()
          return _varios.busquedaAvanzadaLibro_nombreBBDD(parametro)

      def busquedaAvanzadaLibro_autor(self, parametro):
          _varios = variosBBDD()
          return _varios.busquedaAvanzadaLibro_autorBBDD(parametro)

      def busquedaAvanzadaLibro_categoria(self, parametro):
          _varios = variosBBDD()
          return _varios.busquedaAvanzadaLibro_categoriaBBDD(parametro)

      def llavePrimaria(self, columna, tabla):
          _varios = variosBBDD()
          return _varios.llavePrimariaBBDD(columna, tabla) 
  
      def obtenerCliente(self, usuario):
          _varios = variosBBDD()
          return _varios.obtenerClienteBBDD(usuario)
