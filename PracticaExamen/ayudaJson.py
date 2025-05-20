import json

def guardarJson(datos, archivo):
    with open(archivo, "w") as fichero:
        json.dump(datos, fichero, indent = 4)

def cargarJson(archivo):
    try:
        with open(archivo, "r") as fichero:
            return json.load(fichero)
    except FileNotFoundError:
        return []

#RECETA de los cojones
recetasAPI = cargarJson("Recetas.txt")
nombreReceta = input("Introduce el nombre de la receta: ")
cantIngredientes = int(input("Cuantos ingredientes usarás: "))
Ingredientes = []
for i in range(cantIngredientes):
    nombreIngrediente = input("Ingrediente: ")
    cantIngrediente = int(input("Cantidad: "))
    Ingredientes.append({"Nombre": nombreIngrediente, "Cantidad":cantIngrediente})

recetasAPI.append({"Receta":nombreReceta, "Cantidad":cantIngredientes, "Ingredientes":Ingredientes})
guardarJson(recetasAPI, "Recetas.txt")
