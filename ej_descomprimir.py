# Ejemplo descargar y descomprimir un fichero con urllib.request
from io import BytesIO
from urllib.request import urlopen
from zipfile import ZipFile

zip_url='https://info.stackoverflowsolutions.com/rs/719-EMH-566/images/stack-overflow-developer-survey-2021.zip'

with urlopen(zip_url) as zipresp:
    with ZipFile(BytesIO(zipresp.read())) as zfile:
        # Directorio donde guardar los ficheros
        zfile.extractall('/home/runner/IntroPython')
