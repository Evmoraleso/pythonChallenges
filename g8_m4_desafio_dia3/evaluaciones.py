# evaluaciones.py
#Author --> Liz

from pizza import clspizza
# 5 a. Llama al atributo precio y tamaño de la clase clspizza
print("Precio de la pizza:", clspizza.precio)
print("Tamaño de la pizza:", clspizza.tamano)

# 5 b. Llama al método estático valida_elemento de la clase clspizza
print(clspizza.valida_elemento('salsa de tomate',['salsa de tomate','salsa bbq']))

# 5 c. y d. Instancia a la clase clspizza y crea el objeto/el objeto obj_pizza llama al método no estático realizar_pedido
obj_pizza = clspizza()
if obj_pizza.realizar_pedido():
    print(f'Ingredientes vegetales:\n{obj_pizza.ingrediente_vegetal1} - {obj_pizza.ingrediente_vegetal2}\nIngredente Proteico: {obj_pizza.ingrediente_proteico}\nTipo de masa: {obj_pizza.masa}\nPizza válida.')
else:
    print("Pizza no válida. Inténtalo nuevamente.")

# 5 e. La clase clspizza llama al atributo de instancia o no estático provocando un error.
print(clspizza.es_valida)