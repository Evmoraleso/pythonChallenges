from ClsEncuesta import EncuestaEdad, EncuestaRegion
from ClsPregunta import Pregunta
from ClsAlternativa import Alternativa
from ClsListaRespuesta import ListaRespuesta
from ClsUsuario import Usuario

#Creamos dos encuestas una tipo edad y otra de tipo region
#Segun los datos del usuario se utilizara una o la otra
encuestaEdad=EncuestaEdad('Encuesta por edad',21,50)
encuestaRegion=EncuestaRegion('Encuesta por region')
#Creamos las preguntas
pregunta1=Pregunta('¿Cuál es la capital de Francia?','Queda en Europa',True)
pregunta2=Pregunta('¿Quién pintó La última cena?','Pinto Italiano',False)
pregunta3=Pregunta('¿Cuál es el planeta más grande del sistema solar?','',True)
pregunta4=Pregunta('¿En qué año comenzó la Primera Guerra Mundial?','',False)
#Creamos las alternativas a las preguntas 
alternativa1=Alternativa('Roma','')
alternativa2=Alternativa('Berlín','Ayuda')
alternativa3=Alternativa('París','')
alternativa4=Alternativa('Madrid','Ayuda')

alternativa5=Alternativa('Pablo Picasso','')
alternativa6=Alternativa('Leonardo da Vinci','Ayuda')
alternativa7=Alternativa('Vincent van Gogh','')
alternativa8=Alternativa('Miguel Ángel','Ayuda')

alternativa9=Alternativa('Marte','')
alternativa10=Alternativa('Venus','Ayuda')
alternativa11=Alternativa('Júpiter','')
alternativa12=Alternativa('Saturno','Ayuda')

alternativa13=Alternativa('1914','')
alternativa14=Alternativa('1939','Ayuda')
alternativa15=Alternativa('1945','')
alternativa16=Alternativa('1918','Ayuda')
#Asociamos la lista de alternativas a cada pregunta
pregunta1.set_listAlternativas(alternativa1)     
pregunta1.set_listAlternativas(alternativa2)     
pregunta1.set_listAlternativas(alternativa3)     
pregunta1.set_listAlternativas(alternativa4)    
pregunta2.set_listAlternativas(alternativa5)     
pregunta2.set_listAlternativas(alternativa6)     
pregunta2.set_listAlternativas(alternativa7)     
pregunta2.set_listAlternativas(alternativa8)   
pregunta3.set_listAlternativas(alternativa9)     
pregunta3.set_listAlternativas(alternativa10)     
pregunta3.set_listAlternativas(alternativa11)     
pregunta3.set_listAlternativas(alternativa12)   
pregunta4.set_listAlternativas(alternativa13)     
pregunta4.set_listAlternativas(alternativa14)     
pregunta4.set_listAlternativas(alternativa15)     
pregunta4.set_listAlternativas(alternativa16)   
#Creamos un nuevo usuario'
user=Usuario(54,'emorales@gmail.com',2)
#Creamos un listado de respuestas
listaRespuestas=ListaRespuesta('emorales@gmail.com',None)
#Asignamos la encuesta y la lista de respuestas al usuario'
#Validamos que encuesta aplicar al usuario
if user._edad >= encuestaEdad.get_edadMinima() and user._edad <= encuestaEdad.get_edadMaxima():
    respuestaE=True
else:   respuestaE=False    

if user._region in encuestaRegion.get_listaRegiones():
    respuestaR=True
else:   respuestaR=False    

if respuestaE:
    encuesta=encuestaEdad
    encuesta._listaPreguntas=pregunta1
    encuesta._listaPreguntas=pregunta2
    encuesta._listaPreguntas=pregunta3
    encuesta._listaPreguntas=pregunta4
    encuesta._listaRespuesta=listaRespuestas
elif respuestaR:
    encuesta=encuestaRegion
    encuesta._listaPreguntas=pregunta1
    encuesta._listaPreguntas=pregunta2
    encuesta._listaPreguntas=pregunta3
    encuesta._listaPreguntas=pregunta4
    encuesta._listaRespuesta=listaRespuestas
elif respuestaE and respuestaR:
    encuesta=encuestaEdad
    encuesta._listaPreguntas=pregunta1
    encuesta._listaPreguntas=pregunta2
    encuesta._listaPreguntas=pregunta3
    encuesta._listaPreguntas=pregunta4
    encuesta._listaRespuesta=listaRespuestas
#Mostramos la encuesta
encues=encuesta.mostrarEncuesta()
print('Encuesta: ',encues._nombre.upper())
i=1
j=1
respuesta=0
lista_respuesta=[]
for en in encues._listaPreguntas:
    if isinstance(en,Pregunta):
        print('Pregunta ',i)
        print(f'Enunciado: {en._enunciado}, Ayuda: {en._ayuda}')
        j=0
        for alt in en.get_listAlternativas():
            if isinstance(alt,Alternativa):
                print(f'{j}: {alt._contenido}, Ayuda: {alt._ayuda}')
            j+=1
        respuesta=input('Ingrese la respuesta: ')
        lista_respuesta.insert(i,respuesta)
        i+=1
respuestas=ListaRespuesta(user._email,lista_respuesta)
encues._listaRespuesta=respuestas
print(f'Las respuestas del usuario, {user._email} son las siguientes')
resp=encues._listaRespuesta
for indice,r in enumerate(resp._respuesta):
    print('Pregunta: ',indice+1,'  Respuesta: ',r)