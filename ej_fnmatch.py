import fnmatch
import os

# Busca todos los ficheros con el patrón especificado
patron = 'main*.py'
print('Patron:', patron)
print('*****')

ficheros = os.listdir('./')
for nombre in ficheros:
    print('Nombre: %-25s %s' % (nombre, fnmatch.fnmatch(nombre, patron)))
