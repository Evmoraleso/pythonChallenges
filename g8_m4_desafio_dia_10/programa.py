from Clsfoto import Foto

objFoto = Foto(50,50,'c:\misfotos')

print('Vamos a modificar el alto y ancho de una foto ya registrada!\nQué dimensión quieres modificar?\n1.- Alto\n2.- Ancho\n3.- Ambos\n0.- Salir')
alto=None
ancho=None
respuesta = input('')
while respuesta not in ('0','1','2','3'):
    respuesta = input('Ingreso una opcion valida\n')
try:
    if respuesta == '0':
        print('Adios!')
        exit()
    if respuesta == '1':
        alto = int(input("Ingrese el nuevo 'alto' de la foto: "))
    elif respuesta == '2':
        ancho = int(input("Ingrese el nuevo ancho de la foto: "))
    else:
        alto = int(input("Ingrese el nuevo 'alto' de la foto: "))
        ancho = int(input("Ingrese el nuevo ancho de la foto: "))
except ValueError as error:
    print("Debe ingresar un número para ancho y alto. No se hicieron cambios.")

try:
    if alto is not None:
        objFoto.alto=alto
        print(f'Nuevo valor dimensión "Alto": {objFoto.alto}')
    if ancho is not None:
        objFoto.ancho=ancho
        print(f'Nuevo valor dimensión "Ancho": {objFoto.ancho} ')
    print(f'Las dimensiones de la foto son:\nAlto: {objFoto.alto}\nAncho: {objFoto.ancho}')
except Exception as error:
    print(f'Las dimensiones de la foto son:\nAlto: {objFoto.alto}\nAncho: {objFoto.ancho}')
    print(error)