import os
import sys
from validador import validate
from clste import te

#Valores iniciales
continuar = True
op_sys = 'cls' if sys.platform == 'win32' else 'clear'

# limpiar pantalla
os.system(op_sys) 

print('Bienvenido a Tecitos que dan risa!')
tipo_te = input('''Seleccine el tipo de te que desea adquirir:
        1. Te Negro 
        2. Te Verde
        3. Agua de hierbas
        0. Salir
        
    > ''')
# 1. validar opcion
tipo_te = validate(['0','1','2','3'],tipo_te)

# 2. Definir el comportamiento de Salir
if tipo_te == '0':
    print("Nos vemos pronto!")
    os.system(op_sys)
    exit()#Finalizar el programa    

gramos = input('''Seleccione el formato en gramos:
        1. 300 gramos
        2. 500 gramos
        
    > ''')
# 1. validar opcion
gramos = validate(['1','2'],gramos)

te_objeto=te.objte_gr(tipo_te,gramos)
te_precio= te.precio(gramos)

print(f'Usted selecciono {te_objeto.sabor}, en formato de {int(te_objeto.formato)} gramos con un precio de ${int(te_precio)}, el cual tiene un tiempo de preparacion de {int(te_objeto.tiempop)} minutos y {te_objeto.recomendacion}')