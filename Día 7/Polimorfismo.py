class Vaca:

    def __init__(self, nombre):
        self.nombre = nombre

    def hablar(self):
        print(self.nombre + ' dice muuu')


class Oveja:

    def __init__(self, nombre):
        self.nombre = nombre

    def hablar(self):
        print(self.nombre + ' dice beee')


vaca1 = Vaca('Aurora')
oveja1 = Oveja('Nube')

vaca1.hablar()
oveja1.hablar()

# Podemos meter a una lista objetos de diferentes clases
animales = [vaca1, oveja1]
# Con una iteracion podemos hacer que diferentes clases hagan metodos
# que se llamen igual
for animal in animales:
    animal.hablar()


def animal_habla(animal):
    animal.hablar()


animal_habla(vaca1)
animal_habla(oveja1)