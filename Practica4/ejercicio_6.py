from array_ayudita import print2DArray

Inventario = []
m = 3
n = 2
suma = 0

for i in range(n):
    Inventario.append([])
    for j in range(m):
        Inventario[i].append(int(input("Introduce el valor de las piezas: ")))

def sumaGeneral(suma):
    for i in range(n):
        for j in range(m):
            suma += Inventario[i][j]
    return suma

def sumaPiezaXTotalAlmacen():
    num_filas = len(Inventario)
    num_columnas = len(Inventario[0])
    for i in range(n):
        suma = 0
        for j in range(num_filas):
            suma += Inventario[i][j]
        print(f"La suma de las piezas {j + 1} en todos los almacenes es: {suma}")

def totalPiezasXAlmacen():
    for i in range(n):
        for j in range(m):
            print(f"Almacén {i + 1} piezas {j + 1} tiene: {Inventario[i][j]} piezas")

def sumaTotalXAlmacen():
    for i in range(n):
        for j in range(m):
            print(f"La suma de piezas del Almacén {i + 1} es: {sum(Inventario[i])}")

print2DArray(Inventario)
print(f"Valor total: {sumaGeneral(suma)}")
sumaTotalXAlmacen()
totalPiezasXAlmacen()
sumaPiezaXTotalAlmacen()