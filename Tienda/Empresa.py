class Empresa:

    def __init__(self):
        self.__id = input('Ingrese id de la Empresa: ')
        self.__nombre = input("Ingrese nombre de la Empresa: ")

    def mostrar(self):
        print(f'Id: {self.__id} Nombre: {self.__nombre}')

    #Es un metodo que me permite compartir un atributo privado
    def get_id(self):
        return self.__id