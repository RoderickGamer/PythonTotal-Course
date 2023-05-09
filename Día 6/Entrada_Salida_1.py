#
mi_archivo = open('prueba.txt')

#print(mi_archivo)


'''
# La variable mi_archivo, al estar asociado a un archivo tiene unos metodos propios
# Método para leer pero sin mostrar [.read()]
# Imprimir la accion de leer
#print(mi_archivo.read())


# Imprimir solo una linea del archivo
# Si se imprimen seguidas, el sistema lee diferentes lineas
# Como son strings, puedes aplicar metodos de string
una_linea = mi_archivo.readline()
print(una_linea.upper())

# Para quitar el salto de linea [.rstrip()]
una_linea = mi_archivo.readline()
print(una_linea.rstrip())

una_linea = mi_archivo.readline()
print(una_linea)

# Se puede iterar
for l in mi_archivo:
    print('Aquí dice: ' + l)
'''

#
todas = mi_archivo.readlines()
print(todas)


# Siempre cerrar la apertura del archivo
mi_archivo.close()
