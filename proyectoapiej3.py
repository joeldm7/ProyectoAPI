import json
from pprint import pprint
import requests
#busqueda de artista y duracion de sus canciones (mayor)
buscar=str(input("Nombre artista: "))
duracion=int(input("Introduce la duración: "))


response = requests.get("https://deezerdevs-deezer.p.mashape.com/search?q="+buscar,
  headers={
    "X-Mashape-Key": "cDebnrF8yNmshPs5WCu6cIEOimtnp14H3e4jsnZYtQ795tJNZC",
    "Accept": "application/json"
  }
)
data=response.json()


for cancion in data["data"]:
	if cancion["duration"] > duracion:
		print(cancion["title"])