from Persona import *
class Cliente(Persona):

    def __init__(self):
        super().__init__()
        self.__telefono = input("Ingrese telefono: ")

    def mostrar(self):
        super().mostrar()
        print(f'Telefono: {self.__telefono}')

    def get_rut(self):
        return super().get_rut()