from AyudaJSON import cargarJSON, guardarJSON
import random as r
pokemon = {}
pokemon["numPokedex"] = 0
pokemon["nombre"] = "XXX"
pokemon["tipo"] = ["XXX", "XXX"]
pokemon["IV"] = {"ps": 0, "velocidad": 0, "ataque": 0, "defensa": 0, "ataqueEspecial": 0, "defensaEspecial": 0}
"""pokemon["stats"]["velocidad"] = 3"""
"""ataque1 = {
    "nombreAtaque": "XXX",
    "tipo": "XXX"
}"""
"""pokemon["ataques"] = [ataque1]"""
"""print(pokemon)
print(pokemon["stats"]["objetos"][1])
"""
cont = True
pokedex = cargarJSON("pokedex.json")
while(cont):
    pokemon={}
    nombrePoke = input("Introduce el nombre del pokémon: ")
    pokemon["nombre"]=nombrePoke
    cantTiposPoke = int(input("¿Tu pokémon tiene 1 o 2 tipos? --> "))
    if cantTiposPoke == 1:
        tipoPoke1 = input("Introduce el tipo de tu pokemon: ")
        pokemon["tipo"] = tipoPoke1
    elif cantTiposPoke == 2:
        tipoPokes = input("Introduce los tipos de tu pokémon: ").split(",")
        pokemon["tipo"] = tipoPokes
    else:
        print("Error, solo puedes introducir como máximo dos tipos")

    numPoke = input("Introduce su número de pokedex: ")
    pokemon["numPokedex"]=numPoke

    try:
        pokemon["IV"]["ps"] = r.randint(0, 31)
        pokemon["IV"]["velocidad"] = r.randint(0, 31)
        pokemon["IV"]["ataque"] = r.randint(0, 31)
        pokemon["IV"]["defensa"] = r.randint(0, 31)
        pokemon["IV"]["ataqueEspecial"] = r.randint(0, 31)
        pokemon["IV"]["defensaEspecial"] = r.randint(0, 31)
    except KeyError:
        pokedex["IV"] = {}
        pokemon["IV"]["ps"] = r.randint(0, 31)
        pokemon["IV"]["velocidad"] = r.randint(0, 31)
        pokemon["IV"]["ataque"] = r.randint(0, 31)
        pokemon["IV"]["defensa"] = r.randint(0, 31)
        pokemon["IV"]["ataqueEspecial"] = r.randint(0, 31)
        pokemon["IV"]["defensaEspecial"] = r.randint(0, 31)

    print(pokemon)
    guardarJSON(pokemon, "pokedex.json")
    intpoke = input("¿Quieres introducir un pokemón?(s/n) --> ")
    if intpoke.lower() != "s":
        cont = False
    elif intpoke.lower() != "n":
        print("Has introducido un dato erróneo.")
#Se debe de crear un diccionario de IV porque lo detecta como keyError



#Mal hecho y no terminado

"""
numPokedex int
nombre (str)
tipo = [str, str]
género = str
stats = {
    ps: int
    velocidad: int
    ataque: int
    defensa: int
    ataqueEspecial: int
    defensaEspecial: int
}
ataques = [
    {
    nombreAtaque: str
    tipo: str,
    daño: int
    esFisico: boolean,
    pp: int
    },
    ... (1 al 4)
]
"""