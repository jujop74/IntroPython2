# Un ejemplo creando un directorio en la carpeta inicio del usuario
from pathlib import Path
import os

# Se obtien el directorio inicio del usuario en SO Linux y Windows
fichero_path = Path(Path.home(), 'directorio_ficheros')

# Si no existe el directorio, se crea
if not fichero_path.exists():
    os.makedirs(fichero_path)

# Se agregó el fichero al path
fichero_path = fichero_path.joinpath('quijote-ext03.txt')

with fichero_path.open('w') as file:
    lineas = [
        'Primera parte del ingenioso hidalgo don Quijote de la Mancha \n'
        'Capítulo primero. Que trata de la condición y ejercicio del famoso \n'
        'hidalgo don Quijote \n'
    ]
    file.writelines(lineas)

