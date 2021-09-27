from Empleado import *
class Empresa:

    

    def __init__(self):
        self.__id = input('Ingrese id de la Empresa: ')
        self.__nombre = input("Ingrese nombre de la Empresa: ")
        self.__empleados = [] #Creamos una lista de empleados dentro de la empresa por que usamos rombo negro
        self.__clientes = [] #Creamos una lista de clientes dentro de la empresa por que usamos rombo blanco

    def mostrar(self):
        print(f'Id: {self.__id} Nombre: {self.__nombre}')

    #Es un metodo que me permite compartir un atributo privado
    def get_id(self):
        return self.__id

    def registrar_empleado(self):
        e = Empleado() #Llamando al constructor de empleado -> Crea un empleado
        self.__empleados.append(e) #Guardando en la lista el empleado que creamos

    def mostrar_empleados(self):
        for empleado in self.__empleados: #Por cada empleado dentro de la lista empleados haga ...
            empleado.mostrar() #Muestra los datos del empleado

    def eliminar_empleado(self):
        self.mostrar_empleados() #Muestro los empleados
        rut = input("Ingrese rut del empleado a eliminar: ") #Pido el rut del empleado a eliminar
        for empleado in self.__empleados:#Por cada empleado dentro de la lista empleados haga ...
            if empleado.get_rut() == rut: #Comparo el rut del empleado con el rut de lo que ingreso el usuario
                self.__empleados.remove(empleado) #Elimino de la lista el empleado que tiene ese rut
                break

    def registrar_cliente(self, cliente):
        self.__clientes.append(cliente)

    def mostrar_clientes(self):
        for cliente in self.__clientes:
            cliente.mostrar()

    def eliminar_cliente(self):
        self.mostrar_clientes() #Muestro los empleados
        rut = input("Ingrese rut del cliente a eliminar: ") #Pido el rut del empleado a eliminar
        for cliente in self.__clientes:#Por cada empleado dentro de la lista empleados haga ...
            if cliente.get_rut() == rut: #Comparo el rut del empleado con el rut de lo que ingreso el usuario
                self.__clientes.remove(cliente) #Elimino de la lista el empleado que tiene ese rut
                break