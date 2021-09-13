from Rectangulo import *

class Cuadrado(Rectangulo): #Cuadrado hereda atributos y metodos del rectangulo
    
    def __init__(self,lado):
        super().__init__(lado,lado) #Llama al constructor de su super clase
