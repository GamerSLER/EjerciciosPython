import random as r
from FicheroPokemon3.AyudaJSON import cargarJSON, guardarJSON

pokedex = cargarJSON("pokedex.json")

def darInfo(pokemon):
    info = ["Nombre"]
    pokemon["info"] = input("Introduce el nombre del pokemon: ")

def darTipo(pokemon):
    tipo =  ["Tipo"]
    tipos = int(input("¿Cuantos tipos tiene tu pokemon?(max. 2) --> "))
    if tipos == 1:
        pokemon["Tipo"] = input("Introduce el tipo: ")
    elif tipos == 2:
        pokemon["Tipo"] = input("Introduce los tipos: ").split(",")

def darIV(pokemon):
    IVs = ["ps", "velocidad", "ataque", "defensa", "ataqueEspecial", "defensaEspecial"]
    pokemon["ps"] = r.randint(0, 31)
    pokemon["velocidad"] = r.randint(0, 31)
    pokemon["ataque"] = r.randint(0, 31)
    pokemon["defensa"] = r.randint(0, 31)
    pokemon["ataqueEspecial"] = r.randint(0, 31)
    pokemon["defensaEspecial"] = r.randint(0, 31)

def darNumPokedex(pokemon):
    nPokedex = ["numPokedex"]
    pokemon["numPokedex"] = int(input("Introduce el número de pokedex de tu pokémmon: "))

continuar = True
try:
    pokemons = pokedex["pokemons"]
except KeyError:
    pokedex["pokemons"] = []
    pokemons = pokedex["pokemons"]

while continuar:
    pokemon = {}
    darInfo(pokemon)
    darTipo(pokemon)
    darIV(pokemon)
    darNumPokedex(pokemon)
    pokemons.append(pokemon)
    if input("¿Continuar? s/n").lower() != "s":
        continuar = False

pokedex["pokemons"] = pokemons
guardarJSON(pokedex, "pokedex.json")














