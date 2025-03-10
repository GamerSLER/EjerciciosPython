import array_ayudita

tabla = []

for i in range(10):
    tabla.append([])
    for j in range(10):
        if i % 2 == 0:
            tabla[i].append(1)
        else:
            tabla[i].append(0)

array_ayudita.print2DArray(tabla)