class Producto():

    def __init__(self, nombre: str, precio: int, stock: int =0):
        self.nombre=nombre
        self.precio=precio
        self.stock=stock

    @property
    def get_nombre(self)-> str:
        return self.nombre

    @property
    def get_precio(self)-> int:
        return self.precio
        
    @property
    def get_stock(self)-> int:
        return self.stock
          
    @get_stock.setter
    def set_stock(self, stock: int):
        if stock < 0:
            self.stock = 0
        else: self.stock=stock