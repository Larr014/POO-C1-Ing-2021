class Figura:

    def __init__(self,lado=0,longitud=0.0,apotema=0.0):
        self.lado = lado
        self.long = longitud
        self.__apotema = apotema #variable privada por que tiene __
        self.__perimetro = self.lado*self.long

    def __area(self):
        resultado = (self.__apotema*self.__perimetro)/2
        return resultado

    def imprimir(self):
        r = self.__area()
        print(f"El area es: {r}")
