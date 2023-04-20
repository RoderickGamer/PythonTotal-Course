#MMetodo comun
palabra = 'Python'

lista = []

for letra in palabra:
    lista.append(letra)

print(lista)

#MMetodo comun
palabra = 'Python'

lista = [letra for letra in palabra]
print(lista)

#otra forma
lista = [letra for letra in 'Python']
print(lista)

#Con numeros
lista = [n for n in range(0,21,2)]
print(lista)

#Con numeros
lista = [n / 2 for n in range(0,21,2)]
print(lista)

#Con if
lista = [n if n * 2 > 10 else 'no' for n in range(0,21,2)]
print(lista)

#Con numeros
pies = [10, 20, 30, 40, 50]
metros = [pie / 3.281 for pie in pies]

print(metros)

#Con numeros
pies = [10, 20, 30, 40, 50]
metros = [round(pie / 3.281, 2) for pie in pies]

print(metros)
