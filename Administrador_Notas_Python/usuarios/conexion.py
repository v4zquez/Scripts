#!/usr/bin/env python
# - * - coding: latin-1 - * -

import sqlite3

def conectar(): 
    conexion = sqlite3.connect("proyectoPython.db")
    cursor = conexion.cursor() 
    return [conexion, cursor] 
