from array_ayudita import print2DArray

array = []

for fila in range(10):
    array.append([])
    for columna in range(10):
        if fila == columna:
            array[fila].append(1)
        else:
            array[fila].append(0)

print2DArray(array)