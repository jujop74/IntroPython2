# Ejemplo variable nonlocal
def subrutina():
    def sub_subrutina():
        nonlocal x
        print(x)
        x = 10
        return

    x = 20
    sub_subrutina()
    print(x)
    return

x = 30
subrutina()
print(x)
