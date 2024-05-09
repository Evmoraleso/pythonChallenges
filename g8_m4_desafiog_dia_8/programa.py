from ClsAbsMembresia import Gratis

m=Gratis("emo@gmail.com","374987392")

print(m.get_email())
print(m.get_ntarjeta())
print(m.get_costo())
print(m.get_dispositivo())
print(type(m))
print("")

m=m.cambiarsuscripcion(1)

print(m.get_email())
print(m.get_ntarjeta())
print(m.get_costo())
print(m.get_dispositivo())
print(type(m))
print("")

m=m.cambiarsuscripcion(2)

print(m.get_email())
print(m.get_ntarjeta())
print(m.get_costo())
print(m.get_dispositivo())
print(type(m))
print("")

m=m.cambiarsuscripcion(3)

print(m.get_email())
print(m.get_ntarjeta())
print(m.get_costo())
print(m.get_dispositivo())
print(type(m))
print("")

m=m.cambiarsuscripcion(4)

print(m.get_email())
print(m.get_ntarjeta())
print(m.get_costo())
print(m.get_dispositivo())
print(type(m))
print("")

m=m.cancelarsuscripcion()

print(m.get_email())
print(m.get_ntarjeta())
print(m.get_costo())
print(m.get_dispositivo())
print(type(m))
print("")
