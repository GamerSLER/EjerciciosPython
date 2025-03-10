import math
import array_ayudita
from random import randint

matriz = []
fin = True
fila = 0
while fila < 20 and fin:
    columna = 0
    matriz.append([])
    exponente = randint(1, 20)
    #exponente = int(input("Introduzca exponente: "))
    while columna < 2 and fin:
        if exponente != -1000 and columna == 0:
            matriz[fila].append(exponente)
        elif exponente != -1000 and columna != 0:
            matriz[fila].append((math.pow(2, exponente)))
        else:
            fin = False
        columna += 1
    fila += 1
array_ayudita.print2DArray(matriz)