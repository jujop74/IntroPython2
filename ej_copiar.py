import os
import shutil

# # Copiar ficheros situados en el mismo directorio
# shutil.copy(src='quijote_ext01.txt', dst='quijote_ext03.txt')

# # Copiar ficheros preservando los metadatos del fichero
# # (fecha de creación, usuario, ...)
# shutil.copy2(src='quijote_ext01.txt', dst='quijote_ext04.txt')


# # Copiar al igual que el comando cp -R en Linux
# shutil.copytree(src='directorio/', dst='directorio2/')

# # Ignorar ficheros .txt al copiar
# shutil.copytree(src='directorio/', dst='directorio3/', ignore=
# shutil.ignore_patterns('*.txt'))


# # Mover (o cambiar de nombre al fichero) al igual que el comando mv en Linux
# shutil.move(src='directorio/texto.txt', dst='directorio3/texto.txt')


# # Mover un fichero usando la biblioteca os
# os.rename('directorio2/texto.txt', 'directorio/texto.txt')


# Borrar un fichero
os.remove('directorio/texto.txt')
