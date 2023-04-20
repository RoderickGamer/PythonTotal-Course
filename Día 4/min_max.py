#Usando MIN
menor = min(578,23,45,567,78)
print(menor)

#Usando MAX
menor = min(578,23,45,567,78)
mayor = max(578,23,45,567,78)
print(mayor)

#Usar una lista
lista = [578,23,45,567,78]
print(max(lista))

#Lista de string alfabeticamente
nombres = ['juan', 'pablo', 'alicia', 'carlos']
print(min(nombres))

#Primero ordena letras mayusculas y luego minusculas
nombre = "Carlos"
print(min(nombre))

nombre = "carlos"
print(min(nombre))

nombre = "Carlos"
print(min(nombre.lower()))

#Ahora con diccionarios
dic = {'C1':45, 'C2':11}
print(min(dic))

dic = {'C1':45, 'C2':11}
print(min(dic.values()))