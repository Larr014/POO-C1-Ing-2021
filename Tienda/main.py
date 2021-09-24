from Empresa import *

empresas = [] #Listado de empresas .-> Simulando una base de datos


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








while True:
    print('1.- Registrar Empresa')
    print('2.- Mostrar Empresas')
    print('3.- Eliminar Empresa')
    opcion = input("Ingrese una opcion: ")
    if opcion == '1':
        registrar_empresa()
    elif opcion == '2':
        mostrar_empresas()
    elif opcion == '3':
        eliminar_empresa()
    else:
        print("La opcion ingresada no es valida")