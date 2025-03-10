import array_ayudita
matriz = [
    [3, 2, 5, 0, 9],
    [0, 10, 2, 3, 1],
    [-3, 2, 3, 43, 1]
]
matrizGirada = []

for i in range (len(matriz[0])):
    matrizGirada.append([])
    for j in range (len(matriz)):
        matrizGirada[i].append(matriz[j][i])

array_ayudita.print2DArray(matrizGirada)