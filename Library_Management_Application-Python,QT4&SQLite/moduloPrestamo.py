#!/usr/bin/env python 
# -*- coding: utf-8 -*- 

import sys, os
from datetime import date, datetime, timedelta 

from PyQt4 import QtCore, QtGui, uic, Qt
from PyQt4.QtGui import QDialog, QMainWindow

# importar módulos 
from controlador import libro, varios, usuario, cantidad, prestamo 
from registrarDatos import registrarDatos 
from administrador import administrador

# cargar archivo .ui
formularioPrestamo = uic.loadUiType("moduloPrestamo.ui")[0]

class moduloPrestamo(QtGui.QMainWindow, formularioPrestamo):
      def __init__(self, parent=None):
     	  QtGui.QMainWindow.__init__(self, parent)

          # el método setupUi crea los Widgets y configura cada objecto que se necesitará 
  	  self.setupUi(self)
 
          # asignar fechas necesarias 
          self.lbl_prestamo.setText(self.lbl_prestamo.text() + "     " + str(date.today())) 
          self.lbl_devolucion.setText(self.lbl_devolucion.text() + "  " + str(date.today() + timedelta(days=3))) 

          self.btnRegistrar.clicked.connect(self.registrar_cliente)
          self.btnSalir.clicked.connect(self.btnSalir_clicked)

          # llenar qcombobox para mostrar los nombres de las tablas  
          for index in range(0, len(self.solicitarDatos("opciones"))):
              self.cmbBox_buscar.addItem(str(self.solicitarDatos("opciones")[index]))

          # caja de texto para realizar la busqueda avanzada
          self.textBuscar.setText("Buscar ...")
          # cuando se presione  -> enter <- sobre la caja de texto se ejecutará el método -> busquedaAvanzada
          self.textBuscar.returnPressed.connect(self.realizar_busquedaAvanzada)

          self.text_clave.returnPressed.connect(self.login) 

          self.proveedor(varios().solicitarDatos("nombre", "libros"), "Libro", "libros")
          self.cmbBox_libro.activated['int'].connect(self.buscado)

          self.mostrarDatos(libro().mostrarLibro_Cantidad(), self.solicitarDatos("libros")) 

          self.permitirPrestamo = False 

      def btnSalir_clicked(self):
          reply = QtGui.QMessageBox.question(self, "Mensaje", "Seguro quiere salir?", QtGui.QMessageBox.Yes, QtGui.QMessageBox.No)
          if reply == QtGui.QMessageBox.Yes:
             # cerrar programa
             sys.exit()

      def registrar_cliente(self): 
          # mostrar formulario de registro de cliente 
          self.ventanaRegistro = registrarDatos()
          self.ventanaRegistro.show()

      def login(self):
          self.usuario = str(self.text_usuario.text())
          self.clave = str(self.text_clave.text())

          if (usuario().validarCuentaUsuario([self.usuario, self.clave])[0]):
             if (self.usuario == 'admin' ):
                # mostrar formulario de administrador
                self.ventanaAdministrador = administrador()
                self.ventanaAdministrador.show()
             else:
                QtGui.QMessageBox.information(self, "", """Usuario: \n""" + self.usuario,
                QtGui.QMessageBox.Ok)

                self.cedula = int((varios().obtenerCliente(self.usuario)[0])[0]) 
                self.nombre = str((varios().obtenerCliente(self.usuario)[0])[1]) 
                self.apellido = str((varios().obtenerCliente(self.usuario)[0])[2]) 
                self.cliente = self.nombre + " " + self.apellido 

                self.lbl_cliente.setText(self.cliente) 

                self.mostrarDatos_prestamos(prestamo().buscarPrestamo_cliente([self.cedula]), self.solicitarDatos("prestamos")) 
                self.proveedor(varios().solicitarDatos_prestamo([self.cedula]), "Cod. Prestamo", "prestamos")
                self.cmbBox_prestamo.activated['int'].connect(self.buscarPrestamo)

                self.mostrarDatos(libro().mostrarLibro_Cantidad(), self.solicitarDatos("libros")) 

                self.permitirPrestamo = True 
          else:
             QtGui.QMessageBox.information(self, "", """Datos Incorrectos""",
             QtGui.QMessageBox.Ok)
 
          # llenar qcombobox con datos suministrados 
      def proveedor(self, dato, columna, tabla): 
          if (tabla == "libros"):
             # añadir como primer elemento el nombre de la columna 
             self.cmbBox_libro.addItem(columna)
             # recorrer la lista -> dato <-, e ir añadiendo cada elemento al qcombobox 
             for i in dato:
                 self.cmbBox_libro.addItem(str(i[0]))
          else:
             self.cmbBox_prestamo.clear() 
             # añadir como primer elemento el nombre de la columna 
             self.cmbBox_prestamo.addItem(columna)
             # recorrer la lista -> dato <-, e ir añadiendo cada elemento al qcombobox 
             for i in dato:
                 self.cmbBox_prestamo.addItem(str(i[0]))

      def buscado(self, indice):
          # validar que opción seleccionada no sea el nombre de la columna
          if (indice != 0):
             if (isinstance(indice, int)):
                # guardar el valor seleccionado en el qcombobox
                valor = str(self.cmbBox_libro.currentText())
                self.mostrarDatos(libro().buscarLibro_nombre([valor]), self.solicitarDatos("libros")) 
                # mostrar en el qcombobox el primer elemento
                self.cmbBox_libro.setCurrentIndex(0)

      def buscarPrestamo(self, indice):
          if (indice == 0):
             self.mostrarDatos_prestamos(prestamo().buscarPrestamo_cliente([self.cedula]), self.solicitarDatos("prestamos")) 
          else: 
             if (isinstance(indice, int)):
                # guardar el valor seleccionado en el qcombobox
                valor = int(self.cmbBox_prestamo.currentText())
                self.mostrarDatos_prestamos(prestamo().buscarPrestamo_codPrestamo([valor]), self.solicitarDatos("prestamos")) 
                # mostrar en el qcombobox el primer elemento
                self.cmbBox_prestamo.setCurrentIndex(0)

      def solicitarDatos(self, datos): 
          if (datos == "libros"):
             return ['Codigo', 'Nombre', 'Descripcion', 'Autor', 'Categoria', 'Editorial', 'Cantidad', 'Accion']
          elif (datos == "prestamos"):
             return ['Codigo','Cliente', 'Libro', 'Prestamo', 'Devolucion', 'Accion']
          # datos para llenar el qcombobox
          elif (datos == "opciones"):
             return ['nombre', 'autor', 'categoria']

      def realizar_busquedaAvanzada(self):
          if (self.cmbBox_buscar.currentText() == "nombre"): 
             self.mostrarDatos(varios().busquedaAvanzadaLibro_nombre(str(self.textBuscar.text())), self.solicitarDatos("libros"))
          elif (self.cmbBox_buscar.currentText() == "autor"): 
             self.mostrarDatos(varios().busquedaAvanzadaLibro_autor(str(self.textBuscar.text())), self.solicitarDatos("libros"))
          else: 
             self.mostrarDatos(varios().busquedaAvanzadaLibro_categoria(str(self.textBuscar.text())), self.solicitarDatos("libros"))

      def solicitarPrestamo(self):
          if (self.permitirPrestamo == True): 
             datos = []
             datos.append(self.cedula)
             datos.append(int(self.tabla.item(0, 0).text()))
             datos.append(str(date.today())) 
             datos.append(str(date.today() + timedelta(days=3))) 
             if (cantidad().verificarExistencia([int(self.tabla.item(0, 0).text())])[0] > 0):
                QtGui.QMessageBox.information(self, "", prestamo().registrarPrestamo(datos),
                QtGui.QMessageBox.Ok) 
                self.mostrarDatos_prestamos(prestamo().buscarPrestamo_cliente([self.cedula]), self.solicitarDatos("prestamos")) 
                self.proveedor(varios().solicitarDatos("cod_prestamo", "prestamos"), "Cod. Prestamo", "prestamos")

                self.mostrarDatos(libro().mostrarLibro_Cantidad(), self.solicitarDatos("libros")) 
             else: 
                QtGui.QMessageBox.information(self, "", """Cantidad de unidades insuficientes""",
                QtGui.QMessageBox.Ok)
          else:
             QtGui.QMessageBox.information(self, "", """Necesita iniciar sesion""",
             QtGui.QMessageBox.Ok)

      def devolucionLibro(self): 
          # obtener nombre de libro para posteriormente obtener su codigo 
          self.nombreLibro = str(self.tablaPrestamo.item(0, 2).text())
          cantidad().agregarDevolucion([self.nombreLibro])

          # eliminar prestamo seleccionado
          self.codPrestamo = int(self.tablaPrestamo.item(0, 0).text()) 
          prestamo().eliminarPrestamo([self.codPrestamo]) 

          QtGui.QMessageBox.information(self, "", """Devolucion realizada""",
          QtGui.QMessageBox.Ok)

          # actualizar tablas
          self.mostrarDatos_prestamos(prestamo().buscarPrestamo_cliente([self.cedula]), self.solicitarDatos("prestamos")) 
          self.proveedor(varios().solicitarDatos("cod_prestamo", "prestamos"), "Cod. Prestamo", "prestamos")
          self.mostrarDatos(libro().mostrarLibro_Cantidad(), self.solicitarDatos("libros")) 

      def mostrarDatos(self, datos, encabezados):
          filas = datos 
          numeroFilas=len(datos)
          self.tabla.setRowCount(numeroFilas)
          self.tabla.setColumnCount(8)
          self.tabla.setHorizontalHeaderLabels(encabezados)

          # crear botón para solicitar prestamo 
          btnPrestamo = QtGui.QPushButton("Solicitar")
          self.connect(btnPrestamo, QtCore.SIGNAL('clicked()'), self.solicitarPrestamo)

          for j in range(numeroFilas):
              # De esta manera siempre se agregan al final
              fila = filas[j]
              for i in range(0,len(fila)):
                  elemento = fila[i]
                  elemento = str(elemento)
                  if elemento == 'None' : elemento = ' '
                  item=None
                  item = QtGui.QTableWidgetItem()
                  item.setFlags(QtCore.Qt.ItemIsEnabled)
                  item.setText(QtGui.QApplication.translate("Libros", str(elemento), None, QtGui.QApplication.UnicodeUTF8))
                  self.tabla.setItem(j,i-0,item)
                  if (j == 0): 
                     if (i == 4):
                        self.tabla.setCellWidget(0, 7, btnPrestamo) 
 
          # asignar color a la primera fila
          for j in range(0, 7):
              self.tabla.item(0, j).setBackground(QtGui.QColor('light blue')) 

      def mostrarDatos_prestamos(self, datos, encabezados):
          filas = datos 
          numeroFilas=len(datos)
          self.tablaPrestamo.setRowCount(numeroFilas)
          self.tablaPrestamo.setColumnCount(6)
          self.tablaPrestamo.setHorizontalHeaderLabels(encabezados)

          # crear botón para realizar devolucion 
          btnDevolucion = QtGui.QPushButton("Devolver")
          self.connect(btnDevolucion, QtCore.SIGNAL('clicked()'), self.devolucionLibro)

          for j in range(numeroFilas):
              # De esta manera siempre se agregan al final
              fila = filas[j]
              for i in range(0,len(fila)):
                  elemento = fila[i]
                  elemento = str(elemento)
                  if elemento == 'None' : elemento = ' '
                  item=None
                  item = QtGui.QTableWidgetItem()
                  item.setFlags(QtCore.Qt.ItemIsEnabled)
                  item.setText(QtGui.QApplication.translate("Libros", str(elemento), None, QtGui.QApplication.UnicodeUTF8))
                  self.tablaPrestamo.setItem(j,i-0,item)
                  if (j == 0): 
                     if (i == 4):
                        self.tablaPrestamo.setCellWidget(0, 5, btnDevolucion) 
 
          # asignar color a la primera fila
          if (int(self.tablaPrestamo.rowCount()) > 0): # es numero de filas mayor que 0
             for j in range(0, 5):
                 self.tablaPrestamo.item(0, j).setBackground(QtGui.QColor('light green')) 

######################################## Iniciar Programa ############################################
if __name__ == '__main__': 
   app = QtGui.QApplication(sys.argv)
   programa = moduloPrestamo()
   programa.show()
   sys.exit(app.exec_())
######################################################################################################

# no se debe usar QtWidgets, se debe usar QtGui
