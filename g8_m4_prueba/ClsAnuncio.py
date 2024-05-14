from abc import ABC, abstractmethod
from ClsError import SubTipoInvalidoError
class Anuncio():
    def __init__(self, ancho: int, alto: int, url_archivo: str, url_clic: str, sub_tipo: str) -> None:
        self.__ancho = ancho
        self.__alto = alto
        self.__url_archivo = url_archivo
        self.__url_clic = url_clic
        self.__sub_tipo = sub_tipo

    @staticmethod
    def mostrar_formatos():
        print("Formatos y subtipos disponibles para crear anuncios:")
      
        print("\nFormato Video:")
        print("==========")
        for subtipo in Video.SUB_TIPOS:
            print("-", subtipo)
        
        print("\nFormato Display:")
        print("==========")
        for subtipo in Display.SUB_TIPOS:
            print("-", subtipo)
        
        print("\nFormato Social:")
        print("==========")
        for subtipo in Social.SUB_TIPOS:
            print("-", subtipo)

    @abstractmethod
    def comprimir_anuncio():
        pass

    @abstractmethod
    def redimensionar_anuncio():
        pass

class Video(Anuncio):
    FORMATO = "Video"
    SUB_TIPOS = ("instream","outstream")

    def __init__(self, ancho: int, alto: int, url_archivo: str, url_clic: str, sub_tipo: str, duracion: int) -> None:
        super().__init__(ancho, alto, url_archivo, url_clic, sub_tipo)
        self.__ancho = 1
        self.__alto = 1
        self.__duracion = duracion

    @property
    def _url_archivo(self):
        return self.__url_archivo

    @_url_archivo.setter
    def _url_archivo(self, value):
        self.__url_archivo = value

    @property
    def _url_clic(self):
        return self.__url_clic

    @_url_clic.setter
    def _url_clic(self, value):
        self.__url_clic = value

    @property
    def _sub_tipo(self):
        return self.__sub_tipo

    @_sub_tipo.setter
    def _sub_tipo(self, value):
        if value not in self.SUB_TIPOS:
            raise SubTipoInvalidoError('SubTipo NO valido.')
        else:
            self.__sub_tipo = value

    @property
    def _duracion(self):
        return self.__duracion
        
    @_duracion.setter
    def _duracion(self, value):
        if value > 0:
            self.__duracion = value
        else:
            self.__duracion = 5

    def comprimir_anuncio():
        print("COMPRESIÓN DE VIDEO NO IMPLEMENTADA AÚN")     

    def redimensionar_anuncio():
        print( "RECORTE DE VIDEO NO IMPLEMENTADO AÚN")

class Display(Anuncio):
    FORMATO = "Display"
    SUB_TIPOS = ("tradicional","antive")

    def __init__(self, ancho: int, alto: int, url_archivo: str, url_clic: str, sub_tipo: str) -> None:
        super().__init__(ancho, alto, url_archivo, url_clic, sub_tipo)

    @property
    def _sub_tipo(self):
        return self.__sub_tipo
    
    @_sub_tipo.setter
    def _sub_tipo(self, value):
        if value not in self.SUB_TIPOS:
            raise SubTipoInvalidoError('SubTipo NO valido.')
        else:
            self.__sub_tipo = value

    def comprimir_anuncio():
        print("COMPRESIÓN DE ANUNCIOS DISPLAY NO IMPLEMENTADA AÚN")     

    def redimensionar_anuncio():
        print( "REDIMENSIONAMIENTO DE ANUNCIOS DISPLAY NO IMPLEMENTADO AÚN")

class Social(Anuncio):
    FORMATO = "Social"
    SUB_TIPOS = ("facebook","linkedin")
    
    def __init__(self, ancho: int, alto: int, url_archivo: str, url_clic: str, sub_tipo: str) -> None:
        super().__init__(ancho, alto, url_archivo, url_clic, sub_tipo)

    @property
    def _sub_tipo(self):
        return self.__sub_tipo
    
    @_sub_tipo.setter
    def _sub_tipo(self, value):
        if value not in self.SUB_TIPOS:
            raise SubTipoInvalidoError('SubTipo NO valido.')
        else:
            self.__sub_tipo = value

    def comprimir_anuncio():
        print("COMPRESIÓN DE ANUNCIOS DE REDES SOCIALES NO IMPLEMENTADA AÚN")     

    def redimensionar_anuncio():
        print("REDIMENSIONAMIENTO DE ANUNCIOS DE REDES SOCIALES NO IMPLEMENTADO AÚN")