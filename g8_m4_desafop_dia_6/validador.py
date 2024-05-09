
def validate(opciones, eleccion):
    # Definir validación de eleccion
    while eleccion not in opciones:
        print("Opción no válida, ingrese una de las opciones válidas:")
        eleccion = input("")  
    return eleccion 

def validate_str(eleccion):
    # Definir validación de eleccion
    while not eleccion:
        print("El nombre del jugador debe contener al menos un caracter...")
        eleccion = input("").strip().lower()    
    return eleccion 

if __name__ == '__main__':
    #Important: Use only for testing
    #Check the results
    eleccion = input('¿Qué deseas hacer?: ').lower()
    # letras = ['a','b','c','d'] # pueden probar con letras también para verificar su funcionamiento.
    numeros = ['1','2']
    # Si se ingresan valores no validos a eleccion debe seguir preguntando
    validate(numeros,eleccion)
    pass