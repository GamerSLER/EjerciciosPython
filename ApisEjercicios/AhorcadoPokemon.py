import requests
def nombrePokemon():
    url = "https://pokeapi.co/api/v2/pokemon-species?offset=0&limit=1025"
    contenido = requests.get(url)
    dato = contenido.json()
    nombre = dato[1]["name"]

print(nombrePokemon())