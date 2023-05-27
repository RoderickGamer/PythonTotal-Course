class Pajaro:
    # Atributos que todas las instancias creadas van a poseer
    # En este caso todos los pájaros creados van a tener alas
    alas = True

    # Atributos de instancia que serán diferentes para cada una
    # __init__  es el constructor de la clase
    # self es parámetro obligatorio, indica cada atributo que se vaya a crear
    # mi_color es parámetro, se asigna en () al momento de crear la instancia
    # .color es atributo de la instancia, es como se le va a llamar
    def __init__(self, mi_color, especie):
        self.color = mi_color
        self.especie = especie


# self = Pajaro(mi_color, especie)
mi_pajaro = Pajaro('negro', 'Tucán')

print(mi_pajaro.color)
print(mi_pajaro.especie)

print(f'Mi pájaro es un {mi_pajaro.especie} color {mi_pajaro.color}.')

print(Pajaro.alas)

print(mi_pajaro.alas)
