mi_tuple = (1, 2, 3, 4)
print(type(mi_tuple))

mi_tuple = (1, 2, 3, 4)
print(mi_tuple[0]) #se puede indexar

mi_tuple = (1, 2, (10, 20), 4)
print(mi_tuple[2][1])

mi_tuple = (1, 2, 3, 4)
mi_tuple = list(mi_tuple)
print(type(mi_tuple))
mi_tuple = tuple(mi_tuple)
print(type(mi_tuple))

t = (1, 2, 3)
x, y, z = t
print(x, y, z) #Asignar el contenido de t a las variables x, y, z

t = (1, 2, 3, 1)
print(t.count(1)) #Contar cantidad de apariciones de un valor

t = (1, 2, 3, 1)
print(t.index(1))