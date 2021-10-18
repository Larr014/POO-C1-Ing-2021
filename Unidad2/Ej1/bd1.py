import mysql.connector #Estamos indicando que usaremos mysql

#Declarar credenciales de acceso a la base de datos
credenciales = {
    'host':'localhost',
    'user':'root',
    'password':'',
    'database':'bding'
}

#Establecer conexion con esas credenciales
conexion = mysql.connector.connect(**credenciales)

#Cursor: Estructura que ejecuta query, puede recuperar las repuestas de la query (puente)
cursor = conexion.cursor()

#Crear una query
query = "SELECT * FROM people" #Recupera todo el contenido de la tabla people

#Cursor que ejecute la query
cursor.execute(query)

#Cursor retorna el resultado
resultados = cursor.fetchall() #Retorna todo

print(resultados)
print()

for tupla in resultados:
    print(tupla)
print()

for tupla in resultados:
    print(f'{tupla[0]} {tupla[1]} {tupla[7]}')

