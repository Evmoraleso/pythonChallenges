# -*- coding: utf-8 -*-
"""
Cálculo velocidad de escape
Created on Mon Apr  1 

@author: Elizabeth Morales
"""
import re, math

def validar_numero_decimal(varg):
    # Patrón de expresión regular para validar números decimales
    patron = r'^[1-9]\d*(\.\d+)$'
    # Comprobar si el número coincide con el patrón
    if re.match(patron, varg):
        return True
    else:
        return False

def validar_numero_entero(varg):
    # Patrón de expón regular para validar números decimales
    patron = r'^[1-9]\d*$'
    # Comprobar si el número coincide con el patrón
    if re.match(patron, varg):
        return True
    else:
        return False
            

# Main
condition= True
varraiz=0.0 #Variable raíz cuadrada

while condition:
    """ 
    vargra--> Variable de constante gravitacional
    vargi--> Variable radio del planeta
    const2-->Constante de valor entero 2
    varilocal--> Variable local que realiza el calculo antes de la obtención de la raiz  
    """
    
    vargra=input("Ingrese la constante g: \n")

    while not validar_numero_decimal(vargra):
        print("El número ingresado no es válido. Por favor, ingrese un número decimal válido.")
        vargra=input("Ingrese la constante g: \n")
        
    varradio=input("Ingrese el radio en Kilómetros: \n")

    while not validar_numero_entero(varradio):
        print("El número ingresado no es válido. Por favor, ingrese un número entero válido.")
        varradio=input("Ingrese el radio en Kilómetros: \n")

    varradio=int(varradio)*1000
    

    #Multiplicacion de constante mas variables g y radio

    const2=2
    varilocal=const2*float(vargra)*int(varradio)

    #Calculo de la velocidad de escape
    
    varraiz=math.sqrt(varilocal)
    condition=False

print("La velocidad de Escape es","{:.1f}".format(varraiz),"[m/s]")