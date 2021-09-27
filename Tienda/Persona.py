class Persona:

    def __init__(self):
        self.__nombre = input("Ingrese nombre: ")
        self.__rut = input("Ingrese rut: ")

    def mostrar(self):
        print(f'Nombre: {self.__nombre}')
        print(f'Rut: {self.__rut}')

    def get_rut(self):
        return self.__rut