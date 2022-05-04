# # Ejemplo de variables

# lenguaje = 'Pyhton'
# x = 3.14
# y = 3 + 2

# # Asignar múltiples valores
# numero1, numero2 = 1, 2
# numero1, numero2 = 2, 1

# #x = None
# print(x)

# # del x
# # print(x)

# x += 10
# print(x)

# valor = 50
# valor = valor / 2
# print(valor)

# rem = 4
# y = y - (x + valor + rem)
# print(y)

nombre_variable = 'valor'
print(f'El texto y el {nombre_variable}')
print('El texto y el', nombre_variable)

total = 158000000
print(f'El monto total es {total:,} euros'.replace(',', '.'))
print(f'El monto total es {total:,} euros')

# Agrega decimales y formato de moneda
total_decimales = 158000000.57465
print(f'El monto total es: {total_decimales:,.2f} €')

minutos = 2.9
print(f'El proceso tiene una duración de {minutos * 60}')