'''
# Importar modulo OS
import os

# Muestra la ruta actual del archivo
ruta = os.getcwd()
print(ruta)


# Change directory, permite cambiar la ruta de trabajo
ruta1 = os.chdir('D:\\Documentos\\Documentos\\Cursos Online e idiomas\\Udemy\\Python TOTAL - Programador Avanzado en 16 días\\Dia 6')


# Abrir un archivo en la nueva ruta
archivo = open('Prueba.txt')
print(archivo)

# Crear una nueva carpeta en el nuevo destino (poner en la ruta el nombre de la nueva)
#ruta1 = os.makedirs('D:\\Documentos\\Documentos\\Cursos Online e idiomas\\Udemy\\Python TOTAL - Programador Avanzado en 16 días\\Dia 6\\Nueva carpeta')


# Pedir el nombre de la ruta y el nombre del archivo por separado
# Pedir una tupla con ambos nombres separado por coma
ruta2 = 'D:\\Documentos\\Documentos\\Cursos Online e idiomas\\Udemy\\Python TOTAL - Programador Avanzado en 16 días\\Dia 6\\Prueba.txt'

nombre_archivo = os.path.basename(ruta2)
nombre_ruta = os.path.dirname(ruta2)
nombres_separados = os.path.split(ruta2)

print(nombre_ruta)
print(nombre_archivo)
print(nombres_separados)


# Eliminar carpetas con remove directory
#os.rmdir('D:\\Documentos\\Documentos\\Cursos Online e idiomas\\Udemy\\Python TOTAL - Programador Avanzado en 16 días\\Dia 6\\Nueva carpeta')
'''

#
#
# Importar rutas para otros sistemas operativos
from pathlib import Path

# Concatenar rutas con '/'
carpeta = Path('D:/Documentos/Documentos/Cursos Online e idiomas/Udemy/Python TOTAL - Programador Avanzado en 16 días/Dia 6')
archivo = carpeta / 'Prueba.txt'

mi_archivo = open(archivo)
print(mi_archivo.read())

# Concatenar rutas con '/' con una linea menos de codigo
carpeta = Path('D:/Documentos/Documentos/Cursos Online e idiomas/Udemy/Python TOTAL - Programador Avanzado en 16 días/Dia 6') / 'Prueba.txt'
archivo1 = open(carpeta)
print(archivo1.read())