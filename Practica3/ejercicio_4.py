"""from Practica3.array_ayudita import esIdentidad
"""
def esIdentidad():
    identidad = True
    if len(matriz) != len(matriz[0]):
        identidad = False
        return identidad
    else:
        for i in range(len(matriz)):
            for j in range(len(matriz[0])):
                if i == j and matriz[i][j] != 1:
                    return False
                if i != j and matriz[i][j] != 0:
                    identidad = False
                    return False
    return  identidad
matriz = []
Filas = int(input("¿Cuantas filas tendrá la matríz?"))
Columnas = int(input("¿Cuantas columnas tendrá la matríz?"))

for i in range(Filas):
    matriz.append([])
    for j in range(Columnas):
        matriz[i].append(int(input(f"número en posicion {i + 1}, {j + 1}: ")))

print(esIdentidad())