mi_set = set({1, 2, 3, 4, 5})
print(type(mi_set))
print(mi_set)

otro_set = {1, 2, 3}
print(type(otro_set))
print(otro_set)

mi_set = set({1, 2, 3, 4, (1, 2, 3, 4), 5})
print(mi_set)

mi_set = set({1, 2, 3, 4, 5})
print(len(mi_set))

mi_set = set({1, 2, 3, 4, 5})
print(2 in mi_set)

mi_set = set({1, 2, 3, 4, 5})
print(2 not in mi_set)

s1 = {1, 2, 3}
s2 = {3, 4, 5}
s3 = s1.union(s2)
print(s3)

s1 = {1, 2, 3}
s1.add(4)
print(s1)

s1 = {1, 2, 3}
s1.remove(3)
print(s1)

s1 = {1, 2, 3}
s1.discard(6)
print(s1)

s1 = {1, 2, 3}
s1.pop() #Como no hay orden, al estar vacio elimina aleatoriamente
print(s1)

s1 = {1, 2, 3}
s1.clear()
print(s1)