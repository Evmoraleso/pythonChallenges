# -*- coding: utf-8 -*-
"""
Name: Velocidad
@autor: Liz 
"""
#Retorna el promedio de la lista de velocidades de las correas transportadoras
def media():
    return sum(velocidad)/len(velocidad)
#Retorna la lista ordenada de las posiciones de las correas cuya velocidad esta por sobre el promedio
def listar_posiciones():
    prom=media()
    lista=[pos for pos, vel in enumerate(velocidad) if vel > prom]
    lista.sort()
    return print(lista) 
#Main
def main():    
    listar_posiciones()
   
if __name__=="__main__":
    #Lista de velocidades
    velocidad = [25, 12, 19, 16, 11, 11, 24, 1,
    14, 14, 16, 10, 6, 23, 13, 25, 4, 19,
    14, 20, 18, 9, 18, 4, 18, 1, 3, 4, 2,
    14, 23, 19, 23, 9, 18, 20, 22, 14, 1,
    10, 5, 23, 3, 5, 9, 5, 3, 12, 20, 5,
    11, 10, 18, 10, 14, 5, 23, 20, 23, 21]
    #Llama a la funcion main
    main()