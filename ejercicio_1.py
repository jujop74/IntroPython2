# Crear un programa que pregunte el nombre y la edad y muestre por pantalla
# el nombre y el año en el que cumplirá 100 años

def funcion_nombre():
  nombre = input('Introduzca su nombre: ')
  return nombre

def funcion_edad():
  edad = int(input('Introduzca su edad: '))
  return edad

anyo_actual = 2022
nombre = funcion_nombre()
edad = funcion_edad()

print('')
print('Su nombre es:', nombre)
print('El año en el que cumplirá 100 años será:', anyo_actual + 100 - edad)
