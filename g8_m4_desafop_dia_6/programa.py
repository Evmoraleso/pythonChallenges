from ClsRestaurante import Restaurante
from ClsFarmacia import Farmacia
from ClsSupermercado import Supermercado
from validador import validate


def menuTienda():
    numeros = ['1','2','3']
    print('¿Qué tipo de tienda desea crear?')
    print('1. Restaurante')
    print('2. Supermercado')
    print('3. Farmacia')
    return validate(numeros,input(''))

def menuProductos():
    numeros = ['0','1','2']
    print('¿Qué desea realizar?')
    print('1. Listar productos existentes')
    print('2. Realizar una venta')
    print('0. Salir del programa')
    return validate(numeros,input(''))

continuar=1
#Inicia programa
#Muestra dialogo
resp_tienda=menuTienda()
nombre=input('Ingrese el nombre de la tienda:')
costo=input('Ingrese el costo del delivery para la tienda:')
if resp_tienda == '1':  
    print(f'Usted ha creado una tienda tipo "Restaurante" llamado {nombre}')#Cambiar
    tipo_tienda=Restaurante(nombre,int(costo))
elif resp_tienda == '2': 
    print(f'Usted ha creado una tienda tipo "Supermercado" llamado {nombre}')
    tipo_tienda=Supermercado(nombre,int(costo))
else:
    print(f'Usted ha creado una tienda tipo "Farmacia" llamado {nombre}')
    tipo_tienda=Farmacia(nombre,int(costo))
print('Ingrese los productos y presione 0 para finalizar: ')

while continuar!=0:
    nombre= input('Ingrese nombre:')
    precio= input('Ingrese precio:')
    stock= input('Ingrese stock:')
    tipo_tienda.ingresar_producto(nombre,int(precio),int(stock))
    print('Producto creado!')
    continuar=int(input('Desea continuar agregando productos 1: Si o 0: No '))

respuesta=menuProductos()
while respuesta:
    if respuesta=='0':
        exit()
    elif respuesta=='1':
        for prod in tipo_tienda.listar_producto():
            print(prod)
    elif respuesta=='2':
        nombre= input('Ingrese nombre del producto:')
        cantidad= input('Ingrese la cantidad:')
        if tipo_tienda.realizar_venta(nombre,int(cantidad)):
            print('Venta realizada exitosamente.')
        else:
            print('No se pudo realizar la venta.')
    respuesta=menuProductos()