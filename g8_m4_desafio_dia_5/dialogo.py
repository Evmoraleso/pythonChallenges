from validador import validate, validate_str

def menu():
    numeros = ['1','2']
    print('¿Qué deseas hacer?')
    print('1. Atacar')
    print('2. Huir')
    return validate(numeros,input(''))

def diag_bienvenida():
    print('¡Bienvenido a Gran Fantasía!\nPor favor indique nombre de su personaje:')
    return validate_str(input('').strip())

def estado(nombre: str, nivel: int, experiencia: int):
    print(f'NOMBRE: {nombre}          NIVEL: {nivel}           EXPERIENCIA: {experiencia}\n')

def diag_orco():
    print('¡Oh no!, ¡Ha aparecido un Orco!\n')

def diag_prob(probabilidad: int):
    print(f'Con tu nivel actual, tienes {probabilidad}% de probabilidades de ganarle al Orco.\nSi ganas, ganarás 50 puntos de experiencia y el orco perderá 30.\nSi pierdes, perderás 30 puntos de experiencia y el orco ganará 50\n')

def diag_gana():
    print('¡Le has ganado al orco, felicidades!\n¡Recibirás 50 puntos de experiencia!\n')

def diag_pierde():
    print('¡Oh no! ¡El orco te ha ganado!\n¡Has perdido 30 puntos de experiencia!\n')

def diag_final():
    print('¡Has huido! El orco ha quedado atrás.')