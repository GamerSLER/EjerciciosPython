from random import random, randint

import requests
url = "https://pokeapi.co/api/v2/pokemon/" + randint(0, 1302).__str__()
contenido = requests.get(url)
pokemon = contenido.json()
nombre = pokemon["name"]

print(nombre)

def habilidadSecreta():
    habilidades = []
    habilidadesEscondidas = []
    for i in range(len(pokemon["abilities"])):
        if pokemon["abilities"][i]["is_hidden"] == True:
            habilidades.append(pokemon["abilities"][i]["ability"]["name"])
    return habilidades, habilidadesEscondidas


habilidades, habilidadesEscondidas = habilidadSecreta()
print(habilidades)
print(habilidadesEscondidas)