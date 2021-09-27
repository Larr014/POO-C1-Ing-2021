from Persona import *
class Empleado(Persona): #Empleado es una sub clase de Persona -> Persona es super clase de Empleado

    def __init__(self):
        super().__init__() #Llamar al constructor de la clase persona
        self.__sueldo_bruto = int(input("Ingrese sueldo bruto: "))
        self.__salud = input('Ingrese sistema salud: ')
        self.__afp = input("Ingrese sistema afp: ")

    def mostrar(self):
        super().mostrar() #Mostrar nombre y rut de la persona
        print(f'Sueldo Bruto: {self.__sueldo_bruto}')#Mostrar el sueldo bruto
        print(f'Salud: {self.__salud}')#Mostrar salud
        print(f'Afp: {self.__afp}')#Mostrar AFP
        self.calcular_salario_neto()

    def calcular_salario_neto(self):
        if self.__salud =="fonasa":
           descuento_salud = self.__sueldo_bruto * 0.07
        else:
            descuento_salud = self.__sueldo_bruto * 0.08
        
        if self.__afp == 'afp1':
            descuento_afp = self.__sueldo_bruto * 0.10
        else :
            descuento_afp = self.__sueldo_bruto * 0.11
        
        self.__sueldo_liquido = self.__sueldo_bruto - descuento_afp - descuento_salud
        print(f'Sueldo Liquido: {self.__sueldo_liquido}')

    def get_rut(self):
        return super().get_rut() #Llamar al get rut de la super clase