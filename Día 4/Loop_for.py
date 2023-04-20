#loop for
lista = ['a', 'b', 'c', 'd']

for letrarda in lista:
    print('letra ' + letrarda)

for letrarda in lista:
    numero_de_letra = lista.index(letrarda) + 1
    print(f'letra  {numero_de_letra}: {letrarda}')

#.starswith es para buscar que algo comience de alguna forma
lista1 = ['pablo', 'laura', 'fede', 'luis', 'julia']
for nombre in lista1:
    if nombre .startswith('l'):
        print(nombre)

#Importancia de la identación (espaciado) poner print al mismo nivel que el for
numeros = [1, 2, 3, 4, 5]
mi_valor = 0
for numero in numeros:
    mi_valor = mi_valor + numero
print(mi_valor)

#Importancia de la identación (espaciado) poner print a diferente nivel que el for
numeros = [1, 2, 3, 4, 5]
mi_valor = 0
for numero in numeros:
    mi_valor = mi_valor + numero
    print(mi_valor)

#
palabra = 'python'
for letra in palabra:
    print(letra)

#iterar a una lista dentro de otra lista
for letra in [[1, 2], [3, 4], [5, 6]]:
    print(letra)

#iterar con dos variables para obtener valores separados
for a, b in [[1, 2], [3, 4], [5, 6]]:
    print(a)
    print(b)

# iterar diccionarios
dic = {'clave1':'a', 'clave2':'b', 'clave3':'c'}
for item in dic:
    print(item)

# iterar diccionarios
dic = {'clave1':'a', 'clave2':'b', 'clave3':'c'}
for item in dic.items():
    print(item)

# iterar diccionarios
dic = {'clave1':'a', 'clave2':'b', 'clave3':'c'}
for item in dic.values():
    print(item)

# iterar diccionarios
dic = {'clave1':'a', 'clave2':'b', 'clave3':'c'}
for a, b in dic.items():
    print(a, b)