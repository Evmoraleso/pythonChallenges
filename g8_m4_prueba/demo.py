from ClsCampaña import Campaña
import os
from datetime import datetime

def log_error(error_: str):
    with open("error.log", "a+") as log:
        log.seek(0)
        now = datetime.now()
        log.write(f"[{now.strftime('%Y-%m-%d %H:%M:%S')}] ERROR: {error_}\n")
        log.seek(0)
        log.close()

def crea_log():        
    if not os.path.isfile("error.log"):
        with open("error.log", "w") as log:
            now=datetime.now()
            log.write(f"[{now.strftime('%Y-%m-%d %H:%M:%S')}] Se crea el archivo error.log\n")
            log.close()

TEXTO250= "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Sed non risus. Suspendisse lectus tortor, dignissim sit amet, adipiscing nec, ultricies sed, dolor. Cras elementum ultrices diam. Maecenas ligula massa, varius a, semper congue, euismod non, mi. Proin porttitor, orci nec nonummy molestie, enim est eleifend mi, non fermentum diam nisl sit amet erat. Duis semper. Duis arcu massa, scelerisque vitae, consequat in, pretium a, enim. Pellentesque congue. Ut in risus volutpat libero pharetra tempor. Cras vestibulum bibendum augue. Praesent egestas leo in pede. Praesent blandit odio eu enim. Pellentesque sed dui ut augue blandit sodales. Vestibulum ante ipsum primis in faucibus orci luctus et ultrices posuere cubilia Curae; Aliquam nibh. Mauris ac mauris sed pede pellentesque fermentum."
varCamp = Campaña("Nombre Inicial",datetime(2024, 1, 1),datetime(2024, 6, 1))

try:
    crea_log()
    #Descomentar linea siguiente: Prueba ingresando un nombre de Campaña mayor a 250
    #varCamp._nombre=TEXTO250
    #Se solicita ingresar por consola
    nuevoNombre = input("Ingrese un nuevo nombre para la Campaña: \n")
    varCamp._nombre=nuevoNombre

    for anuncio in varCamp._lista_Anuncios:        
        if anuncio["Tipo"] == "Video":
            objeto_video = anuncio["Objeto"]
            #Mostrar los formatos disponibles
            objeto_video.mostrar_formatos()
            #Descomentar linea siguiente: Prueba ingresando un formato no valido para gatillar el error
            #objeto_video._sub_tipo= 'no existe'
            #Se solicita ingresar por consola
            nuevoSubtipo = input("Ingrese un nuevo SubTipo para el anuncio: ")
            objeto_video._sub_tipo= nuevoSubtipo
    #Muestra la sobrecarga del metodo str en la clase Campaña
    print(varCamp)
except Exception as error:
    log_error(error)
    exit()  