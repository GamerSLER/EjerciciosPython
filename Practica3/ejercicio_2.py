import array_ayudita

diagonal = []

for i in range(5):
    diagonal.append([])
    for j in range(5):
        if i == j:
            diagonal[i].append(1)
        else:
            diagonal[i].append(0)

array_ayudita.print2DArray(diagonal)