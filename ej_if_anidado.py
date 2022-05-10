password = input('Ingresa la clave: ')

if len(password) >= 8:
  print('Clave verificada')

  if password == '12345678':
    print('Clave correcta')
  else:
    print('Clave incorrecta')

else:
  print('La clave tiene menos de 8 caracteres')  
