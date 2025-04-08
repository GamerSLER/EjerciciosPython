import random
import requests

url = "https://rickandmortyapi.com/api/character/"
personajeAleatorio = random.randint(1, 826)
webContent = requests.get(f"{url}{personajeAleatorio}")
personaje = webContent.json()

claves = personaje.keys()
valores = personaje.values()

for c,v in personaje.items():
    print(f"{c}: {v}")