class Empleado:

    def __init__(self):
        self.nombre = input("Ingrese nombre del empleado: ")
        self.sueldo = float(input(f'Ingrese sueldo de {self.nombre}: '))

    def mostrar(self):
        print("------")
        print(f'Nombre: {self.nombre}')
        print(f'Sueldo: {self.sueldo}')
        print("------")

    def impuesto(self):
        if self.sueldo>3000:
            print(f'{self.nombre} Paga Impuesto')
        else:
            print(f'{self.nombre} No Paga Impuesto')