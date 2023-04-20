#from random import randint
from random import *

#Numero entero aleatorio
aleatorio = randint(1, 50)
print(aleatorio)

#Numero float aleatorio
aleatorio = round(uniform(1,5),2)
print(aleatorio)

#Numero float aleatorio entre 0 y 1
aleatorio = random()
print(aleatorio)

#Aleatorio de una lista
colores = ['azul', 'rojo', 'verde', 'amarillo']
aleatorio = choice(colores)
print(aleatorio)

#Mezcla una lista
numeros = list(range(5, 50, 5))
shuffle(numeros)
print(numeros)