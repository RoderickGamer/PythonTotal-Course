# Solo se pueden introducir dos argumentos
def suma(a, b):
    return a + b


print(suma(5, 6))


# Ahora no hay limite a los argumentos que puede recibir
def suma(*args):
    total = 0

    for arg in args:
        total = total + arg
    return  total


print(suma(5, 6, 30, 59))


# Ahora no hay limite a los argumentos que puede recibir
def suma(*args):
    return sum(args)


print(suma(5, 6, 30, 59))
