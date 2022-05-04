# Ejemplo de variable global
def subrutina():
    global var_global
    print(var_global)
    var_global = 10
    return

var_global = 5
subrutina()
print(var_global)
