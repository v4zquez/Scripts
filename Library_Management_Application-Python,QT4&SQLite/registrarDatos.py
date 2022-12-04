#!/usr/bin/env python 
# -*- coding: utf-8 -*- 

import sys, os

from PyQt4 import QtCore, QtGui, uic, Qt
from PyQt4.QtGui import QDialog

from controlador import usuario, cliente 

#cargar archivo .ui
formularioRegistrar = uic.loadUiType("registrarDatos.ui")[0]
 
class registrarDatos(QtGui.QDialog, formularioRegistrar):
      def __init__(self, parent=None):
     	  QtGui.QMainWindow.__init__(self, parent)
  	  self.setupUi(self)
   	  self.btnRegistrar.clicked.connect(self.btnRegistrar_clicked)
   	  self.btnCancelar.clicked.connect(self.btnCancelar_clicked)
          self.agregarTexto()

      def agregarTexto(self):
          self.textCedula.setText("Cedula") 
          self.textNombre.setText("Nombre") 
          self.textApellido1.setText("Primer Apellido") 
          self.textApellido2.setText("Segundo Apellido") 
          self.textDireccion.setText("Direccion") 
          self.textTelefono.setText("Telefono") 
          self.textEmail.setText("E-mail") 
          self.textUsuario.setText("Usuario") 
          self.textClave.setText("Clave") 
          self.cmboxEdad.setCurrentIndex(0) 
          self.cmboxSexo.setCurrentIndex(0) 

          for i in range(10, 100):
              self.cmboxEdad.addItem(str(i)) 

      def btnRegistrar_clicked(self): 
          self.cedula = int(self.textCedula.text())
          self.nombre = str(self.textNombre.text())
          self.apellido1 = str(self.textApellido1.text())
          self.apellido2 = str(self.textApellido2.text())
          self.direccion = str(self.textDireccion.text())
          self.telefono = str(self.textTelefono.text())
          self.email = str(self.textEmail.text())
          self.edad = str(self.cmboxEdad.currentText())
          self.sexo = str(self.cmboxSexo.currentText())
          self.fechaNac = str(self.dateEdtFecha.textFromDateTime(self.dateEdtFecha.dateTime()))
          self.usuario = str(self.textUsuario.text())
          self.clave = str(self.textClave.text())
 
          datos = [self.cedula, self.nombre, self.apellido1, self.apellido2, self.edad, self.direccion, self.telefono, self.fechaNac, self.email, self.sexo]
          datosUsuario = [self.usuario, self.clave, self.cedula]

          QtGui.QMessageBox.information(self, "", cliente().registrarClienteUsuario(datos, datosUsuario),
          QtGui.QMessageBox.Ok)

          self.agregarTexto()

      def btnCancelar_clicked(self): 
          self.close() 
              
######################################## Iniciar Programa ############################################
#app = QtGui.QApplication(sys.argv)
#programa = registrarDatos(None)
#programa.show()
#app.exec_()
######################################################################################################
