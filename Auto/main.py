from Auto import *

a1 = Auto("azul",5) #Crear un auto
print(a1.ruedas)
print(f'Auto1: color:{a1.color}')
print(f'Auto1: aceleracion:{a1.aceleracion}')
print(f'Auto1: velocidad: {a1.velocidad}')
a2 = Auto("rojo",10)
print(a2.ruedas)
print(f'Auto2: color: {a2.color}')
print(f'Auto2: aceleracion: {a2.aceleracion}')

print("----")
a1.avanza()
print(f'Auto1: velocidad: {a1.velocidad}')
a1.avanza()
print(f'Auto1: velocidad: {a1.velocidad}')

for i in range(4):
    a2.avanza()
print(f'Auto2: velocidad: {a2.velocidad}')

print("---")
a1.frena()
print(f'Auto1: velocidad: {a1.velocidad}')
a2.frena()
a2.frena()
a2.frena()
print(f'Auto2: velocidad: {a2.velocidad}')
a2.frena()
a2.frena()
a2.frena()
print(f'Auto2: velocidad: {a2.velocidad}')