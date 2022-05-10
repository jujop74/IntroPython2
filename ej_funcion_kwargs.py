# Ejemplo de función admitiendo pares de valores
# Como argumento de entrada utilizar **kwargs
def test_kwargs(**kwargs):
  for key, value in kwargs.items():
    # Ambos print hacen lo mismo
    print('{0} = {1}'.format(key, value))
    print(f'{key} = {value}')

kwargs = {'tres':3, 'cinco':5}

test_kwargs(**kwargs)
