import array_ayudita

matriz = []
suma_total = 0

for fila in range(4):
    matriz.append([])
    if fila == 0:
        matriz[fila].append(" ")
    else:
        matriz[fila].append(input("Nombre de la asignatura"))
    for columna in range(15):
        if fila == 0:
            matriz[fila].append(input(f"Nombre del estudiante {columna + 1}"))
        else:
            matriz[fila].append(int(input(f"Nota de {matriz[0][columna + 1]} en {matriz[fila][0]}")))
array_ayudita.print2DArray(matriz)

for i in range(1, len(matriz[0])):
    suma_columna = 0
    for j in range (1, len(matriz)):
        suma_columna += matriz[j][i]
    media_columna = suma_columna / (len(matriz) - 1)
    print(f"Media general de {matriz[0][i]}: {media_columna}")


for i in range(1, len(matriz)):
    suma_fila = 0
    for j in range(1, len(matriz[i])):
        suma_fila += matriz[i][j]
    suma_total += suma_fila
    print(f"Nota media de {matriz[i][0]}: {suma_fila / len(matriz[i]) - 1}")
print(f"Media total es {suma_total / ((len(matriz) - 1) * (len(matriz[0]) - 1))}")