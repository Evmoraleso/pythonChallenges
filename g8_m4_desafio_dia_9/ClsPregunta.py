from ClsAlternativa import Alternativa
class Pregunta:
    def __init__(self, enunciado: str, ayuda: str, mandatorio: bool):
        self.__enunciado=enunciado
        self.__ayuda=ayuda
        self.__mandatorio=mandatorio
        self.__listAlternativas=[Alternativa]

    @property
    def _enunciado(self):
        return self.__enunciado

    @_enunciado.setter
    def _enunciado(self, value):
        self.__enunciado = value

    @property
    def _ayuda(self):
        return self.__ayuda

    @_ayuda.setter
    def _ayuda(self, value):
        self.__ayuda = value

    @property
    def _mandatorio(self):
        return self.__mandatorio

    @_mandatorio.setter
    def _mandatorio(self, value):
        self.__mandatorio = value

    def get_listAlternativas(self):
        return self.__listAlternativas

    def set_listAlternativas(self, value):
        self.__listAlternativas.append(value)

    def mostrarPregunta(self):
        return self
