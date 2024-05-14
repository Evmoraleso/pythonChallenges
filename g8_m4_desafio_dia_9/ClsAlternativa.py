class Alternativa:

    def __init__(self,contenido: str, ayuda: str=''):
        self.__contenido=contenido
        self.__ayuda=ayuda

    @property
    def _contenido(self):
        return self.__contenido

    @_contenido.setter
    def _contenido(self, value):
        self.__contenido = value

    @property
    def _ayuda(self):
        return self.__ayuda

    @_ayuda.setter
    def _ayuda(self, value):
        self.__ayuda = value

    def mostrarAlternativa(self):
        return self
    
    