from ClsListaRespuesta import ListaRespuesta
class Usuario:
    def __init__(self, edad: int, email:str,region:int):
        self.__edad=edad
        self.__email=email
        self.__region=region

    @property
    def _edad(self):
        return self.__edad

    @_edad.setter
    def _edad(self, value):
        self.__edad = value

    @property
    def _email(self):
        return self.__email

    @_email.setter
    def _email(self, value):
        self.__email = value

    @property
    def _region(self):
        return self.__region

    @_region.setter
    def _region(self, value):
        self.__region = value


