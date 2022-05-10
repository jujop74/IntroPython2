# Se obtienen dos números
numero_1 = int(input('Ingresa un número: '))
numero_2 = int(input('Ingresa el segundo número: '))

if numero_1 == numero_2:
  print('Los números tienen idéntico valor')
elif numero_1 > numero_2:
  numero_mayor = numero_1
  print('El número mayor es:', numero_mayor)
else:
  numero_mayor = numero_2
  print('El número mayor es:', numero_mayor)
