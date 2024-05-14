import json
import os
from datetime import datetime
from usuario import Usuario

#Almacena instancias Usuario
instancias = []

#Abre el archivo log y agrega nuevas lineas con errores 
def log_error(error_: str, mensaje: str):
    with open("logs/error.log", "a+") as log:
        log.seek(0)
        print(log.read())
        now = datetime.now()
        log.write(f"[{now.strftime('%Y-%m-%d %H:%M:%S')}] ERROR: {error_} {mensaje}\n")
        log.seek(0)
        print(log.read())
        log.close()

#Valida si existe el archivo log en la carpeta logs 
#Si no existe lo crea
def crea_log():        
    if not os.path.isfile("logs/error.log"):
        with open("logs/error.log", "w") as log:
            now=datetime.now()
            log.write(f"[{now.strftime('%Y-%m-%d %H:%M:%S')}] Se crea el archivo error.log\n")
            log.close()

try:
    crea_log()
    with open("usuarios.txt") as arch:
        linea = arch.readline()

        while linea:
            user = json.loads(linea)
            instancias.append(Usuario(user.get("nombre"), user.get("apellido"), user.get("email"), user.get("genero")))
            linea = arch.readline()    
except FileNotFoundError as error:#Error archivo no encontrado
    log_error(error,'Archivo no encontrado.')
    exit()
except json.decoder.JSONDecodeError as error:#Error en Json
    log_error(error, 'Problemas en la conformacion del archivo Json, comillas no cerradas o llaves no cerradas.')
    exit()
except Exception as error:#Cualquier otro error
    log_error(error,None)
    exit()        

#Muestra los usuarios creados.
for instancia in instancias:
    print(f'Nombre: {instancia.nombre} Apellido: {instancia.apellido} Email: {instancia.email}, Genero: {instancia.genero}') 