# w --> write --> sobreescribir
# a --> append --> añadir
# r --> read --> leer

"""gestionFicheros = open("lista.txt", "a")
gestionFicheros.write("Informacion.")"""

"""lector = open("lista.txt", "r")
info = lector.read()
print(info)
info = lector.readline()
print(info)
info = lector.readlines()
print(info)"""

"""import os
if os.path.exists("nuevo.txt"):
    print("Existe")
else:
    gestorFicheros = open("nuevo.txt", "x")

try:
    gestorFicheros = open("nuevo.txt", "x")
except FileExistsError:
    print("Ese fichero ya existe.")"""