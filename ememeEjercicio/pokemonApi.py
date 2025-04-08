import json
from random import randint
import requests

url = "https://pokeapi.co/api/v2/pokemon/" + randint(0, 1302).__str__()
contenido = requests.get(url)
pokemon = contenido.json()
nombre = pokemon["name"].lower()
peso= pokemon["weight"]
altura = pokemon["height"]
entrada = pokemon["id"]

print(nombre)
def conseguirDescripcion():
    descripciones = []
    especie = requests.get(pokemon["species"]["url"]).json()
    for i in range(len(especie["flavor_text_entries"])):
        if especie["flavor_text_entries"][i]["language"]["name"] == "en":
            descripciones.append(especie["flavor_text_entries"][i]["flavor_text"])
    return descripciones

def conseguirTipos():
    tipos = []
    for i in range(len(pokemon["types"])):
        tipos.append(pokemon["types"][i]["type"]["name"])
    return tipos

def aparicionesJuegos():
    apariciones = []
    for i in range (len(pokemon["game_indices"])):
        apariciones.append(pokemon["game_indices"][i]["version"]["name"])
    return apariciones

def conseguirHabilidades():
    habilidades = []
    for i in range (len(pokemon["abilities"])):
        habilidades.append(pokemon["abilities"][i]["ability"]["name"])
    return habilidades

def conseguirUbicaciones():
    ubicaciones = []
    contenido = requests.get(pokemon["location_area_encounters"])
    ubicacion = contenido.json()
    for i in range(len(ubicacion)):
        ubicaciones.append(ubicacion[i]["location_area"]["name"])
    return ubicaciones

def pistaLongitud(nombre):
    separado = nombre.split(" ")
    longitud = 0
    for i in range(len(separado)):
        longitud += len(separado[i])
    return longitud

print(f"Adivina el pokemon sabiendo la siguiente información.\nSu nombre tiene {pistaLongitud(nombre)} letras")
incorrecto = True
for i in range(8):
    if incorrecto:
        if input(f"Intento {i + 1} ").lower() == nombre:
            print("Enhorabuena")
            incorrecto = False
        else:
            if i+1 == 1:
                if conseguirUbicaciones() == []:
                    print("No se encuentra salvaje, o es una evolución.")
                else:
                    print(f"Se puede encontrar salvaje en las siguientes ubicaciones: {conseguirUbicaciones()}")
            elif i+1 == 2:
                print(f"El pokemon mide {altura/10} metros y pesa {peso/10} kilos.")
            elif i+1 == 3:
                if aparicionesJuegos() == []:
                    print("El pokemon es posterior a la quinta generación.")
                else:
                    print(f"Aparece en estas generaciones: {aparicionesJuegos()}")
            elif i+1 == 4:
                print(f"Su entrada en la pokedex es: {entrada}")
            elif i+1 == 5:
                print(f"Tiene las habilidades: {conseguirHabilidades()}")
            elif i+1 == 6:
                print(f"Es de tipo/s: {conseguirTipos()}")
            elif i+1 == 7:
                print(f"Una de sus descripciones en la pokedex es: {conseguirDescripcion()[randint(0, len(conseguirDescripcion()))]}")
            else:
                print(f"Se te acabaron los intentos. El personaje era: {nombre}")
                incorrecto = True