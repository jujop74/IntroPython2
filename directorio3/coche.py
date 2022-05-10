class Coche:
    def __init__(self, marca, modelo, tipo):
        self.marca = marca
        self.modelo = modelo
        self.tipo = tipo
        self.capacidad_gasolina = 15
        self.nivel_gasolina = 0

    def gasolina_completo(self):
        self.nivel_gasolina = self.capacidad_gasolina
        print('El depósito de gasolina está lleno')

    def conducir(self):
        print(f'El {self.modelo} se está conduciendo.')


# Herencia: extendiendo la clase
class CocheElectrico(Coche):
    # El método __init__ para crear una clase hija
    def __init__(self, marca, modelo, tipo):
        super().__init__(marca, modelo, tipo)
        self.tamanyo_bateria = 100
        self.modelo = modelo
        self.nivel_carga = 0

    # Sobreescribir el método del padre
    def gasolina_completo(self):
        print('El coche no tiene depósito de gasolina')

    # Agregar un nuevo método a la clase
    def cargar(self):
        self.nivel_carga = 100
        print('El coche se está cargando')

objeto_coche = Coche('SEAT', 'Ateca', '1.0')

# Acceder a los atributos del objeto
print(objeto_coche.marca)
print(objeto_coche.modelo)
print(objeto_coche.tipo)

# Llamando a los métodos de la clase
print()
objeto_coche.gasolina_completo()
objeto_coche.conducir()

# Usar el método padre e hijo
print()
obj_coche_electrico = CocheElectrico('TESLA', 'Modelo 3', 'Berlina')

print(obj_coche_electrico.marca)
print(obj_coche_electrico.modelo)
print(obj_coche_electrico.tipo)

print()
obj_coche_electrico.cargar()
obj_coche_electrico.conducir()

# Usar el método sobreescrito
obj_coche_electrico.gasolina_completo()
