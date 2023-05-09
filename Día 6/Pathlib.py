# Leer un archivo sin abrirlo ni cerrarlo
from pathlib import Path, PureWindowsPath

carpeta = Path('D:/Documentos/Documentos/Cursos Online e idiomas/Udemy/Python TOTAL - Programador Avanzado en 16 días/Dia 6/Prueba.txt')
print(carpeta.read_text())


# Traer el nombre del archivo
carpeta = Path('D:/Documentos/Documentos/Cursos Online e idiomas/Udemy/Python TOTAL - Programador Avanzado en 16 días/Dia 6/Prueba.txt')
print(carpeta.name)


# Traer la extension del archivo
carpeta = Path('D:/Documentos/Documentos/Cursos Online e idiomas/Udemy/Python TOTAL - Programador Avanzado en 16 días/Dia 6/Prueba.txt')
print(carpeta.suffix)

# Traer el nombre del archivo sin extension
carpeta = Path('D:/Documentos/Documentos/Cursos Online e idiomas/Udemy/Python TOTAL - Programador Avanzado en 16 días/Dia 6/Prueba.txt')
print(carpeta.stem)


# saber si un archivo existe
carpeta = Path('D:/Documentos/Documentos/Cursos Online e idiomas/Udemy/Python TOTAL - Programador Avanzado en 16 días/Dia 6/Prueba.txt')
if not carpeta.exists():
    print('Este archivo no existe')
else:
    print('Sí existe')


# El PurewindowsPath convierte cualquier ruta en una ruta aceptada por windows
carpeta = Path('D:/Documentos/Documentos/Cursos Online e idiomas/Udemy/Python TOTAL - Programador Avanzado en 16 días/Dia 6/Prueba.txt')
ruta_windows = PureWindowsPath(carpeta)
print(ruta_windows)