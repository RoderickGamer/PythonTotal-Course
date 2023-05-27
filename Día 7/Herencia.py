# Clase padre
class Animal:

    def __init__(self, edad, color):
        self.edad = edad
        self.color = color

    def nacer(self):
        print('Este animal ha nacido')


# Clase hija
class Pajaro(Animal):
    pass


piolin = Pajaro(2, 'amarillo')

piolin.nacer()

print(piolin.color)

# Ver que subclases están enlazadas a Animal
print(Animal.__subclasses__())

# Ver que clase es la padre de Pajaro
print(Pajaro.__bases__)