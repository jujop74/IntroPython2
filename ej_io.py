# No es necesario la importación de la librería
# import io


# Lectura del fichero copmleto
# fichero = open('quijote_pg2000.txt', 'r')

# for linea in fichero:
#     print(linea)

# fichero.close()


# Lectura de los primeros 200 caracteres
# with open('quijote_pg2000.txt', 'r') as fichero:
#     contenido = fichero.read(200)
#     print(contenido)

# fichero.close()


# Lee la primera línea del fichero
# with open('quijote_pg2000.txt', 'r') as fichero:
#     contenido = fichero.readline()
#     print(contenido)

# fichero.close()


# Lee la primera línea del fichero
# with open('quijote_pg2000.txt', 'r') as fichero:
#     contenido = fichero.readlines(2000)
#     for c in contenido:
#         print(c)

# fichero.close()


# Para crear un nuevo fichero
# entrada = '** Primera parte del ingenioso hidalgo don Quijote de la Mancha'
# with open('quijote_ext01.txt', 'x') as fichero:
#     fichero.write(entrada)

# fichero.close()


# Busca a partir del carácter 18 e imprime los 42 caracteres siguientes
with open('quijote_ext01.txt', 'r') as fichero:
    fichero.seek(18)
    contenido = fichero.read(42)
    print(contenido)

fichero.close()
