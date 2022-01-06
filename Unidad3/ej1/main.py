import requests
from Post import *
import crud


url = 'https://jsonplaceholder.typicode.com/posts'
r = requests.get(url)
data = r.json()
#print(data)

#for x in data:
#    p = Post(x['userId'],x['id'],x['title'],x['body'])
#    p.mostrar()
#    publicaciones.append(p)
for x in data:
    p = Post(x['userId'],x['id'],x['title'],x['body'])
    #crud.registrar_post(p)
    
#print('verificando lista')
#for publicacion in publicaciones:
#    publicacion.mostrar()
publicaciones = crud.recuperar_todo()
for pub in publicaciones:
    pub.mostrar()