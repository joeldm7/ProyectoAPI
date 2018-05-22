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