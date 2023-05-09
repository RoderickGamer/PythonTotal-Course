'''
# Modo solo lectura
archivo = open('prueba.txt', 'r')

archivo.write('Soy el nuevo texto')

archivo.close()


# Modo solo escritura (crea un archivo nuevo porque no existe prueba1)
# Modo solo escritura (reemplaza el archivo si es que ya existe)
archivo = open('prueba1.txt', 'w')
archivo.write('Soy el nuevo texto')
archivo.close()

archivo = open('prueba1.txt', 'w')
archivo.write('Hola\n')
archivo.write('mundo')
archivo.close()


# Modo solo escritura multiples lineas
# con .writelines() escribes string en forma de lista, uno detras de otro
archivo = open('prueba2.txt', 'w')
archivo.writelines(['Hola', 'mundo', 'aquí', 'estoy'])
archivo.close()


# Modo solo 'agregar' (uso más común)
# Agrega lineas a un archivo, o crea uno si no existe.
archivo = open('prueba2.txt', 'a')
archivo.write('\nBienvenido')
archivo.close()
'''