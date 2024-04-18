
def validate(opciones, eleccion):
    # Definir validación de eleccion
    while eleccion not in opciones:
        print("Opción no válida, ingrese una de las opciones válidas:.")
        eleccion = input("").lower()    
    return eleccion 

if __name__ == '__main__':
    #Important: Use only for testing
    #Check the results
    eleccion = input('Ingresa una Opción: ').lower()
    # letras = ['a','b','c','d'] # pueden probar con letras también para verificar su funcionamiento.
    numeros = ['y','n']
    # Si se ingresan valores no validos a eleccion debe seguir preguntando
    validate(numeros,eleccion)
    pass