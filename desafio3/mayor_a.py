# -*- coding: utf-8 -*-
"""
Filtrado compacto
Spyder Editor

This is a temporary script file.
"""

import re,sys

def validar_numero(varg):
    # Patrón de expresión regular para validar números enteros
    patron = r'^[1-9]\d*?$'
    # Comprobar si el número coincide con el patrón
    if re.match(patron, varg):
        return True
    else:
        return False

def mayor_a(varg):
    #Filtra el diccionario con el valor umbral entregado

    # Filtrar elementos cuyo valor sea mayor que el argumento varg
    resultado = {clave: valor for clave, valor in ventas.items() if valor > int(varg)}
    print(resultado)  # Salida: {}


#Main
#Diccionario Ventas
ventas = {
 "Enero": 15000,
 "Febrero": 22000,
 "Marzo": 12000,
 "Abril": 17000,
 "Mayo": 81000,
 "Junio": 13000,
 "Julio": 21000,
 "Agosto": 41200,
 "Septiembre": 25000,
 "Octubre": 21500,
 "Noviembre": 91000,
 "Diciembre": 21000,
}


#varumbral=input("Ingrese el valor a filtrar: ")
# Verificar que se ingresen los argumentos correctamente
if len(sys.argv) != 2:
    print("Error: Debes ingresar 1 argumento como filtro.")
    sys.exit(1)

mayor_a(sys.argv[1])
    
