from ClsAbsTienda import Tienda
from ClsProducto import Producto

class Supermercado(Tienda):
    
    def ingresar_producto(self, nombre:str, precio: int, stock: int):
        var_prod = next((producto for producto in self.lista_productos if producto.nombre.lower() == nombre.lower()),None)
        if isinstance(var_prod, Producto):
            var_prod.set_stock=var_prod.get_stock + stock
        else:
            producto=Producto(nombre,precio,stock)
            self.lista_productos.append(producto)

    def listar_producto(self):
        lista=[]
        for producto in self.lista_productos:
            if producto.stock < 10:
                lista.append('Nombre: '+producto.nombre+' Precio: '+str(producto.precio)+' Stock: '+str(producto.stock)+' '+'Pocos productos disponibles')
            else:
                lista.append('Nombre: '+producto.nombre+' Precio: '+str(producto.precio)+' Stock: '+str(producto.stock))
        return lista    
    
    def realizar_venta(self, nombre: str, cantidad: int):
        var_prod = next((producto for producto in self.lista_productos if producto.nombre.lower() == nombre.lower()),None)
        if isinstance(var_prod, Producto):
            if var_prod.get_stock > 0:
                if cantidad > var_prod.get_stock:
                    var_prod.set_stock=0
                    return True
                else:
                    var_prod.set_stock=var_prod.get_stock-cantidad
                    return True
            return False
