mi_lista = ['a', 'b', 'c']
print(type(mi_lista))

mi_lista = ['a', 'b', 'c']
resultado = len(mi_lista)
print(resultado)

mi_lista = ['a', 'b', 'c']
resultado = mi_lista[0]
print(resultado)

mi_lista = ['a', 'b', 'c']
resultado = mi_lista[0:2]
print(resultado)

mi_lista = ['a', 'b', 'c']
mi_lista2 = ['d', 'e', 'f']
print(mi_lista + mi_lista2)

mi_lista = ['a', 'b', 'c']
mi_lista2 = ['d', 'e', 'f']
mi_lista3 = mi_lista + mi_lista2
print(mi_lista3)

mi_lista = ['a', 'b', 'c']
mi_lista2 = ['d', 'e', 'f']
mi_lista3 = mi_lista + mi_lista2
mi_lista3[0] = 'alpha'
print(mi_lista3)

mi_lista = ['a', 'b', 'c']
mi_lista2 = ['d', 'e', 'f']
mi_lista3 = mi_lista + mi_lista2
mi_lista3.append('G')
print(mi_lista3)

mi_lista = ['a', 'b', 'c']
mi_lista2 = ['d', 'e', 'f']
mi_lista3 = mi_lista + mi_lista2
mi_lista3.pop() #Con parentesis vacio se elimina el ultimo elemento
print(mi_lista3)

mi_lista = ['a', 'b', 'c']
mi_lista2 = ['d', 'e', 'f']
mi_lista3 = mi_lista + mi_lista2
eliminado = mi_lista3.pop()
print(mi_lista3)
print(eliminado)

lista = ['g', 'o', 'b', 'm', 'c']
lista.sort()
print(lista)

lista = ['g', 'o', 'b', 'm', 'c']
lista.reverse()
print(lista)