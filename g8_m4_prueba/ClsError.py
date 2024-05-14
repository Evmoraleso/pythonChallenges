class Error(Exception):
    def __init__(self, mensaje: None):
        self.__mensaje = mensaje 

class LargoExcedido(Error):
    def __str__(self):
        if self._Error__mensaje is not None: 
            return super().__str__()

class SubTipoInvalidoError(Error):
    def __str__(self):
        if self._Error__mensaje is not None: 
            return super().__str__()

