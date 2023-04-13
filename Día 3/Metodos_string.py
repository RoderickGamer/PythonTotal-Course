texto = "Este es el texto de Roderick"
resultado = texto.upper()
print(resultado)

texto = "Este es el texto de Roderick"
resultado = texto[2].upper()
print(resultado)

texto = "Este es el texto de Roderick"
resultado = texto.lower()
print(resultado)

texto = "Este es el texto de Roderick"
resultado = texto.split() #espacio por defecto
print(resultado)

texto = "Este es el texto de Roderick"
resultado = texto.split("t")
print(resultado)

a = "Aprender"
b = "Python"
c = "es"
d = "genial"
e = "-".join([a, b, c, d])
print(e)

texto = "Este es el texto de Roderick"
resultado = texto.find("s")
print(resultado)

texto = "Este es el texto de Roderick"
resultado = texto.replace("Roderick", "todos")
print(resultado)