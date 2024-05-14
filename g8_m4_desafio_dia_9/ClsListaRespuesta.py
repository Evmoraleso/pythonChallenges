class ListaRespuesta:
    def __init__(self,usuario: str, respuestas=None):        
        self.__usuario=usuario
        self.__listaRespuesta = respuestas if respuestas else []

    @property
    def _respuesta(self):
        return self.__listaRespuesta

    @_respuesta.setter
    def _respuesta(self, value):
        self.__listaRespuesta=value

    @property
    def _usuario(self):
        return self.__usuario

    @_usuario.setter
    def _usuario(self, value):
        self.__usuario = value
