#pizza.py
#Author --> Liz

import ingredientes

class clspizza():
    #Atributos estáticos o de clase
    precio=10000
    tamano='familiar'
    
    def __init__(self) -> None:
        #Atributos de instancia o no estáticos
        self.ingredientec=None
        self.ingredientev1=None
        self.ingredientev2=None
        self.masa=None
        self.es_valida = False

    @staticmethod 
    def valida_elemento(elemento,lista_e):
        return True if elemento in lista_e else False
    
    #Método no estático o de instancia
    def realizar_pedido(self):

        ing_proteico = input("Ingrese el ingrediente proteico (pollo, vacuno, carne vegetal): ")
        if self.valida_elemento(ing_proteico, ingredientes.ingredientes_proteicos):
            self.ingrediente_proteico = ing_proteico
        else:
            return False

        ing_vegetal1 = input("Ingrese el primer ingrediente vegetal (tomate, aceitunas, champiñones): ")
        if self.valida_elemento(ing_vegetal1, ingredientes.ingredientes_vegetales):
            self.ingrediente_vegetal1 = ing_vegetal1
        else:
            return False

        ing_vegetal2 = input("Ingrese el segundo ingrediente vegetal (tomate, aceitunas, champiñones): ")
        if self.valida_elemento(ing_vegetal2, ingredientes.ingredientes_vegetales):
            self.ingrediente_vegetal2 = ing_vegetal2
        else:
            return False

        tipo_masa = input("Ingrese el tipo de masa (tradicional, delgada): ")
        if self.valida_elemento(tipo_masa, ingredientes.tipo_masa):
            self.masa = tipo_masa
        else:
            return False

        self.es_valida = True
        return True
