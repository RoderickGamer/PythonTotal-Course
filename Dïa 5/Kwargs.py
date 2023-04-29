# Demostrar que resulta un diccionario
def suma(**kwargs):
    print(type(kwargs))


suma(x=3, y=5 , z=2)


# Imprimir clave y valor
def suma(**kwargs):
    for clave, valor in kwargs.items():
        print(f'{clave} = {valor}')


suma(x=3, y=5 , z=2)


# Sumar los valores del diccionario
def suma(**kwargs):
    total = 0
    for clave, valor in kwargs.items():
        print(f'{clave} = {valor}')
        total = total + valor
    return total

print(suma(x=3, y=5 , z=2))


# Usar numeros, args y kwars en la misma funcion
def prueba(num1, num2, *args, **kwargs):
    print(f'El primer valor es {num1}')
    print(f'El segundo valor es {num2}')

    for arg in args:
        print(f'arg = {arg}')

    for clave, valor in kwargs.items():
        print(f'{clave} = {valor}')


prueba(15, 50, 100, 200, 300, 400, x='uno', y='dos', z='tres')


# desempaquetar usando los asteriscos
def prueba(num1, num2, *args, **kwargs):
    print(f'El primer valor es {num1}')
    print(f'El segundo valor es {num2}')

    for arg in args:
        print(f'arg = {arg}')

    for clave, valor in kwargs.items():
        print(f'{clave} = {valor}')


args = [100, 200, 300, 400]
kwargs = {'x':'uno', 'y':'dos', 'z':'tres'}
prueba(15, 50, *args, **kwargs)