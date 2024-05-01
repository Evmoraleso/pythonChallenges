import random
class personaje():

    def __init__(self, nombre: str) -> None:
        self.var_nombre=nombre
        self.var_nivel=1
        self.var_experiencia=0
        
    @property
    def get_var_nombre(self):
        return self.var_nombre
    
    @property
    def get_var_nivel(self):
        return self.var_nivel

    @property
    def get_var_experiencia(self):
        return self.var_experiencia

    @get_var_nombre.setter
    def set_var_nombre(self, nombre: str):
        self.var_nombre=nombre

    @get_var_nivel.setter
    def set_var_nivel(self, nivel: str):
        self.var_nivel=nivel

    @get_var_experiencia.setter
    def set_var_experiencia(self, experiencia: str):
        self.var_experiencia=experiencia

    #METODO calcula probabilidad de ganar
    def get_calcula_probabilidad(self, orco: 'personaje') -> int:
        if self.get_var_nivel < orco.get_var_nivel:
            return 33
        elif self.get_var_nivel > orco.get_var_nivel:
            return 66
        elif self.get_var_nivel == orco.get_var_nivel:
            return 50
        
    #METODO update estado y nivel
    def set_update_experiencia_nivel(self,nueva_experiencia):
        self.set_var_experiencia=self.get_var_experiencia+nueva_experiencia
        if self.get_var_experiencia > 99:
            self.set_var_nivel=self.get_var_nivel + 1
            self.set_var_experiencia=self.get_var_experiencia-100
        elif self.get_var_experiencia < 0:
            if self.get_var_nivel > 1: 
                self.set_var_nivel=self.set_var_nivel - 1
            self.set_var_experiencia=0

    #METODO random
    @staticmethod
    def get_random(probabilidad: int) -> float:
        numero_azar = random.uniform(0, 1)
        return numero_azar < (probabilidad/100) #Gana

    #SOBRE CARGA
    def __lt__(self, otro):
        # Sobrecarga para comparar "menor que"
        return self.valor < otro.valor

    def __gt__(self, otro):
        # Sobrecarga para comparar "mayor que"
        return self.valor > otro.valor

    def __eq__(self, otro):
        # Sobrecarga para comparar "igual que"
        return self.valor == otro.valor