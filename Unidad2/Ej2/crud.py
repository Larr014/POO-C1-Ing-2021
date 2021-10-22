import mysql.connector

credenciales = {
    'host':'localhost',
    'user':'root',
    'password':'',
    'database':'bding'
}

conexion = mysql.connector.connect(**credenciales)
cursor = conexion.cursor()

def registrar_persona(p):
    query = "INSERT INTO people (fullname,profession,birth,genre,bodyweight,height,nationality) VALUES (%s,%s,%s,%s,%s,%s,%s)"
    values = (p.get_fullname(),p.get_profession(),p.get_birth(),p.get_genre(),p.get_bodyweight(),p.get_height(),p.get_nationality())
    cursor.execute(query,values)
    #Cuando ejecuto una query que realiza alguna cambion en la base de datos debo hacer commit
    conexion.commit()

def mostrar_personas():
    query = "SELECT * FROM people"
    cursor.execute(query)
    filas = cursor.fetchall() #Cuando tienes una query (select) debes recuperar sus resultados
    for fila in filas:
        print(f'Nombre: {fila[1]} ** Peso: {fila[5]}')