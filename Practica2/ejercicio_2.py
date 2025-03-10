"""
Máquina dispensadora de bebidas
[  , 0.05!->0] ==  INTRODUZCA IMPORTE EXACTO
"""

nombresProductos = ["Agua 💧", "Refresco 🥤", "Zumo 🍹"]
preciosProductos = [0.50, 0.75, 0.95]
reservaMonedas = [20, 20, 20, 20, 20,20]
valoresMonedas = [2, 1, 0.50, 0.20, 0.10, 0.05]

def imprimirMenu(nombres, precios):
    textoMenu =""
    for i in range(len(nombres)):
        textoMenu += f"{i+1} - {nombres[i]} : {precios[i]} \n"
    textoMenu += f"{len(nombres)+1} - SALIR"
    print(textoMenu)

def ingresarImporte(opcion):
    precio = preciosProductos[opcion]
    importeUsuario = 0
    monedasIntroducidas = []
    while importeUsuario < precio:
        print(f"Le queda {round(precio-importeUsuario, 2)} por ingresar.")
        moneda = ingresarMoneda()
        importeUsuario += moneda
        monedasIntroducidas.append(moneda)
    if importeUsuario > precio:
        resto = importeUsuario - precio
        darCambio(resto)
    entregarProducto(nombresProductos[opcion])
    sumarMonedas(monedasIntroducidas)

def darCambio(resto):
    vueltas = 0
    monedasDevueltas = []
    while vueltas < resto:
        for valor in valoresMonedas:
            if valor <= resto:
                monedasDevueltas.append(valor)
                vueltas += valor
                if valor == resto:
                    devolverMonedas(monedasDevueltas)
                    print(f"Tus vueltas son estas: {monedasDevueltas}")
                resto -= valor

def devolverMonedas(monedas):
    for moneda in monedas:
        reservaMonedas[valoresMonedas.index(moneda)] -= 1

def sumarMonedas(monedas):
    for moneda in monedas:
        reservaMonedas[valoresMonedas.index(moneda)] += 1

def entregarProducto(producto):
    print(f"Aquí tiene su {producto}")

def ingresarMoneda():
    valoresValidos = []
    for valor in valoresMonedas:
        valoresValidos.append(str(valor))
    moneda = input("Introduzca monedas de 2€, 1€, 0.50cts, 0.20cts, 0.10cts y 0.05cts: ")
    while moneda not in valoresValidos:
        moneda = input("Introduzca una moneda válida: ")
    return float(moneda)

def ingresarOpcion():
    opcion = input("Introduce la opción: ")
    while opcion not in ["1", "2", "3", "4"]:
        opcion = input("Introduzca una opción correcta: ")
    return int(opcion)-1

imprimirMenu(nombresProductos, preciosProductos)
opcion = ingresarOpcion()
ingresarImporte(opcion)

print(reservaMonedas)
print(valoresMonedas)