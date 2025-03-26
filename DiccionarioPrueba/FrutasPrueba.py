"""
ANADIR a un archivo json frutitas
frutas nuevas con sus precios.
"""
from AyudaJSON import guardarJSON, cargarJSON
continuar = True
while(continuar):
    frutitas = cargarJSON("frutitas.json")
    fruta = input("Introduce una fruta: ")
    precio = float(input("Introduce un precio: "))
    frutitas[fruta] = precio
    guardarJSON(frutitas, "frutitas.json")
    frutitas = cargarJSON("frutitas.json")
    print(frutitas)
    rpta = input("¿Quieres introducir otra fruta?(s/n) --> ")
    if rpta.lower() == "n":
        print("Hasta luego.")
        continuar = False