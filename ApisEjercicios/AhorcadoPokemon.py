import os
from platform import system
from random import randint
import requests

try:
    url = "https://pokeapi.co/api/v2/pokemon/" + randint(0, 1302).__str__()
    contenido = requests.get(url)
    pokemon = contenido.json()
    nombre = pokemon["name"]

    def habilidadSecreta():
        habilidades = []
        habilidadesEscondidas = []
        for i in range(len(pokemon["abilities"])):
            if pokemon["abilities"][i]["is_hidden"] == True:
                habilidades.append(pokemon["abilities"][i]["ability"]["name"])
        return habilidades, habilidadesEscondidas

    def tipoPokemon():
        tipos = []
        for i in range(len(pokemon["types"])):
            tipos.append(pokemon["types"][i]["type"]["name"])
        return tipos

    habilidades, habilidadesEscondidas = habilidadSecreta()

    print(nombre)
    print(habilidades)
    print(habilidadesEscondidas)
    print(tipoPokemon())
except:
    print("ERROR")