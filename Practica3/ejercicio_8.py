from random import randint
import array_ayudita

matriz = []

suma = randint(0,10)
for fila in range(10):
    matriz.append([])
    matriz[fila].append(suma)
    suma = 0
    for columna in range(14):
        matriz[fila].append(randint(0, 10))
        #matriz[fila].append(int(input("Introduce número ")))
    suma = sum(matriz[fila])

array_ayudita.print2DArray(matriz)