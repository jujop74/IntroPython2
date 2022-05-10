def crear_lista(n):
  lista = []
  for i in range(n):
    lista.append(i)
  return lista

print(crear_lista(5))


def hola(lista):
  for nombre in lista:
    print('Buen día', nombre)

hola(['María', 'Juan', 'Marta'])
