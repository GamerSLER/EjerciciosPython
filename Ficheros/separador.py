f = open("customers-100.csv", "r")
info = f.read().split("\n")
nombre = input("Introduce un nombre: ").lower().capitalize()
for linea in info:
    listaLinea = linea.split(",")
    if nombre in listaLinea:
        print(f"El número de {nombre} es {listaLinea[8]}")