#!/usr/bin/env python 
# -*- coding: utf-8 -*- 

import sys, os
from datetime import date, datetime, timedelta

from PyQt4 import QtCore, QtGui, uic, Qt
from PyQt4.QtGui import QDialog

# importar módulos 
from controlador import usuario, cliente, editorial, categoria, autor, libro, cantidad, prestamo, varios 

# cargar archivo .ui
formularioAdministrador = uic.loadUiType("administrador.ui")[0]

# -> self <- es para hacer referencia a un objecto de la clase actual 
# ejemplo:
#        self.objecto
 
class administrador(QtGui.QMainWindow, formularioAdministrador):
      def __init__(self, parent=None):
     	  QtGui.QMainWindow.__init__(self, parent)
          
          # el método setupUi crea los Widgets y configura cada objecto que se necesitará 
  	  self.setupUi(self)
     
          # método de cuatro parametros para mostrar los datos de las tablas clientes y usuarios: 
          # el primer parametro hace referencia a la clase cliente del fichero datos importado anteriormente, en 
          # dicha clase se encuentra el método requerido -> mostrarCliente_Usuario, 
          # el segundo parametro suministra los nombres de las columnas de la tabla a la cual hace referencia el
          # parametro que recibe el método solicitarDatos,
          # los dos restantes datos se refieren al numero de columnas de la tabla donde se mostraran los datos, y
          # al nombre que tendra la tabla al mostrar los datos. 
          self.mostrarDatos(cliente().mostrarCliente_Usuario(), self.solicitarDatos("clientes"), 13, "Clientes")
          
          # método para llenar el qcombobox -> cmbBxParametro 
          # el primer parametro es el método solicitarDatos de la clase varios del fichero datos, dicho método recibe
          # dos datos, el primero es el nombre de la columna y el segundo hace referencia a la tabla requerida,
          # el siguiente parametro del método proveedor será el primer elemento del qcombobox (cmbBxParametro), esto
          # para indicar el tipo de dato que contiene el qcombobox.
          self.proveedor(varios().solicitarDatos("cedula", "clientes"), "cedula")

          # llenar qcombobox para mostrar los nombres de las tablas 
          for index in range(0, len(self.solicitarDatos("opciones"))):
              self.cmbBxOpcion.addItem(str(self.solicitarDatos("opciones")[index]))

          # caja de texto para realizar la busqueda avanzada 
          self.textBuscar.setText("Buscar ...")
          # cuando se presione  -> enter <- sobre la caja de texto se ejecutará el método -> busquedaAvanzada 
          self.textBuscar.returnPressed.connect(self.realizar_busquedaAvanzada)
 
          # evento al seleccionar una de las opciones del QcomboBox 
          # al seleccionar una opción del qcombobox se accionará el método indicado como parametro 
          # obteniendo el número de indice según la opción seleccionada. 
          self.cmbBxParametro.activated['int'].connect(self.buscado)
          self.cmbBxOpcion.activated['int'].connect(self.activado)

          # datos necesarios para el encabezado de las columnas de las tablas 
      def solicitarDatos(self, datos):
          if (datos == "clientes"):
             return ['Cedula', 'Nombre', 'P. Apellido', 'S. Apellido', 'Edad', 'Direccion', 'Telefono', 'F. Nac.', 'E-mail', 'Sexo', 'Usuario', 'Clave', 'Accion'] 
          elif (datos == "usuarios"): 
             return ['Usuario', 'Clave', 'Cliente', 'Accion'] 
          elif (datos == "editoriales"): 
             return ['Codigo', 'Nombre', 'Descripcion', 'Direccion', 'E-mail', 'Accion'] 
          elif (datos == "categorias"): 
             return ['Codigo', 'Nombre', 'Descripcion', 'Accion'] 
          elif (datos == "autores"): 
             return ['Codigo', 'Nombre', 'P. Apellido', 'S. Apellido', 'Accion'] 
          elif (datos == "libros"): 
             return ['Codigo', 'Nombre', 'Descripcion', 'Autor', 'Categoria', 'Editorial', 'Accion'] 
          elif (datos == "cantidad"):
             return ['Libro', 'Cantidad', 'Accion']
          elif (datos == "prestamos"):
             return ['Codigo', 'Cliente', 'Libro', 'Prestamo', 'Devolucion']
          # datos para llenar el qcombobox 
          elif (datos == "opciones"):
             return ['Clientes', 'Usuarios', 'Editoriales', 'Categorias', 'Autores', 'Libros', 'Cantidad', 'Prestamos', 'Salir'] 
              

          # método encargado de llenar el qcombobox -> cmbBxParametro 
      def buscado(self, indice):
          # validar que opción seleccionada no sea el nombre de la columna
          if (indice != 0):
             if (isinstance(indice, int)):
                # guardar el valor seleccionado en el qcombobox
                valor = self.cmbBxParametro.currentText()
                if (self.cmbBxOpcion.currentText() == "Clientes"):
                   # mostrar los datos requeridos en la tabla:
                   # el método -> buscarCliente_Usuario es el encargado de buscar los datos correspodientes con los dos
                   # parámetros suministrados, obtenidos del qcombobox. Los datos son suministrados en forma de lista -> [dato1, dato2, ...] 
                   self.mostrarDatos(cliente().buscarCliente_Usuario([int(valor), int(valor)]), self.solicitarDatos("clientes"), 13, "Clientes")
                elif (self.cmbBxOpcion.currentText() == "Usuarios"):
                   self.mostrarDatos(usuario().buscarUsuario([str(valor)]), self.solicitarDatos("usuarios"), 4, "Usuarios")
                elif (self.cmbBxOpcion.currentText() == "Editoriales"):
                   self.mostrarDatos(editorial().buscarEditorial([int(valor)]), self.solicitarDatos("editoriales"), 6, "Editoriales")
                elif (self.cmbBxOpcion.currentText() == "Categorias"):
                   self.mostrarDatos(categoria().buscarCategoria([int(valor)]), self.solicitarDatos("categorias"), 4, "Categorias")
                elif (self.cmbBxOpcion.currentText() == "Autores"):
                   self.mostrarDatos(autor().buscarAutor([int(valor)]), self.solicitarDatos("autores"), 5, "Autores")
                elif (self.cmbBxOpcion.currentText() == "Libros"):
	           self.mostrarDatos(libro().buscarLibro([int(valor)]), self.solicitarDatos("libros"), 7, "Libros")
                elif (self.cmbBxOpcion.currentText() == "Cantidad"):
                   self.mostrarDatos(cantidad().buscarCantidad([int(valor)]), self.solicitarDatos("cantidad"), 3, "Cantidad")
                elif (self.cmbBxOpcion.currentText() == "Prestamos"):
                   self.mostrarDatos(prestamo().buscarPrestamo([int(valor)]), self.solicitarDatos("prestamos"), 5, "Prestamos")
                # mostrar en el qcombobox el primer elemento
                self.cmbBxParametro.setCurrentIndex(0) 

          # método encargado de llenar la tabla (QTableWidget) con los datos requeridos 
      def activado(self, indice):
          # clientes y usuarios 
          if (indice == 0):  
             self.mostrarDatos(cliente().mostrarCliente_Usuario(), self.solicitarDatos("clientes"), 13, "Clientes")
             self.proveedor(varios().solicitarDatos("cedula", "clientes"), "cedula")
          # usuarios 
          elif (indice == 1): 
             self.mostrarDatos(usuario().mostrarUsuario(), self.solicitarDatos("usuarios"), 4, "Usuarios")
             self.proveedor(varios().solicitarDatos("usuario", "usuarios"), "usuario")
          # editoriales 
          elif (indice == 2): 
             self.mostrarDatos(editorial().mostrarEditorial(), self.solicitarDatos("editoriales"), 6, "Editoriales")
             self.proveedor(varios().solicitarDatos("cod_editorial", "editoriales"), "cod. Editorial")
          # categorias 
          elif (indice == 3): 
             self.mostrarDatos(categoria().mostrarCategoria(), self.solicitarDatos("categorias"), 4, "Categorias")
             self.proveedor(varios().solicitarDatos("cod_categoria", "categorias"), "cod. Categoria")
          # autores 
          elif (indice == 4): 
             self.mostrarDatos(autor().mostrarAutor(), self.solicitarDatos("autores"), 5, "Autores")
             self.proveedor(varios().solicitarDatos("cod_autor", "autores"), "cod. Autor")
          # libros 
          elif (indice == 5): 
             self.mostrarDatos(libro().mostrarLibro(), self.solicitarDatos("libros"), 7, "Libros")
             self.proveedor(varios().solicitarDatos("cod_libro", "libros"), "cod. Libro")
          # cantidad 
          elif (indice == 6): 
             self.mostrarDatos(cantidad().mostrarCantidad(), self.solicitarDatos("cantidad"), 3, "Cantidad")
             self.proveedor(varios().solicitarDatos("libro", "cantidades"), "Libro")
          # cantidad 
          elif (indice == 7): 
             self.mostrarDatos(prestamo().mostrarPrestamo(), self.solicitarDatos("prestamos"), 5, "Prestamos")
             self.proveedor(varios().solicitarDatos("cod_prestamo", "prestamos"), "Cod. Prestamo")
          # cerrar aplicación 
          elif (indice == 8):
             # cerrar ventana 
             reply = QtGui.QMessageBox.question(self, "Mensaje", "Seguro quiere salir?", QtGui.QMessageBox.Yes, QtGui.QMessageBox.No)
       	     if reply == QtGui.QMessageBox.Yes:
 		self.close() 
          # caja de texto para realizar la busqueda avanzada 
          self.textBuscar.setText("Buscar ...")

          # llenar qcombobox con datos suministrados 
      def proveedor(self, dato, columna): 
          # limpiar qcombobox
          self.cmbBxParametro.clear() 
          # añadir como primer elemento el nombre de la columna 
          self.cmbBxParametro.addItem(columna)
          # recorrer la lista -> dato <-, e ir añadiendo cada elemento al qcombobox 
          for i in dato:
              self.cmbBxParametro.addItem(str(i[0]))
           
      def realizar_busquedaAvanzada(self):
          if (self.cmbBxOpcion.currentText() == "Clientes"):
                                                         # tabla     columna   parametro                                                                                    
             self.mostrarDatos(varios().busquedaAvanzada("clientes", "cedula", str(self.textBuscar.text())), self.solicitarDatos("clientes"), 10, "Clientes") 
          elif (self.cmbBxOpcion.currentText() == "Usuarios"):
             self.mostrarDatos(varios().busquedaAvanzada("usuarios", "usuario", str(self.textBuscar.text())), self.solicitarDatos("usuarios"), 4, "Usuarios") 
          elif (self.cmbBxOpcion.currentText() == "Editoriales"):
             self.mostrarDatos(varios().busquedaAvanzada("editoriales", "cod_editorial", str(self.textBuscar.text())), self.solicitarDatos("editoriales"), 6, "Editoriales") 
          elif (self.cmbBxOpcion.currentText() == "Categorias"):
             self.mostrarDatos(varios().busquedaAvanzada("categorias", "cod_categoria", str(self.textBuscar.text())), self.solicitarDatos("categorias"), 4, "Categorias") 
          elif (self.cmbBxOpcion.currentText() == "Autores"):
             self.mostrarDatos(varios().busquedaAvanzada("autores", "cod_autor", str(self.textBuscar.text())), self.solicitarDatos("autores"), 5, "Autores") 
          elif (self.cmbBxOpcion.currentText() == "Libros"):
             self.mostrarDatos(varios().busquedaAvanzada("libros", "cod_libro", str(self.textBuscar.text())), self.solicitarDatos("libros"), 7, "Libros") 
          elif (self.cmbBxOpcion.currentText() == "Cantidad"):
             self.mostrarDatos(varios().busquedaAvanzada("cantidades", "libro", str(self.textBuscar.text())), self.solicitarDatos("cantidad"), 3, "Cantidad") 
          elif (self.cmbBxOpcion.currentText() == "Prestamos"):
             self.mostrarDatos(varios().busquedaAvanzada("prestamos", "cod_prestamo", str(self.textBuscar.text())), self.solicitarDatos("prestamos"), 5, "Prestamos") 

      def mostrarDatos(self, datos, cabeceras, numeroColumnas, nombreTabla):
          filas = datos 
          numerodefilas=len(filas)
          if (nombreTabla == "Prestamos" or nombreTabla == "Usuarios" or nombreTabla == "Cantidad"):
             self.tabla.setRowCount(numerodefilas)
          else: 
              self.tabla.setRowCount(numerodefilas+1)
          self.tabla.clear()
          self.tabla.setColumnCount(numeroColumnas)
          self.tabla.setHorizontalHeaderLabels(cabeceras)

          # variable para mostrar los datos de la BBDD a partir de la segunda fila 
          _fila = 0 

          combo_boxSexo = ['Masculino', 'Femenino'] 

          # crear celdas de la primera fila 
          for index in range(numeroColumnas):
              # asignar valores a la primera fila 
              if (nombreTabla != "Usuarios" and nombreTabla != "Cantidad"): 
                 if (nombreTabla == "Editoriales"):
                    if (cabeceras[index] == "Codigo"):
                       # obtener el valor mas alto de la columna llave primaria de la tabla editoriales, y sumarle un 1 para 
                       # establecer la que sería la nueva llave primaria 
                       if (varios().llavePrimaria("cod_editorial", "editoriales")[0] == None):
                          item = QtGui.QTableWidgetItem(str(1))
                       else: 
                          item = QtGui.QTableWidgetItem(str(varios().llavePrimaria("cod_editorial", "editoriales")[0]+1))
                       item.setFlags(QtCore.Qt.ItemIsEnabled) 
                       self.tabla.setItem(0, index, item) 
                    else: 
                       item = QtGui.QTableWidgetItem(cabeceras[index])
                       self.tabla.setItem(0, index, item) 
                 elif (nombreTabla == "Categorias"):
                    if (cabeceras[index] == "Codigo"):
                       # obtener el valor mas alto de la columna llave primaria de la tabla categorias, y sumarle un 1 para 
                       # establecer la que sería la nueva llave primaria 
                       if (varios().llavePrimaria("cod_categoria", "categorias")[0] == None):
                          item = QtGui.QTableWidgetItem(str(1))
                       else: 
                          item = QtGui.QTableWidgetItem(str(varios().llavePrimaria("cod_categoria", "categorias")[0]+1))
                       item.setFlags(QtCore.Qt.ItemIsEnabled) 
                       self.tabla.setItem(0, index, item) 
                    else: 
                       item = QtGui.QTableWidgetItem(cabeceras[index])
                       self.tabla.setItem(0, index, item) 
                 elif (nombreTabla == "Autores"):
                    if (cabeceras[index] == "Codigo"):
                       # obtener el valor mas alto de la columna llave primaria de la tabla categorias, y sumarle un 1 para 
                       # establecer la que sería la nueva llave primaria 
                       if (varios().llavePrimaria("cod_autor", "autores")[0] == None):
                          item = QtGui.QTableWidgetItem(str(1))
                       else: 
                          item = QtGui.QTableWidgetItem(str(varios().llavePrimaria("cod_autor", "autores")[0]+1))
                       item.setFlags(QtCore.Qt.ItemIsEnabled) 
                       self.tabla.setItem(0, index, item) 
                    else: 
                       item = QtGui.QTableWidgetItem(cabeceras[index])
                       self.tabla.setItem(0, index, item) 
                 elif (nombreTabla == "Libros"):
                    if (cabeceras[index] == "Codigo"):
                       # obtener el valor mas alto de la columna llave primaria de la tabla categorias, y sumarle un 1 para 
                       # establecer la que sería la nueva llave primaria 
                       if (varios().llavePrimaria("cod_libro", "libros")[0] == None):
                          item = QtGui.QTableWidgetItem(str(1))
                       else: 
                          item = QtGui.QTableWidgetItem(str(varios().llavePrimaria("cod_libro", "libros")[0]+1))
                       item.setFlags(QtCore.Qt.ItemIsEnabled) 
                       self.tabla.setItem(0, index, item) 
                    else: 
                       item = QtGui.QTableWidgetItem(cabeceras[index])
                       self.tabla.setItem(0, index, item) 
                 else:
                    item = QtGui.QTableWidgetItem(cabeceras[index])
                    self.tabla.setItem(0, index, item) 
              
              comboEdad = QtGui.QComboBox()
              comboSexo = QtGui.QComboBox()
              comboAutor = QtGui.QComboBox()
              comboCategoria = QtGui.QComboBox()
              comboEditorial = QtGui.QComboBox()
              comboLibro = QtGui.QComboBox()
              comboCantidad = QtGui.QComboBox()
              fechaNac = QtGui.QDateEdit() 
              fechaNac.setDisplayFormat('dd/MM/yyyy')
              btnRegistrar = QtGui.QPushButton("Registrar") 
              self.connect(btnRegistrar, QtCore.SIGNAL('clicked()'), self.registrarDatos)
              if (nombreTabla == "Clientes"): 
                 for i in range(10, 100):
                     comboEdad.addItem(str(i))
                 self.tabla.setCellWidget(0, 4, comboEdad)
                 self.tabla.setCellWidget(0, 7, fechaNac)
                 for t in combo_boxSexo:
                     comboSexo.addItem(t)
                 self.tabla.setCellWidget(0, 9, comboSexo)
                 self.tabla.setCellWidget(0, 12, btnRegistrar)
              elif (nombreTabla == "Editoriales"): 
                 self.tabla.setCellWidget(0, 5, btnRegistrar)
              elif (nombreTabla == "Categorias"): 
                 self.tabla.setCellWidget(0, 3, btnRegistrar)
              elif (nombreTabla == "Autores"): 
                 self.tabla.setCellWidget(0, 4, btnRegistrar)
              elif (nombreTabla == "Libros"): 
                 for a in varios().solicitarDatos("cod_autor", "autores"):
                     comboAutor.addItem(str(a[0]))
                 self.tabla.setCellWidget(0, 3, comboAutor)
                 for c in varios().solicitarDatos("cod_categoria", "categorias"):
                     comboCategoria.addItem(str(c[0]))
                 self.tabla.setCellWidget(0, 4, comboCategoria)
                 for e in varios().solicitarDatos("cod_editorial", "editoriales"):
                     comboEditorial.addItem(str(e[0]))
                 self.tabla.setCellWidget(0, 5, comboEditorial)
                 self.tabla.setCellWidget(0, 6, btnRegistrar)

          if (nombreTabla != "Usuarios" and nombreTabla != "Cantidad" and nombreTabla != "Prestamos"): 
             # asignar color a la primera fila 
             for j in range(self.tabla.columnCount()):
                 self.tabla.item(0, j).setBackground(QtGui.QColor('yellow')) 

          # crear botón para realizar modificación 
          btnModificar = QtGui.QPushButton("Modificar")
          self.connect(btnModificar, QtCore.SIGNAL('clicked()'), self.modificarDatos)

          # cargar datos en la tabla a partir de la segunda fila 
          for j in range(numerodefilas):
              fila = filas[j]
              _fila = 1 + _fila
              for i in range(0,len(fila)):
                  elemento = fila[i]
                  elemento = str(elemento)
                  if elemento == 'None' : elemento = ' '
                  item=None
                  item = QtGui.QTableWidgetItem()
                  #item.setText(QtGui.QApplication.translate(nombreTabla, str(elemento), None, QtGui.QApplication.UnicodeUTF8))

                  # hacer la primer celda de la segunda fila de solo lectura
                  if (i == 0):
                     if (_fila == 1): 
                        item.setFlags(QtCore.Qt.ItemIsEnabled) 
                        item.setText(QtGui.QApplication.translate(nombreTabla, str(elemento), None, QtGui.QApplication.UnicodeUTF8))
                     else:
                        item.setText(QtGui.QApplication.translate(nombreTabla, str(elemento), None, QtGui.QApplication.UnicodeUTF8))
                  else:
                     item.setText(QtGui.QApplication.translate(nombreTabla, str(elemento), None, QtGui.QApplication.UnicodeUTF8))

                  if (nombreTabla == "Clientes"): 
                     if (i == 4):
                        if (_fila == 1):
                           comboEdad = QtGui.QComboBox()
                           for e in range(10, 100):
                               comboEdad.addItem(str(e))
                           self.tabla.setCellWidget(1, 4, comboEdad)
                           comboEdad.setCurrentIndex(int(elemento)-10)
                     if (i ==7):
                        if (_fila == 1):
                           datosFecha = [3]
                           datosFecha = elemento.split('/') 
                           day = datosFecha[0]
                           month = datosFecha[1]
                           year = datosFecha[2]
                           fechaNac = QtGui.QDateEdit() 
                           fechaNac.setDisplayFormat('dd/MM/yyyy')
                           fechaNac.setDate(QtCore.QDate(int(year), int(month), int(day))) 
                           # asignar fecha actual 
                           #fechaNac.setDate(QtCore.QDate.currentDate()) 
                           self.tabla.setCellWidget(1, 7, fechaNac)
                     if (i == 9):
                        comboSexo = QtGui.QComboBox()
                        for s in combo_boxSexo:
                            comboSexo.addItem(s)
                        self.tabla.setCellWidget(1, 9, comboSexo)
                        if (elemento == "Femenino"):
                           comboSexo.setCurrentIndex(1)
                     # hacer la celda de solo lectura, celda del nombre de usuario 
                     if (i == 10):
                        if (_fila == 1): 
                           item.setFlags(QtCore.Qt.ItemIsEnabled) 
                     # insertar botón en la celda 12 de la segunda fila 
                     if (i == 11):
                        if (_fila == 1): 
                           self.tabla.setCellWidget(1, 12, btnModificar) 
                     self.tabla.setItem(_fila,i-0,item)
                  elif (nombreTabla == "Usuarios"): 
                     # hacer la celda de solo lectura
                     if (i == 2):
                        if (_fila == 1): 
                           item.setFlags(QtCore.Qt.ItemIsEnabled) 
                     # insertar botón de modificar 
                     if (i == 1):
                        if (_fila == 1): 
                           self.tabla.setCellWidget(0, 3, btnModificar) 
                     self.tabla.setItem(_fila-1,i-0,item)
                  elif (nombreTabla == "Editoriales"): 
                     # insertar botón de modificar 
                     if (i == 1):
                        if (_fila == 1): 
                           self.tabla.setCellWidget(_fila, 5, btnModificar) 
                     self.tabla.setItem(_fila,i-0,item)
                     #self.connect(btnModificar, QtCore.SIGNAL('clicked()'), self.seleccionarDatos)
                  elif (nombreTabla == "Categorias"): 
                     # insertar botón de modificar 
                     if (i == 1):
                        if (_fila == 1): 
                           self.tabla.setCellWidget(_fila, 3, btnModificar) 
                     self.tabla.setItem(_fila,i-0,item)
                  elif (nombreTabla == "Autores"): 
                     # insertar botón de modificar 
                     if (i == 1):
                        if (_fila == 1): 
                           self.tabla.setCellWidget(_fila, 4, btnModificar) 
                     self.tabla.setItem(_fila,i-0,item)
                  elif (nombreTabla == "Libros"): 
                     # insertar botón de modificar 
                     if (i == 1):
                        if (_fila == 1): 
                           self.tabla.setCellWidget(_fila, 6, btnModificar) 
                     if (i == 3):
                        if (_fila == 1): 
                           comboAutor = QtGui.QComboBox()
                           for a in varios().solicitarDatos("cod_autor", "autores"):
                               comboAutor.addItem(str(a[0]))
                           self.tabla.setCellWidget(_fila, 3, comboAutor)
                           comboAutor.setCurrentIndex(int(elemento)-1)
                     if (i == 4):
                        if (_fila == 1): 
                           comboCategoria = QtGui.QComboBox()
                           for c in varios().solicitarDatos("cod_categoria", "categorias"):
                               comboCategoria.addItem(str(c[0]))
                           self.tabla.setCellWidget(_fila, 4, comboCategoria)
                           comboCategoria.setCurrentIndex(int(elemento)-1)
                     if (i == 5):
                        if (_fila == 1): 
                           comboEditorial = QtGui.QComboBox()
                           for e in varios().solicitarDatos("cod_editorial", "editoriales"):
                               comboEditorial.addItem(str(e[0]))
                           self.tabla.setCellWidget(_fila, 5, comboEditorial)
                           comboEditorial.setCurrentIndex(int(elemento)-1)
                     self.tabla.setItem(_fila,i-0,item)
                  elif (nombreTabla == "Cantidad"): 
                     if (i == 1):
                        if (_fila == 1):
                           comboCantidad = QtGui.QComboBox()
                           for c in range(1, 6):
                               comboCantidad.addItem(str(c))
                           self.tabla.setCellWidget(_fila-1, 1, comboCantidad)
                           comboCantidad.setCurrentIndex(int(elemento)-1)
                     # insertar botón de modificar 
                     if (i == 1):
                        if (_fila == 1): 
                           self.tabla.setCellWidget(0, 2, btnModificar) 
                     self.tabla.setItem(_fila-1,i-0,item)
                  elif (nombreTabla == "Prestamos"): 
                     # todas las celdas son readonly(solo lectura) 
                     item.setFlags(QtCore.Qt.ItemIsEnabled) 
                     self.tabla.setItem(_fila-1,i-0,item)

          if (nombreTabla == "Usuarios"): 
             # asignar color a la primera fila 
             if (int(self.tabla.rowCount()) > 0): # es numero de filas mayor que 0 
                for j in range(0, 3):
                    self.tabla.item(0, j).setBackground(QtGui.QColor('light blue')) 
          elif (nombreTabla == "Cantidad"): 
             # asignar color a la primera fila 
             if (int(self.tabla.rowCount()) > 0): # es numero de filas mayor que 0 
                for j in range(0, 1):
                    self.tabla.item(0, j).setBackground(QtGui.QColor('light blue')) 
          else: 
             if (nombreTabla != "Prestamos"): 
                if (int(self.tabla.rowCount()) > 1): # es numero de filas mayor que 1 
                   # asignar color a la segunda fila 
                   for j in range(self.tabla.columnCount()-1):
                       self.tabla.item(1, j).setBackground(QtGui.QColor('light blue')) 
             elif (nombreTabla == "Prestamos"): 
                # recorrer columna correspondiente a la fecha de devolucion 
                for j in range(self.tabla.columnCount()-1):
                    # comparar fecha actual con fecha obtenidad de la base de datos 
                    # si fecha de la base de datos es mayor que la fecha actual 
                    if (datetime.strptime(str(self.tabla.item(j, 4).text()), '%Y-%m-%d') < datetime.strptime(str(date.today()), '%Y-%m-%d')):
                       # asignar color a las filas donde han pasado tres dias 
                       for i in range(self.tabla.columnCount()):
                           self.tabla.item(j, i).setBackground(QtGui.QColor('red')) 

      def registrarDatos(self):
          #seleccionar datos de la tabla (QTableWidget)
          datos = []
          datosUsuario = [] # lista para guardar los datos de la tabla usuarios (usuario, clave, cedula) 
          guardarCedula = False # permitir que se añada cedula a la lista datosUsuario 
          realizarRegistro = True
          allColumns = self.tabla.columnCount()
          for column in xrange(0, allColumns-1):
              if (self.cmbBxOpcion.currentText() == "Clientes"):
                 # datos de cliente 
                 if (column < 10): # es column menor que 10
                    if (column == 0): 
                       # validar que cedula corresponda a un número 
                       try: 
                          datos.append(int(self.tabla.item(0, column).text()))
                          cedula = int(self.tabla.item(0, column).text()) # seleccionar cedula para posteriormente añadirla a la lista datosUsuario 
                       except Exception, e: 
                          QtGui.QMessageBox.information(self, "", "Error a digitar la cedula",
                          QtGui.QMessageBox.Ok) 
                          realizarRegistro = False 
                          break
                    elif (column == 4 or column == 9):
                       # obtener valores del qcombobox correspondiente 
                       datos.append(str(self.tabla.cellWidget(0, column).currentText()))
                    elif (column == 7):
                       # obtener fecha de la celda correspodiente 
                       # se utiliza el método textFromDateTime que devuelve un string pasandole una fecha, la fecha contenida en la celda 
                       # de la tabla correspondiente a la columna fecha de la tabla en la base de datos 
                       datos.append(str(self.tabla.cellWidget(0, column).textFromDateTime(self.tabla.cellWidget(0, column).dateTime())))
                    else:
                       datos.append(str(self.tabla.item(0, column).text()))
                 # datos de usuario 
                 else:
                    datosUsuario.append(str(self.tabla.item(0, column).text()))
                    if (column == 11):
                       # columna 11 corresponde a clave, posteriormente permitir añadir cedula a lista datosUsuario 
                       guardarCedula = True 
                    if (guardarCedula == True): 
                       datosUsuario.append(cedula) 
              elif (self.cmbBxOpcion.currentText() == "Editoriales"):
                   if (column == 0): 
                      datos.append(int(self.tabla.item(0, column).text()))
                   else: 
                      datos.append(str(self.tabla.item(0, column).text()))
              elif (self.cmbBxOpcion.currentText() == "Categorias"):
                   if (column == 0): 
                      datos.append(int(self.tabla.item(0, column).text()))
                   else: 
                      datos.append(str(self.tabla.item(0, column).text()))
              elif (self.cmbBxOpcion.currentText() == "Autores"):
                   if (column == 0): 
                      datos.append(int(self.tabla.item(0, column).text()))
                   else: 
                      datos.append(str(self.tabla.item(0, column).text()))
              elif (self.cmbBxOpcion.currentText() == "Libros"):
                   if (column == 0): 
                      datos.append(int(self.tabla.item(0, column).text()))
                   elif (column == 3 or column == 4 or column == 5):
                      # obtener valores del qcombobox correspondiente 
                      datos.append(int(self.tabla.cellWidget(0, column).currentText()))
                   else: 
                      datos.append(str(self.tabla.item(0, column).text()))

          if (self.cmbBxOpcion.currentText() == "Clientes"):
             if (realizarRegistro == True):
                QtGui.QMessageBox.information(self, "", cliente().registrarClienteUsuario(datos, datosUsuario),
                QtGui.QMessageBox.Ok) 
                self.mostrarDatos(cliente().mostrarCliente_Usuario(), self.solicitarDatos("clientes"), 13, "Clientes")
                self.proveedor(varios().solicitarDatos("cedula", "clientes"), "cedula")
          elif (self.cmbBxOpcion.currentText() == "Editoriales"):
             QtGui.QMessageBox.information(self, "", editorial().registrarEditorial(datos),
             QtGui.QMessageBox.Ok) 
             self.mostrarDatos(editorial().mostrarEditorial(), self.solicitarDatos("editoriales"), 6, "Editoriales")
             self.proveedor(varios().solicitarDatos("cod_editorial", "editoriales"), "cod. Editorial")
          elif (self.cmbBxOpcion.currentText() == "Categorias"):
             QtGui.QMessageBox.information(self, "", categoria().registrarCategoria(datos),
             QtGui.QMessageBox.Ok) 
             self.mostrarDatos(categoria().mostrarCategoria(), self.solicitarDatos("categorias"), 4, "Categorias")
             self.proveedor(varios().solicitarDatos("cod_categoria", "categorias"), "cod. Categoria")
          elif (self.cmbBxOpcion.currentText() == "Autores"):
             QtGui.QMessageBox.information(self, "", autor().registrarAutor(datos),
             QtGui.QMessageBox.Ok) 
             self.mostrarDatos(autor().mostrarAutor(), self.solicitarDatos("autores"), 5, "Autores")
             self.proveedor(varios().solicitarDatos("cod_autor", "autores"), "cod. Autor")
          elif (self.cmbBxOpcion.currentText() == "Libros"):
             QtGui.QMessageBox.information(self, "", libro().registrarLibro(datos),
             QtGui.QMessageBox.Ok) 
             self.mostrarDatos(libro().mostrarLibro(), self.solicitarDatos("libros"), 7, "Libros")
             self.proveedor(varios().solicitarDatos("libro", "cantidades"), "Libro")

      def modificarDatos(self):
          #seleccionar datos de la tabla (QTableWidget)
          datos = []
          datosUsuario = [] # lista para guardar los datos de la tabla usuarios (usuario, clave, cedula) 
          allColumns = self.tabla.columnCount()
          for column in xrange(0, allColumns-1):
              if (self.cmbBxOpcion.currentText() == "Clientes"):
                 # datos de cliente 
                 if (column < 10): 
                    if (column == 0): 
                       #datos.append(int(self.tabla.item(1, column).text()))
                       cedula = int(self.tabla.item(1, column).text()) # seleccionar cedula para posteriormente añadirla a la lista datosUsuario 
                    elif (column == 4 or column == 9):
                       # obtener valores del qcombobox correspondiente 
                       datos.append(str(self.tabla.cellWidget(1, column).currentText()))
                    elif (column == 7):
                       # obtener fecha de la celda correspodiente 
                       # se utiliza el método textFromDateTime que devuelve un string pasandole una fecha, la fecha contenida en la celda 
                       # de la tabla correspondiente a la columna fecha de la tabla en la base de datos 
                       datos.append(str(self.tabla.cellWidget(1, column).textFromDateTime(self.tabla.cellWidget(1, column).dateTime())))
                    else:
                       datos.append(str(self.tabla.item(1, column).text()))
                 # datos de usuario 
                 else:
                    if (column == 10):
                       # añadir cedula (último elemento) a la lista correspondiente a usuario 
                       datos.append(cedula)
                       # añadir clave (primer elemento) a la lista correspondiente a usuario 
                       datosUsuario.append(str(self.tabla.item(1, 11).text()))
                    else:
                       # añadir nombre de usuario a la lista
                       datosUsuario.append(str(self.tabla.item(1, 10).text()))
              elif (self.cmbBxOpcion.currentText() == "Usuarios"):
                   if (column == 0): 
                      nombreUsuario = str(self.tabla.item(0, column).text()) # seleccionar nombre de usuario para usarlo como parametro de busqueda 
                   elif ( column == 1):
                      # validar que el usuario digite una clave, si no digita una clave se asignará 
                      # el nombre de usuario como nueva clave 
                      if (str(self.tabla.item(0, column).text()) == ""): 
                         datos.append(nombreUsuario) # añadir nombre de usuario como clave 
                      else: 
                         datos.append(str(self.tabla.item(0, column).text())) # añadir clave 
                      datos.append(nombreUsuario)
              elif (self.cmbBxOpcion.currentText() == "Editoriales"):
                   if (column < 4): 
                      if (column == 0): 
                         cod_editorial = int(self.tabla.item(1, column).text()) 
                      else: 
                         datos.append(str(self.tabla.item(1, column).text()))
                   else: 
                      datos.append(str(self.tabla.item(1, column).text()))
                      datos.append(cod_editorial)
              elif (self.cmbBxOpcion.currentText() == "Categorias"):
                   if (column < 2): 
                      if (column == 0): 
                         cod_categoria = int(self.tabla.item(1, column).text()) 
                      else: 
                         datos.append(str(self.tabla.item(1, column).text()))
                   else: 
                      datos.append(str(self.tabla.item(1, column).text()))
                      datos.append(cod_categoria)
              elif (self.cmbBxOpcion.currentText() == "Autores"):
                   if (column < 3): 
                      if (column == 0): 
                         cod_autor = int(self.tabla.item(1, column).text()) 
                      else: 
                         datos.append(str(self.tabla.item(1, column).text()))
                   else: 
                      datos.append(str(self.tabla.item(1, column).text()))
                      datos.append(cod_autor)
              elif (self.cmbBxOpcion.currentText() == "Libros"):
                   if (column < 5):
                      if (column == 0): 
                         cod_libro = int(self.tabla.item(1, column).text()) 
                      elif (column == 3 or column == 4 or column == 5):
                         # obtener valores del qcombobox correspondiente 
                         datos.append(int(self.tabla.cellWidget(1, column).currentText()))
                      else: 
                         datos.append(str(self.tabla.item(1, column).text()))
                   else: 
                      datos.append(int(self.tabla.cellWidget(1, column).currentText()))
                      datos.append(cod_libro) 
              elif (self.cmbBxOpcion.currentText() == "Cantidad"):
                   if (column == 0):
                      cod_libro = int(self.tabla.item(0, column).text()) 
                   else: 
                      datos.append(int(self.tabla.cellWidget(0, column).currentText()))
                      datos.append(cod_libro) 

          if (self.cmbBxOpcion.currentText() == "Clientes"):
             QtGui.QMessageBox.information(self, "", cliente().modificarClienteUsuario(datos, datosUsuario),
             QtGui.QMessageBox.Ok) 
             self.mostrarDatos(cliente().buscarCliente_Usuario([cedula, cedula]), self.solicitarDatos("clientes"), 13, "Clientes")
          elif (self.cmbBxOpcion.currentText() == "Usuarios"):
             QtGui.QMessageBox.information(self, "", usuario().modificarUsuario(datos),
             QtGui.QMessageBox.Ok) 
             self.mostrarDatos(usuario().buscarUsuario([nombreUsuario]), self.solicitarDatos("usuarios"), 4, "Usuarios")
          elif (self.cmbBxOpcion.currentText() == "Editoriales"):
             QtGui.QMessageBox.information(self, "", editorial().modificarEditorial(datos),
             QtGui.QMessageBox.Ok) 
             self.mostrarDatos(editorial().buscarEditorial([cod_editorial]), self.solicitarDatos("editoriales"), 6, "Editoriales")
          elif (self.cmbBxOpcion.currentText() == "Categorias"):
             QtGui.QMessageBox.information(self, "", categoria().modificarCategoria(datos),
             QtGui.QMessageBox.Ok) 
             self.mostrarDatos(categoria().buscarCategoria([cod_categoria]), self.solicitarDatos("categorias"), 4, "Categorias")
          elif (self.cmbBxOpcion.currentText() == "Autores"):
             QtGui.QMessageBox.information(self, "", autor().modificarAutor(datos),
             QtGui.QMessageBox.Ok) 
             self.mostrarDatos(autor().buscarAutor([cod_autor]), self.solicitarDatos("autores"), 5, "Autores")
          elif (self.cmbBxOpcion.currentText() == "Libros"):
             QtGui.QMessageBox.information(self, "", libro().modificarLibro(datos),
             QtGui.QMessageBox.Ok) 
             self.mostrarDatos(libro().buscarLibro([cod_libro]), self.solicitarDatos("libros"), 7, "Libros")
          elif (self.cmbBxOpcion.currentText() == "Cantidad"):
             QtGui.QMessageBox.information(self, "", cantidad().modificarCantidad(datos),
             QtGui.QMessageBox.Ok) 
             self.mostrarDatos(cantidad().buscarCantidad([cod_libro]), self.solicitarDatos("cantidad"), 3, "Cantidad")

# no permitir valores nulos 

######################################## Iniciar Programa ############################################
#app = QtGui.QApplication(sys.argv)
#programa = administrador(None)
#programa.show()
#app.exec_()
######################################################################################################
