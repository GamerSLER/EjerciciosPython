"""
nombre (str)
tipo = [str, str]
género = str
stats = {
    vida: int
    velocidad: int
    ataque: int
    ataqueEspecial: int
    defensa: int
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
import json

def guardarJSON(datos, nombre):
    with open(nombre, "w") as fichero:
        json.dump(datos, fichero, indent=4)

def cargarJSON(nombre):
    try:
        with open(nombre, "r") as fichero:
            return json.load()
    except FileNotFoundError:
        return {}


tios = cargarJSON("tios.json")
print(tios)
tios["josué"] = "buen chaval"
tios["rafa"] = "gracioso"
print(tios)
guardarJSON(tios, "tios.json") 