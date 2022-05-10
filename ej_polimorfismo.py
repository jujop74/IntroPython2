class Animal:
    def hablar(self):
        pass

# Hereda de la clase Animal
class Perro(Animal):
    def hablar(self):
        print("Guau!")

# Hereda de la clase Animal
class Gato(Animal):
    def hablar(self):
        print("Miau!")


# Polimorfismo: se llama a la función de la clase adecuada según el tipo de objeto
for animal in Perro(), Gato():
    animal.hablar()

# animal1 = Perro()
# animal2 = Gato()

# animal1.hablar()
# animal2.hablar()
