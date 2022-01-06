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
    #Cuando ejecuto una query que realiza alguna cambio en la base de datos debo hacer commit
    conexion.commit()

def mostrar_personas():
    query = "SELECT * FROM people"
    cursor.execute(query)
    filas = cursor.fetchall() #Cuando tienes una query (select) debes recuperar sus resultados
    for fila in filas:
        print(f'Nombre: {fila[1]} ** Peso: {fila[5]}')


def buscar_persona(id):
    query = "SELECT * FROM people WHERE id = %s"
    values = (id,)
    #binding
    cursor.execute(query,values)
    fila = cursor.fetchone() #Cuando un select retorna como máximo 1 valor se usa fetchone
    if fila!=None: #Si fila tiene algo
        print(f'ID: {fila[0]} | Nombre: {fila[1]}')
        return fila
    else:
        print("No existe el id")

def modificar_persona(persona):
    query = "UPDATE people SET fullname = %s,profession = %s, birth=%s,genre=%s,bodyweight=%s,height=%s,nationality=%s WHERE id = %s"
    values = (persona.get_fullname(),persona.get_profession(),persona.get_birth(),persona.get_genre(),persona.get_bodyweight(),persona.get_height(),persona.get_nationality(),persona.get_id())
    #binding
    cursor.execute(query,values)
    conexion.commit()

def eliminar_persona(p):
    query = "DELETE FROM people WHERE id = %s"
    values = (p.get_id(),)
    cursor.execute(query,values)
    conexion.commit()