from datetime import date
from ClsError import LargoExcedido
from ClsAnuncio import Video, Display, Social

class Campaña:
    def __init__(self,nombre: str, fecha_inicio: date, fecha_termino: date) -> None:
        self.__nombre = nombre
        self.__fecha_inicio = fecha_inicio
        self.__fecha_termino = fecha_termino
        self.__listaAnuncios = []                               
        self._instancia_privada()

    @property
    def _nombre(self):
        return self.__nombre

    @_nombre.setter
    def _nombre(self, value):
        if len(value) > 250:
            raise LargoExcedido('El nombre excede el largo permitido (250)')
        else:
            self.__nombre = value

    @property
    def _fecha_inicio(self):
        return self.__fecha_inicio

    @_fecha_inicio.setter
    def _fecha_inicio(self, value):
        self.__fecha_inicio = value

    @property
    def _fecha_termino(self):
        return self.__fecha_termino

    @_fecha_termino.setter
    def _fecha_termino(self, value):
        self.__fecha_termino = value

    @property
    def _lista_Anuncios(self):
        return self.__listaAnuncios
    
    def _instancia_privada(self):
        video = Video(1, 1, 'url1', 'url2', 'instream', 1)
        display = Display(1,1,'url1','url2','tradicional')
        display2 = Display(1,1,'url1','url2','native')
        self.__listaAnuncios = [{"Tipo":"Video","Objeto":video},{"Tipo":"Display","Objeto":display}, {"Tipo":"Display","Objeto":display2}]

    def __str__(self): 
        #Se conoce que los metodos no deben generar, imprimir o mostrar texto
        #Se realiza de esta forma por el requerimiento del ejercicio
        str = f'Nombre de la campana: {self._nombre}\n'
        countv=0
        countd=0
        counts=0
        for anuncio in self._lista_Anuncios:
            if anuncio["Tipo"] == "Video":
                countv +=1
            elif anuncio["Tipo"] == "Display":
                countd +=1
            elif anuncio["Tipo"] == "Social":
                counts +=1
        str = str + f'Anuncios: {countv} Video, {countd} Display, {counts} Social'
        return str