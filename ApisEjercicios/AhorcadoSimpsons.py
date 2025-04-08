import random

import requests

url = "https://thesimpsonsquoteapi.glitch.me/quotes"
contenido = requests.get(url)
quote = contenido.json()

frase = quote[0]["quote"]
nombrePersonaje = quote[0]["character"]
print(frase)
print(f"{nombrePersonaje}") #No se debería ver esto, pero lo uso para la probar el código

oportunidades = 5
continuar = True

def esconderNombre(nombrePersonaje):
    longitud = len(nombrePersonaje)
    mensajeEscondido = "_"*longitud
    print(mensajeEscondido)
"""    nP = list(nombrePersonaje)
    nombreEscondido = []
    for i in range(longitud):
        nombreEscondido.append("_")
    print(nombreEscondido)"""

def ventaja(nombrePersonaje):
    mensajeEscondido = nombrePersonaje
    random.randint(0, len(nombrePersonaje))
    print(mensajeEscondido)

while (continuar):
    nombre = input("El nombre de el personaje: ")
    if nombre != nombrePersonaje:
        print("Incorrecto")
        oportunidades -= 1
        if oportunidades == 0:
            print(f"Haz perdido, el personaje era {quote[0]["character"]}")
            continuar = False

        print(f"{esconderNombre(nombrePersonaje)}")


    else:
        print("Haz adivinado.")
        continuar = False