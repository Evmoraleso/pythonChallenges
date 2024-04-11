# -*- coding: utf-8 -*-
"""
Name: Factorial y productoría
@autor: Liz 
"""
import math
#Retorna el factorial de un número
def factorial(argv):
    return math.factorial(argv)
#Retorna la productoría de una lista de números
def productoria(argv):
    prod = 1
    for num in argv:
        prod *= num
    return prod
#Calcula el factorial y la productoría 
def calcular(**kwargs):
    lista=[]
    for key, valor in kwargs.items():
        if "fact_" in key:
            lista.append((f"El factorial de {valor} es",factorial(valor)))
        elif "prod_" in key:
            lista.append((f"La productoria de {valor} es",productoria(valor)))
    return lista

def main():
    #Imprime los resultados 
    [print(desc,val) for desc, val in calcular(fact_1 = 5, prod_1 = [4,6,7,4,3], fact_2 = 6)]

if __name__=="__main__":
    main()