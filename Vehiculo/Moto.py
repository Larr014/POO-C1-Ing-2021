from Vehiculo import *

class Moto(Vehiculo):

    def __init__(self):
        super().__init__("Motocicleta")

    def num_ruedas(self):
        return 2