from abc import ABC, abstractmethod
from ClsPregunta import Pregunta
from ClsListaRespuesta import ListaRespuesta
class Encuesta(ABC):

    def __init__(self,nombre: str):
        super().__init__()
        self.__nombre = nombre
        self.__listaPreguntas=[Pregunta]
        self.__listaRespuesta=ListaRespuesta

        
    @property
    def _nombre(self):
        return self.__nombre

    @_nombre.setter
    def _nombre(self, value):
        self.__nombre = value

    @property
    def _listaPreguntas(self):
        return self.__listaPreguntas

    @_listaPreguntas.setter
    def _listaPreguntas(self, value):
        self.__listaPreguntas.append(value)

    @property
    def _listaRespuesta(self):
        return self.__listaRespuesta

    @_listaRespuesta.setter
    def _listaRespuesta(self, value):
        self.__listaRespuesta=value

    @abstractmethod
    def mostrarEncuesta(self):
        pass
    
    @abstractmethod
    def agregarRespuestas(self):
        pass

class EncuestaEdad(Encuesta):
    
    def __init__(self, nombre: str, edadMinima: int, edadMaxima: int):
        super().__init__(nombre)
        self.__edadMinima= edadMinima
        self.__edadMaxima= edadMaxima    

    def get_edadMinima(self):
        return self.__edadMinima

    def set_edadMinima(self, value):
        self.edadMinima = value

    def get_edadMaxima(self):
        return self.__edadMaxima

    def set_edadMaxima(self, value):
        self.__edadMaxima = value

    def mostrarEncuesta(self):         
        return self
     

    def agregarRespuestas(self, lista: list[ListaRespuesta], usuario)->bool:
            if self.get_edadMinima <= usuario._edad <= self.get_edadMaxima:
                self._listaRespuesta(lista)
                return True
            else:
                return False

class EncuestaRegion(Encuesta):
    def __init__(self, nombre: str):
        super().__init__(nombre)
        self.listaRegiones = [1,2,4,6,8,10]

    def get_listaRegiones(self):
        return self.listaRegiones

    def mostrarEncuesta(self):      
        return self    
    
    def agregarRespuestas(self, lista: list[ListaRespuesta], usuario)->bool:
            if usuario._region in self.get_listaRegiones:
                self._listaRespuesta(lista)
                return True
            else:
                return False
