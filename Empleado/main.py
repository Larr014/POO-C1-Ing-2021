from Empleado import *

e1 = Empleado()
e2 = Empleado()
e1.mostrar()
e2.mostrar()
e1.impuesto()
e2.impuesto()

#Llegaremos hasta esto en algun momento

empleados = []
cantidad = int(input("Ingrese numero de empleados: "))
for i in range(cantidad):
    em = Empleado() #Creo un objeto, un empleado
    empleados.append(em) #Agrego a mi lista el empleado

for x in empleados:
    x.impuesto()