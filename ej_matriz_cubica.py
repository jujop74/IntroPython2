cubo = [[['Hola', 'x', 'x'],
         ['z', 'x', 'x'],
         ['y', 'x', 'x']],

        [['w', 'x', 'x'],
         ['z', 'x', 'x'],
         ['y', 'x', 'x']],

        [['z', 'x', 'x'],
         ['y', 'x', 'x'],
         ['Adiós', 'x', 'x']]]

print(cubo)
print(cubo[0][0][0])
print(cubo[2][2][0])

# Impresión por 'filas' del array
for i in range(len(cubo)):
  print(cubo[i])
