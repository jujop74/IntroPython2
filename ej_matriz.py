tablero = []
casilla = 'v'

for i in range(8):
  fila = [casilla for i in range(8)]
  tablero.append(fila)

print(len(tablero))
print(tablero)

print('**********')

# Versión refactorizada
casilla = 'x'
tablero = [[casilla for i in range(8)] for j in range(8)]

print(len(tablero))
print(tablero)
