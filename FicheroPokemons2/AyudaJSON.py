import json
def guardarJSON(datos, nombre):
    with open(nombre, "w") as fichero:
        json.dump(datos, fichero, indent=4)

def cargarJSON(nombre):
    try:
        with open(nombre, "r") as fichero:
            return json.load(fichero)
    except FileNotFoundError:
        return {}