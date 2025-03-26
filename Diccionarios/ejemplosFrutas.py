"""frutas = {
  "platano": 1.40,
  "naranja": 2,
  "tomate": 1.65,
  "piña": 2.30
}"""
"""print(frutas)
frutaNueva = input("Mete una fruta nueva: ")
precioFrutaNueva = float(input("Mete su precio: "))
frutas[frutaNueva] = precioFrutaNueva
print(frutas)"""




"""
def estaFruta(fruta):
    try:
        frutas[fruta]
        return True 
    except:
        return False
 """
"""def estaFruta(fruta):
    return fruta in frutas

print("================ FRUTAS ================")
print(f"Tenemos estas frutas: {frutas}")
fruta = input("Introduce una fruta: ")
if estaFruta(fruta):
    peso = float(input("¿Cuanto pesa la fruta? --> "))
    print(f"Te va a costar {frutas[fruta]*peso}€")
else:
    print("La fruta no está en la lista.")"""

"""
continuar = True
while(continuar):
    print(f"¿Qué frutas quieres comprar? \n{frutas}")
    fruta = input("Introduce fruta: ")
    if fruta in frutas:
        peso = int(input("¿Cuantos kilos quieres comprar? --> "))

    else:
        print("Hay un error, intenta insertar una fruta de la lista")
 """