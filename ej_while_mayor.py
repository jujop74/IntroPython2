numero_mayor = -9999999999

numero = int(input('Introduce un número entero o escribe 0 para detener: '))

while numero != 0:
  if numero > numero_mayor:
    numero_mayor = numero
  numero = int (input('Introduce un número entero o escribe 0 para detener: '))

print(f'El número mayor es: {numero_mayor}')