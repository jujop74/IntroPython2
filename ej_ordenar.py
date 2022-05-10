# Método 'manual' para ordernar las listas
lista = [72, 100, 51, 13, 40]

intercambio = True

while intercambio:
  intercambio = False
  for i in range(len(lista) - 1):
    if lista[i] > lista[i + 1]:
      intercambio = True
      lista[i], lista[i + 1] = lista[i + 1], lista[i]

print(lista)


# Método sort() para ordernar las listas
lista = [72, 100, 51, 13, 40]
lista.sort()
print(lista)


# Método reverse() para ordernar las listas en orden inverso
# Parece que funciona mal la función de Python...
lista = [72, 100, 51, 13, 40]
lista.reverse()
print(lista)
