class Rectangulo:

    def __init__(self,base,altura):
        self.base = base
        self.altura = altura

    def area(self):
        return self.base*self.altura

    def perimetro(self):
        return ((self.base*2)+(self.altura*2))

    

    