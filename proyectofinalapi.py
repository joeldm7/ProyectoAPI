from colorama import init, Fore, Back, Style #Importamos la libreria de colorama
init(autoreset=True) #Necesitamos este init con el autoreset para que examine una por una las lineas de colorama
import json # importamos json
from pprint import pprint #Importamos el pretty print
import requests #Importamos request
opcionMenu=0 #Inicializamos la variable opcionMenu a 0
def menu(opcionMenu): #Funcion menu para mostrar las opciones que tiene la API en nuestro fichero python
	print (Fore.GREEN + Style.BRIGHT +("MENÚ OPCIONES API DEEZER"))
	print (Fore.CYAN + Style.BRIGHT +("1. Buscar Artista y te muestro sus canciones"))
	print (Fore.CYAN + Style.BRIGHT +("2. Buscar Canción y te muestro sus autores"))
	print (Fore.CYAN + Style.BRIGHT +("3. Duración Máxima de las canciones de un Artista"))
	print (Fore.CYAN + Style.BRIGHT +("4. Buscar si una canción esta disponible en tu país"))
	print (Fore.CYAN + Style.BRIGHT +("5. Salir"))
	opcionMenu = input(Fore.RED + Style.BRIGHT +"Selecciona una opción  del menú: ") #Seleccionamos el número y lo asignamos a la variable opción

	return opcionMenu #retornamos el resultado de la opción para trabajar con ella en el bucle while

def artista (buscar): # Funcion artista que busca dentro de la API los artistas que queramos buscar
#busqueda de artista
	
	response = requests.get("https://deezerdevs-deezer.p.mashape.com/search?q="+buscar, #Llamada a la API con la variable buscar
  	headers={
    	"X-Mashape-Key": "cDebnrF8yNmshPs5WCu6cIEOimtnp14H3e4jsnZYtQ795tJNZC",
    	"Accept": "application/json"
  	}
	)
	data=response.json()


	for cancion in data["data"]:
			print(Fore.CYAN + Style.BRIGHT +(cancion["title"])) #Bucle que imprime los nombres de las canciones del artista que hemos buscado



def cancion (song): #Funcion cancion que busca dentro de la API las canciones que queramos buscar

	response = requests.get("https://deezerdevs-deezer.p.mashape.com/search?q="+song, #Llamada a la API con la variable song
  	headers={
    	"X-Mashape-Key": "cDebnrF8yNmshPs5WCu6cIEOimtnp14H3e4jsnZYtQ795tJNZC",
    	"Accept": "application/json"
  	}
	)
	data=response.json()


	for cancion in data["data"]:
		print (Fore.CYAN + Style.BRIGHT +(cancion['artist']['name'])) #Bucle que imprime los nombres de los artistas que interpretan esa canción




def duracion (): #Funcion duracion que busca dentro de la API en función de el artista y la duración que le damos previamente y nos muestra el titulo de las canciones que entran dentro de los parámetros.
	#busqueda de artista y duracion de sus canciones (mayor)
	buscar=str(input(Fore.RED + Style.BRIGHT +("Nombre artista: "))) #Busqueda de artista
	duracion=int(input(Fore.RED + Style.BRIGHT +("Introduce la duración: "))) #Busqueda de la duracion


	response = requests.get("https://deezerdevs-deezer.p.mashape.com/search?q="+buscar, #Llamada a la API con la variable buscar
  	headers={
    	"X-Mashape-Key": "cDebnrF8yNmshPs5WCu6cIEOimtnp14H3e4jsnZYtQ795tJNZC",
    	"Accept": "application/json"
  	}
	)
	data=response.json()


	for cancion in data["data"]:
		if cancion["duration"] > duracion:
			print(Fore.CYAN + Style.BRIGHT +(cancion["title"])) #Bucle que compara la duracion que hemos dado con el campo duration de la api y si es mayor imprime el titulo de la canción.



