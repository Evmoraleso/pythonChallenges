from get_api import get_api
from create_html import get_template
from launch_html import deploy_html
from validador import validate
import os
import sys
import time

#Valores iniciales
continuar = True
op_sys = 'cls' if sys.platform == 'win32' else 'clear'

# limpiar pantalla
os.system(op_sys) 

print('Bienvenido!')
opcion = input('''Desea crear el sitio web 'Aves de Chile'? Elija una opción:
        1. Sí 
        0. No
        
    > ''')
# 1. validar opcion
opcion = validate(['0','1'],opcion)

# 2. Definir el comportamiento de Salir
if opcion == '0':
    print("Nos vemos pronto!")
    time.sleep(2)
    os.system(op_sys)
    exit()#Finalizar el programa    

while continuar:
#Llamado a la API

    url= 'http://localhost:5000/birds' #'https://aves.ninjas.cl/api/birds'
    api_content=get_api(url)
    #Llama a la funcion get_template para crear el html
    html=get_template(api_content)
    time.sleep(3)    
    #Exportar el sitio creado como un archivo html llamado 'index.html' para que pueda ser abierto en el navegador
    deploy_html(html)
    time.sleep(3)
    print("Proceso finalizado, puede abrir el archivo llamado 'index.html'")
    #Espera 3 segundos y finaliza el programa   
    time.sleep(3)
    exit() 
#Fin 

