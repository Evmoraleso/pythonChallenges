class DimensionError(Exception):
    def __init__(self, mensaje: None, dimension: int, maxmin: int):
        self.__mensaje = mensaje 
        self.__dimension = dimension
        self.__maxmin = maxmin

    def __str__(self):
        if self.__mensaje is not None and self.__dimension is None and self.__maxmin is None: 
            return super().__str__() 
        else:
            ret = f"El valor de la dimensión '{self.__mensaje}'"
            if self.__dimension != None:
                ret += f" ingresado: {self.__dimension} esta fuera de rango. "
            if self.__maxmin != None:
                ret += f"El valor máximo permitido es {self.__maxmin} "
            ret += "y valor mínimo permitido es 1."
            return ret


