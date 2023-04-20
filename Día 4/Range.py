#El range(5) indica a partir del 0 hasta uno antes, o sea el 4
for numero in range(5):
    print(numero)

#El primer numero es el comienzo el segundo el final (exclusivo)
for numero in range(1, 6):
    print(numero)

#El tercer numero es cada cuanto va a contar
for numero in range(1, 20, 2):
    print(numero)

#Puedes hacer una lista con el rango
lista = list(range(1,101))
print(lista)