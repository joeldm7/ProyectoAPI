"""pedirle una cancion y a través del id volver a llamar a la api y mirar si esta en available_countries"""
import json
from pprint import pprint
import requests
#busqueda de artista
buscar=str(input("Nombre artista: "))


response = requests.get("https://deezerdevs-deezer.p.mashape.com/search?q="+buscar,
  headers={
    "X-Mashape-Key": "cDebnrF8yNmshPs5WCu6cIEOimtnp14H3e4jsnZYtQ795tJNZC",
    "Accept": "application/json"
  }
)
data=response.json()


for cancion in data["data"]:
	print(cancion["title"])
	print(cancion["id"])

recoger=int(input("Escribe el id de la canción que quieres comprobar: "))
pais=str(input("Escribe las siglas del pais que quieres comprobar por ejemplo ES : "))

for cancion in data["data"]:
	if recoger == cancion["id"]:
		response = requests.get("https://deezerdevs-deezer.p.mashape.com/track/"+str(recoger),
  headers={
    "X-Mashape-Key": "cDebnrF8yNmshPs5WCu6cIEOimtnp14H3e4jsnZYtQ795tJNZC",
    "Accept": "application/json"
  }
)
data=response.json()

Disponible=False
for datos in data["available_countries"]:
	if datos == pais:
		Disponible=True
	else:
		print("No disponible en tu país")
	