#archivoLector = open("archivoPrueba", "r")
#archivoCreador = open("archivoPrueba", "x")
#archivoSobreescritor = open("archivoPrueba", "w")
#archivoEscritor = open("archivoPrueba", "a")

try:
    archivoLector = open("archivoPrueba", "r")
    print(archivoLector.read())
except:
    archivoCreador = open("archivoPrueba", "x")

archivoSobreescritor = open("archivoPrueba", "w")
archivoSobreescritor.write("Pe")

archivoEscritor = open("archivoPrueba", "a")
archivoEscritor.write("Causa")