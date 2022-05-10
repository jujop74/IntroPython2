def multiplicar(x, y):
  return x * y

print(multiplicar(3, 6))

# Mismo ejemplo con lambda (2 líneas de código)
multiplicar = lambda x, y: x * y
print(multiplicar(3, 6))

# Mismo ejemplo con lambda (1 línea de código)
print(f'{(lambda x: x * 5)(8)}')
