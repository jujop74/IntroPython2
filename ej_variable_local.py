# Ejemplo de variable local
def subrutina():
    variable = 10
    print(variable)
    return

variable = 26
subrutina()
print(variable)
subrutina()

# Ejemplo de variable local
def subrutina():
    variable_local = 10
    print(variable_local)
    return

subrutina()
print(variable_local)
