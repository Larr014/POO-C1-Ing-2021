from Empresa import *
from Cliente import *
empresas = [] #Listado de empresas .-> Simulando una base de datos
clientes = [] #Listado de clientes -> 

def registrar_empresa():
    e = Empresa() #Llamando al constructor de empresa -> Crea una empresa
    empresas.append(e) #Guardando en la lista la empresa que creamos

def mostrar_empresas():
    for empresa in empresas: #Por cada empresa dentro de la lista empresas haga ...
        empresa.mostrar() #Muestra los datos de la empresa

def eliminar_empresa():
    mostrar_empresas() #Muestro las empresas
    id = input("Ingrese id de la empresa a eliminar: ") #Pido el id de la empresa a eliminar
    for empresa in empresas:#Por cada empresa dentro de la lista empresas haga ...
        if empresa.get_id() == id: #Comparo el id de la empresa con el id de lo que ingreso el usuario
            empresas.remove(empresa) #Elimino de la lista la empresa que tiene ese id
            break


def agregar_empleado():
    mostrar_empresas() #Mostramos las empresas al usuario
    id = input("Ingrese id de la empresa a buscar: ") #Pido el id de la empresa a buscar
    for empresa in empresas:#Por cada empresa dentro de la lista empresas haga ...
        if empresa.get_id() == id: #Comparo el id de la empresa con el id de lo que ingreso el usuario
            empresa.registrar_empleado() #Registrar empleado en la empresa que tiene ese id
            break

def mostrar_empleados():
    mostrar_empresas() #Mostramos las empresas al usuario
    id = input("Ingrese id de la empresa a buscar: ") #Pido el id de la empresa a buscar
    for empresa in empresas:#Por cada empresa dentro de la lista empresas haga ...
        if empresa.get_id() == id: #Comparo el id de la empresa con el id de lo que ingreso el usuario
            empresa.mostrar_empleados() #Mostrar Empleados de la empresa que tiene ese id
            break


def registrar_cliente():
    c = Cliente() #Llamando al constructor de cliente -> Crea un cliente
    clientes.append(c) #Guardando en la lista el cliente que creamos

def mostrar_cliente():
    for cliente in clientes: #Por cada cliente dentro de la lista clientes haga ...
        cliente.mostrar() #Muestra los datos del cliente

def eliminar_cliente():
    #Terminar ustedes
    pass

def asociar_cliente():
    mostrar_empresas() #Mostramos las empresas al usuario
    id = input("Ingrese id de la empresa a buscar: ") #Pido el id de la empresa a buscar
    for empresa in empresas:#Por cada empresa dentro de la lista empresas haga ...
        if empresa.get_id() == id: #Comparo el id de la empresa con el id de lo que ingreso el usuario
            empresa.mostrar_clientes() #Mostrar todos los clientes dentro de la empresa
            rut = input("Ingrese rut del cliente a asociar: ") #Pedimos al usuario el rut del cliente a asociar
            for cliente in clientes: #Por cada cliente dentro de la lista clientes haga ...
                if cliente.get_rut() == rut: #Comparo el rut del cliente con el rut que ingreso el usuario
                    empresa.registrar_cliente(cliente) #Registrar cliente en la empresa que tiene ese id
            break

def mostrar_clientes_empresa():
    mostrar_empresas() #Mostramos las empresas al usuario
    id = input("Ingrese id de la empresa a buscar: ") #Pido el id de la empresa a buscar
    for empresa in empresas:#Por cada empresa dentro de la lista empresas haga ...
        if empresa.get_id() == id: #Comparo el id de la empresa con el id de lo que ingreso el usuario
            empresa.mostrar_clientes() #Mostrar todos los clientes dentro de la empresa
            break

def eliminar_cliente_empresa():
    mostrar_empresas() #Mostramos las empresas al usuario
    id = input("Ingrese id de la empresa a buscar: ") #Pido el id de la empresa a buscar
    for empresa in empresas:#Por cada empresa dentro de la lista empresas haga ...
        if empresa.get_id() == id: #Comparo el id de la empresa con el id de lo que ingreso el usuario
            empresa.eliminar_cliente #Llamar a la funcion eliminar cliente de la empresa
            break


while True:
    print('1.- Registrar Empresa')
    print('2.- Mostrar Empresas')
    print('3.- Eliminar Empresa')
    print('4.- Registrar Empleado')
    print('5.- Mostrar Empleados')
    print('6.- Despedir Empleado')
    print('7.- Registrar Cliente')
    print('8.- Mostrar Cliente')
    print('9.- Eliminar Cliente')
    print('10.- Asociar cliente a empresa')
    print('11.- Mostrar Clientes de empresa')
    print('12.- Eliminar Cliente de empresa')
    opcion = input("Ingrese una opcion: ")
    if opcion == '1':
        registrar_empresa()
    elif opcion == '2':
        mostrar_empresas()
    elif opcion == '3':
        eliminar_empresa()
    elif opcion == '4':
        agregar_empleado()
    elif opcion == '5':
        mostrar_empleados()
    elif opcion == '6':
        pass #Trabajar ustedes
    elif opcion == '7':
        registrar_cliente()
    elif opcion == '8':
        mostrar_cliente()
    elif opcion == '9':
        eliminar_cliente()
    elif opcion == '10':
        asociar_cliente()
    elif opcion == '11':
        mostrar_clientes_empresa()
    elif opcion=='12':
        eliminar_cliente_empresa()
    else:
        print("La opcion ingresada no es valida")