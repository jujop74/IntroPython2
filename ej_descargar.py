# Ejemplo descargar y descomprimir un fichero con wget
# import wget

# url='https://info.stackoverflowsolutions.com/rs/719-EMH-566/images/stack-overflow-developer-survey-2021.zip'
# wget.download(url)


import requests

url='https://info.stackoverflowsolutions.com/rs/719-EMH-566/images/stack-overflow-developer-survey-2021.zip'
req = requests.get(url)

# Se obtiene solamante el nombre del fichero en la URL
fichero = url.split('/')[-1]

with open(fichero, 'wb') as output_file:
    output_file.write(req.content)
  