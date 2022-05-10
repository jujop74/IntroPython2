# Ejemplo de uso de la biblioteca re
import re

# Encontrar coincidencias
texto = 'Hoy es un día magnífico y maravilloso'
exp_reg = re.search('^Hoy.*oso$', texto)

print(exp_reg)

# Encuentra todas la coincidencias
exp_reg2 = re.findall('ma', texto)
print(exp_reg2)

# Reemplazar espacios vacíos
exp_reg3 = re.sub('\s', '      ', texto)
print(exp_reg3)
