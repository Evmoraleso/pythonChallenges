# -*- coding: utf-8 -*-
"""
Contador de caracteres y palabras distintas del texto dentro de un archivo txt

"""
import sys

def open_arch(archivo):
    #Abre el archivo y lee el archivo ipsum.txt
    with open(archivo, "r") as file:
        return file.read()

def count_chr(archtxt):
    #Cuenta los caracteres distintos del archivo ipsum.txt
    return print("El número de caracteres distintos es: ",len(set(archtxt)))

def count_word(archtxt):
    #Cuenta las palabras distintas del archivo ipsum.txt
    return print("El número de palabras distintas es: ",len(set(archtxt.split(" "))))

def main():
    # Verificar que se ingresen los argumentos correctamente
    if len(sys.argv) < 2:
        print("Debe ingresar el nombre del archivo '.txt' como argumento.")
        sys.exit(1)
    else:
        #Captura el error en caso de ingresar el nombre de un archivo que no se encuentre en la carpeta del proyecto
        try:
            vararch=open_arch(sys.argv[1])
        except FileNotFoundError:
            print("El nombre de archivo ingresado, no existe, trying it again...") 
        else:    
            #Llama a la funcion count_chr para contar los caracteres distintos del archivo de texto
            count_chr(vararch)
            #Llama a la funcion count_word para contar las palabras distintos del archivo de texto
            count_word(vararch)
#Main
if __name__ == "__main__":
    # Ejecutar el script por primera vez
    main()