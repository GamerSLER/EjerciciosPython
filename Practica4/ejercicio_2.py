import random as r
from array_ayudita import print2DArray

matriz = []

for fila in range(0, 3):
    matriz.append([])
    for columna in range(0, 4):
        matriz[fila].append(r.randint(1, 9))
"""        numeros = int(input("Introduce numeros: "))
        matriz[fila].append(numeros)"""

sumaVector = []
for fila in range(0,3):
    suma = 0
    for columna in range(0,4):
        suma += matriz[fila][columna]
    sumaVector.append(suma)

print2DArray(matriz)
print("---------------------------------------------------------")
print("")
print(f"En la fila {sumaVector.index(max(sumaVector)) + 1} ({matriz[sumaVector.index(max(sumaVector))]})\nEl resultado es {max(sumaVector)}")
"""print(sumaVector.index(max(sumaVector)))
print("")
print(sumaVector)
print("")
print(matriz[sumaVector.index(max(sumaVector))])"""