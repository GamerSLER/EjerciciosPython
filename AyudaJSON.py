import json
def guardarJSON(datos, nombre):
    with open(nombre, "w") as fichero:#El with es obligatorio.
        json.dump(datos, fichero, indent=4)#el indent es para darle 4 espacios, la indentación, vaya.

def cargarJSON(nombre):
    try:
        with open(nombre, "r") as fichero:
            return json.load(fichero)
    except FileNotFoundError:
        return {}