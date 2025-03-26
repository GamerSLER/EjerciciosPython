receta = {
    "recetas": [
        {
            "nombreReceta": "Lentejas con verduras",
            "tiempo": 80,
            "dificultad": "media",
            "ingredientes": [
                "lentejas",
                "patatas",
                "zanahoria",
                "seitán",
                "cebolla",
                "ajo",
                "tomate"
            ]
        },
        {
            "nombreReceta": "Sopa castellana",
            "tiempo": 20,
            "dificultad": "fácil",
            "ingredientes": [
                "pan",
                "aceite",
                "pimenton",
                "ajo"
            ]
        }
    ],
    "disponibilidad": True,
    "diaSemana": "Lunes"
}

"""print(receta["nombreReceta"])
cuantoTiempo = int(input("Dime los minutos que tienes para hacer la receta: "))

def tieneIngrediente(ingrediente, ingredientes):
    return ingrediente in ingredientes

if cuantoTiempo >= receta["tiempo"]:
    print(f"Claro, te va a llevar {receta["tiempo"]}. Haz {receta["nombreReceta"]}.")
    if tieneIngrediente(input("¿Qué no te gusta? --> "), receta["ingredientes"]):
        print("No te va a gustar...")
else:
    print("No te alcanza el tiempo.")"""

"""if cuantoTiempo >= receta["tiempo"]:
    print(f"Claro, te va a llevar {receta["tiempo"]}. Haz {receta["nombreReceta"]}.")
    for ingrediente in receta["ingredientes"]:
        print(ingrediente)
else:
    print("No te alcanza el tiempo.")
"""