# -*- coding: utf-8 -*-
"""
Cachipún

@author: Elizabeth Morales
"""

import random

def inicia_juego():
    #Captura el dato ingresado por el usuario.
    vartipo=input("Ingrese Piedra, Papel o Tijera para comenzar a jugar: ")

    #Se mantiene en el loop hasta que el usuario ingrese un dato válido.
    while not valida_opcion(vartipo):
        print("Argumento inválido: Debe ingresar Piedra, Papel o Tijera.")
        vartipo=input("Ingrese Piedra, Papel o Tijera para comenzar a jugar: ")

    juega_cachipun(vartipo)

def valida_opcion(opcion):
    #Valida si se ingresó piedra, papel o tijera.  
    #Se convierte el dato a minúscula.
    match opcion.lower():
        case "piedra" |  "papel" |  "tijera":
            return True
        case _:
            return False

def juega_cachipun(vartipo):
    #Juega el "computador" y la persona
    
    #Se define una nueva variable tipo que será minúscula.
    vartipo_=vartipo.lower()
    
    #Se define la lista que será random
    varlist=["piedra","papel","tijera"]

    #Selecciona el dato al azar.
    varrandom=random.choice(varlist) 

    #Según lo ingresado por el usuario y lo que selecciona aleatoriamente el "computador" busca quién gana o pierde
    #o si empatan el juego.
    if varrandom==vartipo_:
        print("Tu jugaste ", vartipo,"\nComputador jugó ", varrandom,"\nEmpataste!!")
    elif vartipo_=="piedra" and varrandom=="papel": #Gana computador
        print("Tu jugaste ", vartipo,"\nComputador jugó ", varrandom,"\nPerdiste :(")
    elif vartipo_=="papel" and varrandom=="piedra": #Gana persona
        print("Tu jugaste ", vartipo,"\nComputador jugó ", varrandom,"\nGanaste!!")
    elif vartipo_=="piedra" and varrandom=="tijera": #Gana persona
        print("Tu jugaste ", vartipo,"\nComputador jugó ", varrandom,"\nGanaste!!")
    elif vartipo_=="tijera" and varrandom=="piedra": #Gana computador
        print("Tu jugaste ", vartipo,"\nComputador jugó ", varrandom,"\nPerdiste :(")
    elif vartipo_=="papel" and varrandom=="tijera": #Gana computador
        print("Tu jugaste ", vartipo,"\nComputador jugó ", varrandom,"\nPerdiste :(")
    elif vartipo_=="tijera" and varrandom=="papel": #Gana persona
        print("Tu jugaste ", vartipo_,"\nComputador jugó ", varrandom,"\nGanaste!!")

def jugar_o_salir():
    #El usuario selecciona si quiera iniciar el juego, continuar jugando o salir del juego
    while True:
        opcion = input("Presione '1' para jugar Cachipún o '0' para salir: ").lower()
        if opcion == "1":
            inicia_juego()
        elif opcion == "0":
            print("Saliendo del juego...")
            break
        else:
            print("Opción no válida. Por favor, ingrese '1' para continuar o '0' para salir.")

#Main
jugar_o_salir()

