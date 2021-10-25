import crud
from Persona import *
def registrar_persona():
    print("Registrando persona .....")
    nombre = input("Ingrese nombre: ")
    profesion = input("Ingrese profesion: ")
    fecha = input("Ingrese fecha de nacimiento: (Año-Mes-Dia) ")
    genero = input("Ingrese genero: (M/F) ").upper()
    peso = float(input("Ingrese peso: "))
    altura = float(input("Ingrese altura: "))
    nacionalidad = input("Ingrese nacionalidad: ")
    #Un objeto persona creado con los datos que ingresa el usuario
    p = Persona(nombre,profesion,fecha,genero,peso,altura,nacionalidad)
    #Usar el crud
    crud.registrar_persona(p)

def buscar_persona():
    #pedir el id
    id = input("Ingrese id de la persona a buscar: ")
    #buscar el id
    fila = crud.buscar_persona(id)
    return fila
    #mostrar resultado

def modificar_persona():
    #pedir el id
    fila = buscar_persona()
    p = Persona(fila[1],fila[2],fila[3],fila[4],fila[5],fila[6],fila[7],fila[0])
    #Preguntar que quiere modificar
    respuesta = input("Desea modificar el nombre: s/n").lower()
    if respuesta == 's':
        nombre = input("Ingrese nombre: ")
        p.set_fullname(nombre) #Actualizar el objeto persona con el campo nuevo
    respuesta = input("Desea modificar la profesion: s/n").lower()
    if respuesta == 's':
        profesion = input("Ingrese profesion: ")
        p.set_profession(profesion)
    respuesta = input("Desea modificar la fecha: s/n").lower()
    if respuesta == 's':
        fecha = input("Ingrese fecha de nacimiento: (Año-Mes-Dia) ")
        p.set_birth(fecha)
    respuesta = input("Desea modificar el genero: s/n").lower()
    if respuesta == 's':
        genero = input("Ingrese genero: (M/F) ").upper()
        p.set_genre(genero)
    respuesta = input("Desea modificar el peso: s/n").lower()
    if respuesta == 's':
        peso = float(input("Ingrese peso: "))
        p.set_bodyweight(peso)
    respuesta = input("Desea modificar la altura: s/n").lower()
    if respuesta == 's':
        altura = float(input("Ingrese altura: "))
        p.set_height(altura)
    respuesta = input("Desea modificar la nacionalidad: s/n").lower()
    if respuesta == 's':
        nacionalidad = input("Ingrese nacionalidad: ")
        p.set_nationality(nacionalidad)
    crud.modificar_persona(p)





    #Modificar lo que se pregunto

def eliminar_persona():
    pass

def mostrar_personas():
    crud.mostrar_personas()




while True:
    print('1.- Registrar Persona')
    print('2.- Buscar Persona')
    print('3.- Modificar Persona')
    print('4.- Eliminar Persona')
    print('5.- Mostrar Personas')
    opcion = input("Ingrese una opcion: ")
    if opcion == '1':
        registrar_persona()
    elif opcion == '2':
        buscar_persona()
    elif opcion == '3':
        modificar_persona()
    elif opcion == '4':
        eliminar_persona()
    elif opcion == '5':
        mostrar_personas()
    else:
        print("Opcion incorrecta")