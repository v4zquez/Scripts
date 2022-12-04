#!/usr/bin/env python 
# -*- coding: utf-8 -*- 

import sys, os

from PyQt4 import QtCore, QtGui, uic, Qt
from PyQt4.QtGui import QDialog

from controlador import libro, varios 

#cargar archivo .ui
formularioInformacion = uic.loadUiType("infoLibro.ui")[0]
 
class infoLibro(QtGui.QMainWindow, formularioInformacion):
      def __init__(self, parent=None):
     	  QtGui.QMainWindow.__init__(self, parent)
  	  self.setupUi(self)

          self.btnSalir.clicked.connect(self.btnSalir_clicked) 

          # añadir nombre de libros a la lista 
          for item in varios().solicitarDatos('nombre', 'libros'): 
              self.listWget_libros.addItems(item)
          self.listWget_libros.itemSelectionChanged.connect(self.informacionLibro) 

      def btnSalir_clicked(self):
          self.close() 

      def informacionLibro(self): 
          libro_ = str(self.listWget_libros.currentItem().text()) 
          datos = libro().mostrarInformacion_Libro([libro_])
          numeroFilas=len(datos)
          self.tablaInfo.setRowCount(6)
          self.tablaInfo.setColumnCount(1)

          # columna j -> 0
          for j in range(numeroFilas):
              # De esta manera siempre se agregan al final
              fila = datos[j]
              # fila i -> 0, 5 
              for i in range(0,len(fila)):
                  elemento = fila[i]
                  elemento = str(elemento)
                  if elemento == 'None' : elemento = ' '
                  item = None
                  item = QtGui.QTableWidgetItem()
                  item.setFlags(QtCore.Qt.ItemIsEnabled)
                  item.setText(QtGui.QApplication.translate("Libros", str(elemento), None, QtGui.QApplication.UnicodeUTF8))
                  self.tablaInfo.setItem(i,j,item)

######################################## Iniciar Programa ############################################
#app = QtGui.QApplication(sys.argv)
#programa = infoLibro(None)
#programa.show()
#app.exec_()
######################################################################################################
