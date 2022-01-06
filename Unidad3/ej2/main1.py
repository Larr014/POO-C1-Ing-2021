import requests

url = 'http://larr.cl/larr.cl/json/post1.php'

while True:
    nombre = input('Ingrese nombre: ')
    apellido = input('Ingrese apellido: ')
    json = {'nombre': nombre,'apellido':apellido}
    r = requests.post(url,json)
