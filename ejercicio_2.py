# Preguntar al usuario un número y mostrar si es par o impar.
# Si el número es múltiplo de 4 imprimir el mensaje apropiado al usuario

def funcion_numero():
  numero = int(input('Introduzca número: '))
  return numero

numero = funcion_numero()
print('')

# if numero%2 == 0:
#   print('El número es par')
# else:
#   print('El número es impar')

# if numero%4 == 0:
#   print('El número es múltiplo de 4')
# else:
#   print('El número no es múltiplo de 4')

if numero % 4 == 0:
  print(numero, 'es múltiplo de 4 y es par')
elif numero % 2 == 0:
  print(numero, 'es par')
else:
  print(numero, 'es impar')