def paises (apto): #Función paises que a partir del nombre de un artista muestra sus canciones con sus respectivos ids y cuando seleccionamos el id que queremos nos pide un pais si esta cancion esta disponible en ese pais te lo indica y sino también.
	
	response = requests.get("https://deezerdevs-deezer.p.mashape.com/search?q="+apto, #Llamada de la API con la variable apto(Nombre Artista)
  	headers={
    	"X-Mashape-Key": "cDebnrF8yNmshPs5WCu6cIEOimtnp14H3e4jsnZYtQ795tJNZC",
    	"Accept": "application/json"
  	}
	)
	data=response.json()


	for cancion in data["data"]:
		print(Fore.CYAN + Style.BRIGHT +(cancion["title"]))
		print(Fore.CYAN + Style.BRIGHT +(str(cancion["id"]))) #Bucle que que imprime el titulo de la cancion y su id del artista previamente introducido

	recoger=int(input(Fore.RED + Style.BRIGHT +("Escribe el id de la canción que quieres comprobar: "))) #Selección del ID
	pais=str(input(Fore.RED + Style.BRIGHT +("Escribe las siglas del pais que quieres comprobar por ejemplo ES : "))) #Selección del pais

	for cancion in data["data"]:
		if recoger == cancion["id"]:
			response = requests.get("https://deezerdevs-deezer.p.mashape.com/track/"+str(recoger), #Bucle que compara el id que hemos recogido con el id de las canciones de la API si coincide con alguna llama a la API de nuevo con la variable recoger
  	headers={
    	"X-Mashape-Key": "cDebnrF8yNmshPs5WCu6cIEOimtnp14H3e4jsnZYtQ795tJNZC",
    	"Accept": "application/json"
  	}
	)
	data=response.json()

	Disponible=False #Igualamos la variable Disponible para usarla dentro del if
	for datos in data["available_countries"]: #bucle que compara si los datos de available_countries dentro del id de la canción que hemos introducido previamente es igual al pais que hemos introducido, en caso de que sea igual cambia la variable Disponible a True y para el bucle
		if datos == pais:
			Disponible=True
			break
	if Disponible==True: #Si el pais ha coincidido con algún pais de la canción y ha cambiado el valor de la variable Disponible a True entonces imprime el mensaje de Disponible sino muestra que no esta Disponible
		print(Fore.RED + Style.BRIGHT +("====================="))
		print("Disponible en tu pais")
		print(Fore.RED + Style.BRIGHT +("====================="))

	else:
		print(Fore.RED + Style.BRIGHT +("========================"))
		print("No disponible en tu pais")
		print(Fore.RED + Style.BRIGHT +("========================"))



while True:
	# Mostramos el menu sin parar para que el usuario siempre pueda ver las opciones a elegir
	opcionMenu=menu(opcionMenu)
	# solicitamos una opción al usuario
	if opcionMenu=="1": #Condición de la primera opción
		buscar=str(input(Fore.RED + Style.BRIGHT +"Nombre artista: "))
		artista(buscar) #Llamada a la función artista
	elif opcionMenu=="2":#Condición de la segunda opción
		song=str(input(Fore.RED + Style.BRIGHT +"Escribe que cancion quieres buscar y que artistas la interpretan: "))
		cancion(song) #Llamada a la función cancion
	elif opcionMenu=="3":#Condición de la tercera opción
		duracion() #Llamada a la función duracion
	elif opcionMenu=="4":#Condición de la cuarta opción
		apto=str(input(Fore.RED + Style.BRIGHT +("Nombre artista: ")))
		paises(apto)#Llamada a la función paises
	elif opcionMenu=="5":#Condición de la quinta opción
		print(Fore.GREEN + Style.BRIGHT +("Saliendo del Programa..."))
		break #Salimos del programa
	else:
		input(Fore.GREEN + Style.BRIGHT +"No has pulsado ninguna opción correcta...\nPulsa cualquier tecla para continuar") #En caso de no introducir una opción disponible nos muestra un error y vuelve al bucle.
