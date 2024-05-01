
from clspersonaje import personaje
import dialogo

#Inicializa constantes
const_orco='Orco'
const_gana=50
const_pierde=-30

#Inicia programa
#Muestra dialogo
nombre=dialogo.diag_bienvenida()
#Instancias de la clase personaje
jugador=personaje(nombre.capitalize())
orco=personaje(const_orco)
#Obtiene el estado inicial del jugador
dialogo.estado(jugador.get_var_nombre,jugador.get_var_nivel,jugador.get_var_experiencia)
#Muestra dialogo
dialogo.diag_orco()
#Obtiene probabilidad
probabilidad=jugador.get_calcula_probabilidad(orco)
#Muestra dialogo
dialogo.diag_prob(probabilidad)
##Muestra dialogo menu y obtiene input
respuesta=dialogo.menu()

#Entra al ciclo si el jugador quiere atacar
while respuesta=='1':
    #Retorna si el jugador gana o pierde
    if personaje.get_random(probabilidad):
        #Muestra dialogo si gana
        dialogo.diag_gana()
        #Setea la experiencia y el nivel del jugador y el Orco
        jugador.set_update_experiencia_nivel(const_gana)
        orco.set_update_experiencia_nivel(const_pierde)       
    else:
        #Muestra dialogo si jugador pierde
        dialogo.diag_pierde()
        #Setea la experiencia y el nivel del jugador y el Orco
        jugador.set_update_experiencia_nivel(const_pierde)
        orco.set_update_experiencia_nivel(const_gana)
    #Obtiene el nuevo estado del jugador
    dialogo.estado(jugador.get_var_nombre,jugador.get_var_nivel,jugador.get_var_experiencia)
    #Obtiene el nuevo estado del orco
    dialogo.estado(orco.get_var_nombre,orco.get_var_nivel,orco.get_var_experiencia)
    #Obtiene probabilidad
    probabilidad=jugador.get_calcula_probabilidad(orco)
    #Muestra dialogo       
    dialogo.diag_prob(probabilidad)
    ##Muestra dialogo menu y obtiene input
    respuesta=dialogo.menu()

#Muestra dialogo final    
dialogo.diag_final()
