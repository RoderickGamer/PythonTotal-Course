#
nombres = ['Ana', 'Hugo', 'Valeria']
edades = [65, 49, 42]

combinados = list(zip(nombres, edades))

print(combinados)

#La union se termina cuando la lista mas corta termina
nombres = ['Ana', 'Hugo', 'Valeria']
edades = [65, 49, 42, 23, 65, 23]

combinados = list(zip(nombres, edades))

print(combinados)

#La union puede ser del numero de listas que ocupes
nombres = ['Ana', 'Hugo', 'Valeria']
edades = [65, 49, 42, 23, 65, 23]
ciudades = ['Lima', 'Madrid', 'México']

combinados = list(zip(nombres, edades, ciudades))

print(combinados)

#
nombres = ['Ana', 'Hugo', 'Valeria']
edades = [65, 49, 42, 23, 65, 23]
ciudades = ['Lima', 'Madrid', 'México']

combinados = list(zip(nombres, edades, ciudades))

for nombre, edades, ciudades in combinados:
    print(f'{nombre} tiene {edades} años y vive en {ciudades}')