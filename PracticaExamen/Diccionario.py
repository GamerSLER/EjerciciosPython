Personas = [
    {
        "nombre": "Alex",
        "edad": 19
    },
    {
        "nombre": "Stephano",
        "edad": 18
    },
    {
        "nombre": "Fabio",
        "edad": 19
    },
    {
        "nombre": "Rafael",
        "edad": 21
    }
]

for persona in Personas:
    for clave, valor in persona.items():
        print(f"{clave}: {valor}")