from clste import te

#Crear dos instancias (4.a b)
te1=te(None,None,None,None)
te2=te(None,None,None,None)
#(4. c)
print(type(te1))
print(type(te2))
#(4. d)
if (type(te1)==type(te2)):
    print('Ambos objetos son del mismo tipo')
else:
    print('Los objetos no son del mismo tipo')