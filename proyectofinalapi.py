from colorama import init, Fore, Back, Style
init(autoreset=True)
import json
from pprint import pprint
import requests
opcionMenu=0
def menu(opcionMenu):
	"""
	Función para limpiar la pantalla y mostrar el menú
	"""
	print (Fore.GREEN + Style.BRIGHT +("MENÚ"))
	print("1. Busca Artista")
	print("2. Canción")
	print("3. Duración Máxima")
	print("4. Paises Aptos")
	print("5. Salir")
	opcionMenu = input("Selecciona una opción: ")

	return opcionMenu

def artista (buscar):
#busqueda de artista
	
	response = requests.get("https://deezerdevs-deezer.p.mashape.com/search?q="+buscar,
  	headers={
    	"X-Mashape-Key": "cDebnrF8yNmshPs5WCu6cIEOimtnp14H3e4jsnZYtQ795tJNZC",
    	"Accept": "application/json"
  	}
	)
	data=response.json()


	for cancion in data["data"]:
			print(cancion["title"])



def cancion (song):

	response = requests.get("https://deezerdevs-deezer.p.mashape.com/search?q="+song,
  	headers={
    	"X-Mashape-Key": "cDebnrF8yNmshPs5WCu6cIEOimtnp14H3e4jsnZYtQ795tJNZC",
    	"Accept": "application/json"
  	}
	)
	data=response.json()


	for cancion in data["data"]:
		print (cancion['artist']['name'])




def duracion ():
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
			print(cancion["duration"])



def paises (apto):
#busqueda de artista
	
	response = requests.get("https://deezerdevs-deezer.p.mashape.com/search?q="+apto,
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
			break
	if Disponible==True:
		print("Disponible en tu pais")
	else:
		print("No disponible en tu pais")



while True:
	# Mostramos el menu
	opcionMenu=menu(opcionMenu)
	print(opcionMenu)
	# solicituamos una opción al usuario
	if opcionMenu=="1":
		buscar=str(input("Nombre artista: "))
		artista(buscar)
	elif opcionMenu=="2":
		song=str(input("Nombre cancion a buscar: "))
		cancion(song)
	elif opcionMenu=="3":
		duracion()
	elif opcionMenu=="4":
		apto=str(input("Nombre artista: "))
		paises(apto)
	elif opcionMenu=="5":
		print("Saliendo del Programa...")
		break
	else:
		input("No has pulsado ninguna opción correcta...\npulsa una tecla para continuar")
