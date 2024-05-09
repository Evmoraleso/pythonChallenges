from ClsAbsTienda import Tienda
from ClsProducto import Producto

class Restaurante(Tienda):
    

    def ingresar_producto(self, nombre:str, precio: int, stock=0):
        var_prod = next((producto for producto in self.lista_productos if producto.nombre.lower() == nombre.lower()),None)
        if not isinstance(var_prod, Producto):
            producto=Producto(nombre,precio,0)
            self.lista_productos.append(producto)

    def listar_producto(self):
        lista=[]
        for producto in self.lista_productos:
            cadena='Producto: '+producto.nombre+' Precio: '+str(producto.precio)
            lista.append(cadena)
        return lista

    def realizar_venta(self, nombre: str, cantidad: int):
        var_prod = next((producto for producto in self.lista_productos if producto.nombre.lower() == nombre.lower()),None)
        if var_prod != None:
            return True
        else: return False