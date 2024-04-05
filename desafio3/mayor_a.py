# -*- coding: utf-8 -*-
"""
Filtrado compacto
Spyder Editor

This is a temporary script file.
"""

import re

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


varumbral=input("Ingrese el valor a filtrar: ")

while not validar_numero(varumbral):
    print("El número ingresado no es válido. Por favor, ingrese un número.")
    varumbral=input("Ingrese el valor a filtrar: ")

mayor_a(varumbral)
    
