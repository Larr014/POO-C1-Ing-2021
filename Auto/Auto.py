class Auto:

    ruedas = 4 #Atributo de Clase

    def __init__(self,color,aceleracion): #El constructor crea un objeto con los parametros que uno le pasa
        self.color = color
        self.aceleracion = aceleracion
        self.velocidad = 0

    def avanza(self):
        self.velocidad = self.velocidad + self.aceleracion

    def frena(self):
        v = self.velocidad - self.aceleracion
        if v<0:
            v = 0
        self.velocidad = v