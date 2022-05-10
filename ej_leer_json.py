# Leer un fichero JSON
import json

with open('datos_persona.json') as fichero:
    # .loads (encode) toma un string como imput y devuelve un dicccionario
    datos = json.loads(fichero.read())

print(datos)
# Muestra solo un dato del fichero
print(datos['Nombre'])

# Exporta 'datos' a un fichero .json
with open('datos_persona_json.txt', 'w') as json_fichero:
    json.dump(datos, json_fichero)
