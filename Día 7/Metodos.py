class Pajaro:

    alas = True

    def __init__(self, mi_color, especie):
        self.color = mi_color
        self.especie = especie

    def piar(self):
        print('pío, mi color es {}'.format(self.color))
        print(f'pío, mi color es {self.color}')

    def volar(self, metros):
        print(f'El pajaro ha volado {metros} metros.')


piolin = Pajaro('amarillo', 'Canario')

piolin.piar()
piolin.volar(50)
