# Clase padre
class Animal:

    def __init__(self, edad, color):
        self.edad = edad
        self.color = color

    def nacer(self):
        print('Este animal ha nacido')

    def hablar(self):
        print('Este animal emite un sonido')


# Clase hija
class Pajaro(Animal):

    '''# Primera forma de agregar atributos propios
    def __init__(self, edad, color, altura_vuelo):
        self.edad = edad
        self.color = color
        self.altura_vuelo = altura_vuelo'''

    # Segunda forma (mas facil) de agregar atributos propios
    def __init__(self, edad, color, altura_vuelo):
        super().__init__(edad, color)
        self.altura_vuelo = altura_vuelo

    # Modifica un metodo heredado
    def hablar(self):
        print('pio')

    # Metodo propio
    def volar(self, metros):
        print(f'El pajaro vuela {metros} metros')


piolin = Pajaro(3, 'amarillo', 60)

mi_animal = Animal(5, 'negro')

piolin.nacer()
# No usa el metodo hablar de Animal, sino el modificado de Pajaro
piolin.hablar()
# Metodo propio
piolin.volar(50)

#
# HERENCIA MULTIPLE
#

class Padre:
    def hablar(self):
        print('Hola')


class Madre:
    def reir(self):
        print('Ja ja ja')

    def hablar(self):
        print('Qué tal?')


# Los hijos heredan de izquierda a der, en este caso primero de Padre luego Madre
class Hijo(Padre, Madre):
    pass


class Nieto(Hijo):
    pass


mi_nieto = Nieto()
# En caso de metodos iguales hereda primero de izquierda a derecha
mi_nieto.hablar()
mi_nieto.reir()

print(Nieto.__mro__)