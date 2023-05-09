from pathlib import Path
'''
# Crear una ruta relativa
guia = Path('Barcelona', 'Sagrada Familia')
print(guia)


# El home devuelve la ruta del directorio principal del usuario
base = Path.home()
guia = Path('Barcelona', 'Sagrada Familia')
print(base)
print(guia)

guia = Path(base, 'Barcelona', 'Sagrada Familia')
print(guia)


# Un Path dentro de un Path
base = Path.home()
guia = Path(base, 'Europa', 'España', Path('Barcelona', 'Sagrada Familia.txt'))
print(guia)


# Usar un Path para redireccionar
base = Path.home()
guia = Path(base, 'Europa', 'España', Path('Barcelona', 'Sagrada Familia.txt'))
guia2 = guia.with_name('La_Pedrera.txt')
print(guia)
print(guia2)


# Devuelve el antecesor más inmediato de una ruta determinada
base = Path.home()
guia = Path(base, 'Europa', 'España', Path('Barcelona', 'Sagrada Familia.txt'))
print(guia.parent.parent)


# Devuelve el antecesor más inmediato de una ruta determinada
base = Path.home()
guia = Path(base, 'Europa', 'España', Path('Barcelona', 'Sagrada Familia.txt'))
print(guia.parent.parent)
'''

# Devuelve todos los archivos buscados en la ruta seleccionada
guia = Path(Path.home(), 'Europa')
for txt in Path(guia).glob('*.txt'):
    print(txt)


# Devuelve todos los archivos buscados en la ruta seleccionada incluyendo subdirectorios
guia = Path(Path.home(), 'Europa')
for txt in Path(guia).glob('**/*.txt'):
    print(txt)


# Buscar rutas relativas en una ruta seleccionada
guia = Path('Europa', 'España', 'Barcelona', 'Sagrada Familia.txt')
en_europa = guia.relative_to(Path('Europa'))
en_espania = guia.relative_to(Path('Europa', 'España'))
print(en_europa)
print(en_espania)
