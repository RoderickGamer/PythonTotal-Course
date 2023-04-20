#Esto sirve pero hay una forma mejor
mi_bool = 4 < 5 < 6

# and
mi_bool = 4 < 5 and 5 < 6
print(mi_bool)

# and
mi_bool = (4 < 5 )and (5 == 2 + 3)
print(mi_bool)

# or
mi_bool = 4 < 5 or 5 < 4
print(mi_bool)

# or
mi_bool = 1==10 or 5 < 4
print(mi_bool)

# not
mi_bool = not ('a' == 'a')
print(mi_bool)

# not
mi_bool = not ('a' != 'a')
print(mi_bool)