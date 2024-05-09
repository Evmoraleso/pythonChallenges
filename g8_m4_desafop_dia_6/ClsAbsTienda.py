from abc import ABC, abstractmethod
class Tienda(ABC):

    def __init__(self,nombre: str,costod: int):
        #super().__init__()
        self.nombre=nombre
        self.costod=costod
        self.lista_productos=[]

    @abstractmethod
    def ingresar_producto():
        pass

    @abstractmethod
    def listar_producto():
        pass    

    @abstractmethod
    def realizar_venta():
        pass