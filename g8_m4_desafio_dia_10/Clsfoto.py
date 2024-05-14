from Clserror import DimensionError
class Foto():
    MAX = 2500

    def __init__(self, ancho: int, alto: int, ruta: str) -> None:
        self.__ancho = ancho
        self.__alto = alto
        ruta = ruta

    @property
    def ancho(self) -> int:
        return self.__ancho

    @ancho.setter#modificar
    def ancho(self, ancho) -> None:
        if ancho < 1 or ancho > self.MAX:
            raise DimensionError('ancho',ancho, self.MAX)
        else: self.__ancho = ancho

    @property
    def alto(self) -> int:
        return self.__alto

    @alto.setter#modificar
    def alto(self, alto) -> None:
        if alto < 1 or alto > self.MAX:
            raise DimensionError('alto',alto, self.MAX)
        else: self.__alto = alto
