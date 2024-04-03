# -*- coding: utf-8 -*-
"""
Rentabilidad 1, 2 y 3
Created on Mon Apr  1

@author: Elizabeth Morales
"""
import re, os

def validar_numero(varg):
    # Patrón de expresión regular para validar números enteros
    patron = r'^[1-9]\d*?$'
    # Comprobar si el número coincide con el patrón
    if re.match(patron, varg):
        return True
    else:
        return False

def limpiar_pantalla():
    # Verificar el sistema operativo y ejecutar el comando adecuado
    if os.name == 'nt':  # Windows
        os.system('cls')
    else:  # Linux, macOS, etc.
        os.system('clear')

def opcion1():
    """ 
    Emprendedor 1
    varps--> Precio subscripcion
    varnu--> Numero de usuarios
    vargt--> Gastos totales
    varutilidades-->Utilidades
    """
    varutilidades=0.0

    while True:
    
        varps=input("Ingrese el Precio de Subscripción: \n")
    
        while not validar_numero(varps):
            print("El número ingresado no es válido. Por favor, ingrese un número. \n")
            varps=input("Ingrese el Precio de Subscripción: \n")
            
        varnu=input("Ingrese el Número de Usuarios: \n")
    
        while not validar_numero(varnu):
            print("El número ingresado no es válido. Por favor, ingrese un número. \n")
            varnu=input("Ingrese el Número de Usuarios: \n")
    
        vargt=input("Ingrese los Gastos Totales: \n")
    
        while not validar_numero(vargt):
            print("El número ingresado no es válido. Por favor, ingrese un número. \n")
            vargt=input("Ingrese los Gastos Totales: \n")
            
        varutilidades=(int(varps)*int(varnu))-int(vargt)
        
        break

    print("Las Utilidades del Proyecto son: ", varutilidades)  
    mostrar_menu()     
    
def opcion2():
    """ 
    Emprendedor 2
    varps--> Precio subscripcion
    varnunor--> Numero de usuarios normales
    varnupre--> Numero de usuarios premium
    vargt--> Gastos totales
    varutilidades-->Utilidades
    """
    constpor=1.5
    varutilidades=0.0

    while True:
    
        varps=input("Ingrese el Precio de Subscripción: ")
    
        while not validar_numero(varps):
            print("El número ingresado no es válido. Por favor, ingrese un número.")
            varps=input("Ingrese el Precio de Subscripción: ")
            
        varnunor=input("Ingrese el Número de Usuarios Normales: ")
    
        while not validar_numero(varnunor):
            print("El número ingresado no es válido. Por favor, ingrese un número.")
            varnunor=input("Ingrese el Número de Usuarios Normales: ")

        varnupre=input("Ingrese el Número de Usuarios Premium: ")
    
        while not validar_numero(varnupre):
            print("El número ingresado no es válido. Por favor, ingrese un número.")
            varnupre=input("Ingrese el Número de Usuarios Premium: ")
           
        vargt=input("Ingrese los Gastos Totales: ")
    
        while not validar_numero(vargt):
            print("El número ingresado no es válido. Por favor, ingrese un número.")
            vargt=input("Ingrese los Gastos Totales: ")
        
        totalun=int(varps)*int(varnunor)
        totalpre=(int(varps)*constpor)*int(varnupre)
        varutilidades=(totalun+totalpre)-int(vargt)
         
        break
        
    print("Las Utilidades del Proyecto son: ", varutilidades)    
    mostrar_menu()      

def opcion3():
    """ 
    Emprendedor 3
    varps--> Precio subscripcion
    varnu--> Numero de usuarios normales
    vargt--> Gastos totales
    varutaant--> Utilidades del año anterior
    varutilidades-->Utilidades
    """
    varutilidades=0.0

    while True:
    
        varps=input("Ingrese el Precio de Subscripción: ")
    
        while not validar_numero(varps):
            print("El número ingresado no es válido. Por favor, ingrese un número.")
            varps=input("Ingrese el Precio de Subscripción: ")
            
        varnu=input("Ingrese el Número de Usuarios: ")
    
        while not validar_numero(varnu):
            print("El número ingresado no es válido. Por favor, ingrese un número.")
            varnu=input("Ingrese el Número de Usuarios: ")
           
        vargt=input("Ingrese los Gastos Totales: ")
    
        while not validar_numero(vargt):
            print("El número ingresado no es válido. Por favor, ingrese un número.")
            vargt=input("Ingrese los Gastos Totales: ")
        
        varutaant=input("Ingrese las Utilidades del año anterior: ")
    
        while not validar_numero(varutaant):
            print("El número ingresado no es válido. Por favor, ingrese un número.")
            varutaant=input("Ingrese las Utilidades del año anterior: ")
        
        currentut=(int(varps)*int(varnu))-int(vargt)
        varutilidades=currentut/int(varutaant)
         
        break
        
    print("La razón entre las utilidades actuales y las del año anterior es: {:.2f}".format(varutilidades))  
    mostrar_menu()      

def mostrar_menu():

    print("Bienvenido al menú:")
    print("1. Opción 1")
    print("2. Opción 2")
    print("3. Opción 3")
    print("0. Salir")

    opcion = input("Selecciona una opción: ")

    if opcion == "1":
        opcion1()
    elif opcion == "2":
        opcion2()
    elif opcion == "3":
        opcion3()
    elif opcion == "0":
        print("Saliendo del programa...")
    else:
        print("Opción no válida. Por favor, selecciona una opción del menú.")

# Loop principal del programa
opcion="0"
while True:
    mostrar_menu()
    if opcion == "0":
        break
