# -*- coding: utf-8 -*-
"""
Conversiones

@author: elita
"""
import sys

def convertir_pesos_chilenos(tasas, valor_en_pesos):
    resultado = {}
    for moneda, tasa in tasas.items():
        resultado[valor_en_pesos * tasa] = moneda 
    return resultado
 
#Main
# Verificar que se ingresen los argumentos correctamente
if len(sys.argv) != 5:
    print("Error: Debes ingresar 4 argumentos en total.")
    sys.exit(1)

#Creamos un diccionario llamado tasas
tasas = {"Soles":float(sys.argv[1]),"Pesos Argentinos":float(sys.argv[2]),"Dólares Americanos":float(sys.argv[3])}

# Obtener el valor en pesos chilenos a convertir
valor_en_pesos = int(sys.argv[4])

# Convertir el valor en pesos chilenos a las distintas monedas
resultados = convertir_pesos_chilenos(tasas, valor_en_pesos)

# Imprimir los resultados
print(f"Los {valor_en_pesos} pesos equivalen a:")
for moneda, resultado in resultados.items():
    print(f"{moneda} {resultado}")

