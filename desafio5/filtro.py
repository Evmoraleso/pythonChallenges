# -*- coding: utf-8 -*-
"""
Name: Filtro
@autor: Liz 
"""
import sys

def umbral(varg,varg1):
    #Filtrar elementos cuyo valor sea mayor o menor que el argumento varg
    if varg1 == "" or varg1=="mayor": 
        resultado = {clave for clave, valor in precios.items() if valor > int(varg)}
        print(f"Los productos mayores al umbral son: {', '.join(resultado)}")
    elif varg1=="menor":
        resultado = {clave for clave, valor in precios.items() if valor < int(varg)}
        print(f"Los productos menores al umbral son: {', '.join(resultado)}")
    else: print("Lo sentimos, no es una operación válida, try it again...")

def main():    
    # Verificar que se ingresen los argumentos correctamente
    if len(sys.argv) < 2:
        print("Debe ingresar el valor a filtrar y/o seguido de 'menor'/'mayor' (si no lo indica, por defecto el umbral es mayor al valor ingresado....)")        
        sys.exit(1)
    else:
        # Captura el error en caso de que el argumento 1 no sea numérico
        if not sys.argv[1].isnumeric():
            print("El valor a filtrar o umbral, debe ser numérico.")
            sys.exit(1)        
        # Captura el error en caso de que el argumento 2 venga sin dato, por lo que toma por defecto 'mayor'
        try:       
            maymen = sys.argv[2]
        except IndexError:
            maymen = "mayor"
        # Llama a la función umbral con los argumentos umbral y maymen
        umbral(sys.argv[1], maymen)

#Main
if __name__ == "__main__":
    #Diccionario de precios
    precios = {'Notebook': 700000,
    'Teclado': 25000,
    'Mouse': 12000,
    'Monitor': 250000,
    'Escritorio': 135000,
    'Tarjeta de Video': 1500000}
    main()
    


