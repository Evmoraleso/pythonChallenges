# -*- coding: utf-8 -*-
"""
Fuerza bruta
@author: elita
"""

from string import ascii_lowercase
import re

def solo_letras(varg):
    # Patrón para solo letras, excluyendo la 'ñ'
    patron = r'^[a-zA-Z]'
    return bool(re.match(patron, varg))


def contar_intentos(varpass):
    """
    Cuenta la cantidad de intentos para forzar la contraseña.
    """
    count = 0
    for varp in varpass.lower():
        for varl in ascii_lowercase:
            count += 1
            if varp == varl:
                break
    return count

# Main
   
# Se mantiene en el loop hasta que el usuario ingrese un dato válido.
while not solo_letras(varpass := input("Ingrese la contraseña, solo letras (excepto la ñ): ")):
    print("Incorrecto, ingrese solo letras, excepto la ñ.")

#Se llama a la función para obtener la cantidad de intentor totales.
count = contar_intentos(varpass)           
print(f'"La contraseña fue forzada en {count} intentos"')            