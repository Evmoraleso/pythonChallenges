# -*- coding: utf-8 -*-
"""
Cálculo IMC

@author: Elizabeth Morales
"""
import re

def inicio():
    #Obtiene variable peso
    varpeso=pregunta_valida("Ingrese el peso en Kg: ")
    
    #Obtiene variable altura    
    varaltura=pregunta_valida("Ingrese la altura en centímetros: ")

    #Cálcula IMC
    varimc=calcula_imc(varpeso, varaltura)

    #Obtiene la clasificacion OMS
    varclasificacion=obtiene_clasificacion_oms(varimc)

    #Imprime los resultados
    print("Su IMC es","{:.2f}".format(varimc))
    print(varclasificacion)
 
def pregunta_valida(varg):
    varaux=input(varg)
    while not validar_numero_decimal(varaux):
        varaux=input(varg)
    return varaux
    
def validar_numero_decimal(varg):
    # Patrón de expresión regular para validar números enteros y decimales
    patron = r'^[1-9]\d*(\.\d+)?$'
    # Comprobar si el número coincide con el patrón
    if re.match(patron, varg):
        return True
    else:
        return False

def calcula_imc(vargp,varga):
    #Constante para transformar de cm a mts
    constmt=100
    #Se transforma el valor de la altura de cm a mts.
    varalturamt=float(varga)/constmt
    
    #Se calcula el IMC
    return float(vargp)/pow(varalturamt,2)

def obtiene_clasificacion_oms(varimc):
    #Obtiene la clasificacion OMS según el IMC calculado.
    
    if varimc < 18.5:
        return "La clasificación OMS es Bajo Peso."
    elif varimc >= 18.5 and varimc < 25:
        return "La clasificación OMS es Adecuado."
    elif varimc >= 25 and varimc < 30:
        return "La clasificación OMS es Sobrepeso."
    elif varimc >= 30 and varimc < 35:
        return "La clasificación OMS es Obesidad Grado I."
    elif varimc >= 35 and varimc < 40:
        return "La clasificación OMS es Obesidad Grado II."
    else: #si varimc es mayor o mayor igual de 40
        return "La clasificación OMS es Obesidad Grado III."
    
def calcular_o_salir():
    #El usuario selecciona si quiera iniciar el juego, continuar jugando o salir del juego
    while True:
        opcion = input("Presione '1' para calcular el IMC o '0' para salir: ").lower()
        if opcion == "1":
            inicio()
        elif opcion == "0":
            print("Saliendo del calcular IMC...")
            break
        else:
            print("Opción no válida. Por favor, ingrese '1' para continuar o '0' para salir.")

#Main
calcular_o_salir()