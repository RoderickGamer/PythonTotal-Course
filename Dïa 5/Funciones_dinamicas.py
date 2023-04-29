def chequear_3_cifras(numero):
    return numero in range(100, 1000)


resultado = chequear_3_cifras(658)

print(resultado)


#
def chequear_3_cifras(numero):
    return numero in range(100, 1000)


suma = 500 + 499
resultado = chequear_3_cifras(suma)

print(resultado)


# Loop que solo devuelve True o NoneType
def chequear_3_cifras(lista):
    for n in lista:
        if n in range(100,1000):
            return True
        else:
            pass


resultado = chequear_3_cifras([55,99,6000])

print(resultado)


# Loop que sí devuelve False
def chequear_3_cifras(lista):
    for n in lista:
        if n in range(100,1000):
            return True
        else:
            pass
    return False


resultado = chequear_3_cifras([555,99,6000])

print(resultado)


# Devolver lista con todos los numeros de 3 cifras
def chequear_3_cifras(lista):

    lista_3_cifras = []

    for n in lista:
        if n in range(100,1000):
            lista_3_cifras.append(n)
        else:
            pass
    return lista_3_cifras


resultado = chequear_3_cifras([555,999,6000])

print(resultado)