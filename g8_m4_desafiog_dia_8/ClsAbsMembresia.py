from abc import ABC, abstractmethod
class Membresia():

    def __init__(self, email: str, ntarjeta: str, costo: int, dispositivo: int):
        self.__email=email
        self.__ntarjeta=ntarjeta
        self.__costo = costo
        self.__dispositivo = dispositivo
    
    @abstractmethod
    def cambiarsuscripcion():
        pass

    @abstractmethod
    def cancelarsuscripcion():
        pass

    def get_email(self):
        return self.__email

    def get_ntarjeta(self):
        return self.__ntarjeta
    
    def get_costo(self):
        return self.__costo

    def get_dispositivo(self):
        return self.__dispositivo
    
    def set_costo(self, costo: int):
        self.__costo = costo
    
    def set_dispositivo(self, dispositivo: int):
        self.__dispositivo = dispositivo    

    
class Gratis(Membresia):
    def __init__(self, email: str, ntarjeta: str):
        super().__init__(email, ntarjeta, 0, 1)
        
    def cambiarsuscripcion(self, tipo_membresia):
        if tipo_membresia == 1:
            nueva_membresia = Basica(self.get_email(),self.get_ntarjeta())
        elif tipo_membresia == 2:
            nueva_membresia = Familiar(self.get_email(),self.get_ntarjeta())
        elif tipo_membresia == 3:
            nueva_membresia = SinConexion(self.get_email(),self.get_ntarjeta())
        elif tipo_membresia == 4:
            nueva_membresia = Pro(self.get_email(),self.get_ntarjeta())
        else:
            nueva_membresia = self
        return nueva_membresia

class Basica(Membresia):
    def __init__(self, email: str, ntarjeta: str):
        super().__init__(email, ntarjeta, 3000, 2)

    def cambiarsuscripcion(self, tipo_membresia):
        if tipo_membresia == 2:
            nueva_membresia = Familiar(self.get_email(),self.get_ntarjeta())
        elif tipo_membresia == 3:
            nueva_membresia = SinConexion(self.get_email(),self.get_ntarjeta())
        elif tipo_membresia == 4:
            nueva_membresia = Pro(self.get_email(),self.get_ntarjeta())
        else:
            nueva_membresia = self
        return nueva_membresia        

    def cancelarsuscripcion(self):
        return Gratis(self.get_email(),self.get_ntarjeta())

class Familiar(Basica,Membresia):
    def __init__(self, email: str, ntarjeta: str):
        super().__init__(email, ntarjeta)
        self.set_costo(5000)
        self.set_dispositivo(5)
        self.__diasfree = 7
        #puso set de costo y dispositivo no etiendo por que
    def cambiarsuscripcion(self, tipo_membresia):
        if tipo_membresia == 1:
            nueva_membresia = Basica(self.get_email(),self.get_ntarjeta())
        elif tipo_membresia == 3:
            nueva_membresia = SinConexion(self.get_email(),self.get_ntarjeta())
        elif tipo_membresia == 4:
            nueva_membresia = Pro(self.get_email(),self.get_ntarjeta())
        else:
            nueva_membresia = self
        return nueva_membresia
    
    def modificarcontrolparental():
        pass

class SinConexion(Basica,Membresia):
    def __init__(self, email: str, ntarjeta: str):
        super().__init__(email, ntarjeta)
        self.set_costo(3500)
        self.set_dispositivo(2)
        self.__diasfree = 7

    def cambiarsuscripcion(self, tipo_membresia):
        if tipo_membresia == 1:
            nueva_membresia = Basica(self.get_email(),self.get_ntarjeta())
        elif tipo_membresia == 2:
            nueva_membresia = Familiar(self.get_email(),self.get_ntarjeta())
        elif tipo_membresia == 4:
            nueva_membresia = Pro(self.get_email(),self.get_ntarjeta())
        else:
            nueva_membresia = self
        return nueva_membresia
    
    def aumentarcontenido():
        pass

class Pro(SinConexion,Familiar,Membresia):
    def __init__(self, email: str, ntarjeta: str):
        super().__init__(email, ntarjeta)
        self.set_costo(7000)
        self.set_dispositivo(6)
        self.__diasfree = 15

    def cambiarsuscripcion(self, tipo_membresia):
        if tipo_membresia == 1:
            nueva_membresia = Basica(self.get_email(),self.get_ntarjeta())
        elif tipo_membresia == 2:
            nueva_membresia = Familiar(self.get_email(),self.get_ntarjeta())
        elif tipo_membresia == 3:
            nueva_membresia = SinConexion(self.get_email(),self.get_ntarjeta())
        else:
            nueva_membresia = self
        return nueva_membresia
    