# -*- coding: utf-8 -*-
"""
Primeros auxilios

@author: elita
    
"""

def valida_si_no(varg):
    if varg=="si" or varg=="no":    
        return True
    else:
        print("Respuesta inválida. Por favor, ingresa 'Si' o 'No'.")
        return False

def pregunta(varg):
    varaux=input(varg+" (Si/No): ").lower()
    while not valida_si_no(varaux):
        varaux=input(varg+" (Si/No): ").lower()
    return varaux

def reevaluar_con_ambulancia():
    print("Reevaluar a la espera de la ambulancia.")
    return pregunta("¿Llegó la ambulancia?")

def administrar_con_ambulancia():
    print("Administrar compresiones torácicas hasta que llegue la ambulancia.")
    return pregunta("¿Llegó la ambulancia?")
    
#Main
while True:

    print("Bienvenido al sistema de primeros auxilios... ")
    
    entrada=pregunta("¿Responde a estímulos?") 
            
    if entrada == "si":
        print("Valorar la necesidad de llegarlo al hospital más cercano.\nFIN ATENCION")
        break
    elif entrada=="no":
        print("Abrir la vía aérea")
        
    entrada=pregunta("¿Respira?")
         
    if entrada == "si":
        print("Permitirle posición de suficiente ventilación.\nFIN ATENCION")
        break
    elif entrada =="no":
        print("Administrar 5 ventilaciones y llamar a ambulancia.")
        
        while True:
            
            entrada=pregunta("¿Signos de vida?") 
    
            if entrada == 'si':
                varamb1=reevaluar_con_ambulancia()
                if varamb1=="si":
                    print("FIN ATENCION")
                    break
                elif varamb1=="no":
                    False
            elif entrada == 'no':
                varamb2=administrar_con_ambulancia()
                if varamb2=='si':
                    print("FIN ATENCION")
                    break
                elif varamb2=='no':
                    False               
        break

    