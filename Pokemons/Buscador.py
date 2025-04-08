import requests
def conseguirPokemons():
    url = "https://pokeapi.co/api/v2/pokemon-species?offset=0&limit=1025"
    try:
        response = requests.get(url)
        if response.status_code == 200:
            llamada = response.json()
            return llamada
        else:
            print("Error")
    except:
        print("NADA")

objeto = conseguirPokemons()
pokedex = objeto["results"]
for pokemon in pokedex:
    print(pokemon["name"])