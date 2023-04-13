diccionario = {'c1':'valor1', 'c2':'valor2'}
print(type(diccionario))

diccionario = {'c1':'valor1', 'c2':'valor2'}
print(diccionario)

diccionario = {'c1':'valor1', 'c2':'valor2'}
resultado = diccionario['c1']
print(resultado)

cliente = {'nombre':'Juan',
           'apellido':'Fuentes',
           'peso':88,
           'talla':1.76}
consulta = (cliente['apellido'])
print(consulta)

dic = {'c1':55,
       'c2':[10, 20, 30],
       'c3': {'s1':100,
              's2':200}}
print(dic['c2'][1])

dic = {'c1':55,
       'c2':[10, 20, 30],
       'c3': {'s1':100,
              's2':200}}
print(dic['c3']['s1'])

dicc = {'c1':['a', 'b', 'c'],
        'c2':['d', 'e', 'f']}
print(dicc['c2'][1].upper())

dic = {1:'a', 2:'b'}
dic[3] = 'c'
print(dic)

dic = {1:'a', 2:'b'}
dic[2] = 'v'
dic[3] = 'c'
print(dic)

print(dic.keys())
print(dic.values())
print(dic.items())