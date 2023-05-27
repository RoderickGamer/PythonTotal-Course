class Pajaro:

    alas = True

    def __init__(self, mi_color, especie):
        self.color = mi_color
        self.especie = especie

    def piar(self):
        print('pío, mi color es {}'.format(self.color))
        print(f'pío, mi color es {self.color}')

    # Puede llamar/invocar a otros metodos
    # self.piar
    def volar(self, metros):
        print(f'El pajaro ha volado {metros} metros.')
        self.piar()

    # Puede modificar los atributos del objeto
    # self.color
    def pintar_negro(self):
        self.color = 'negro'
        print(f'Ahora el pájaro es {self.color}')

    # Metodos de clase
    @classmethod
    def poner_huevos(cls, cantidad):
        print(f'Puso {cantidad} huevos')
        cls.alas = False
        print(Pajaro.alas)

    # Metodo estatico
    # No puede ver ni modificar instancias ni clase
    @staticmethod
    def mirar():
        # self.color
        # cls.alas = 2
        print('El pajaro mira')


piolin = Pajaro('amarillo', 'Canario')

# El metodo de instancia 'pintar_negro()' necesita una instancia para ejecutarse
piolin.pintar_negro()

# Puede modificar los atributos de clase
piolin.alas = False

# El metodo de clase no necesita una instancia para ejecutarse
Pajaro.poner_huevos(3)

Pajaro.mirar()