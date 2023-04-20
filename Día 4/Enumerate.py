#Esta seria la forma básica de hacerlo en Python
lista = ['a', 'b', 'c']
indice = 0

for item in lista:
    print(indice, item)
    indice += 1

# Usando Enumerate
lista = ['a', 'b', 'c']

for item in enumerate(lista):
    print(item)

#
for item in enumerate(range(1, 10)):
    print(item)

#Convirtiendo las tuplas en una lista
lista = ['a', 'b', 'c']

mis_tuples = list(enumerate(lista))
print(mis_tuples)