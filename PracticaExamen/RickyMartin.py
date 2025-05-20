#1 - 126
import requests

num = int(input("Introduce un número entre 1 y 126: "))
url = "https://rickandmortyapi.com/api/location/"+num.__str__()
contenido = requests.get(url)
ubicacion = contenido.json()
nombre = ubicacion["name"]
tipo = ubicacion["type"]
residentes = ubicacion["residents"]

print(f"En " + nombre + " de tipo " + tipo + " viven: ")

for i in range(len(residentes)):
    url = residentes[i]
    contenido = requests.get(url).json()
    nombre = contenido["name"]
    print(nombre)