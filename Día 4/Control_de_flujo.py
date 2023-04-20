# if
if 10 > 9:
    print('Es correcto')

# if
x = True
if x:
    print('Es correcto')

# if
if 10 < 9:
    print('Es correcto')
else:
    print('Es incorrecto')

# if
mascota = 'perro'
if mascota == 'gato':
    print('Tienes un gato')
else:
    print('No se quie animal tienes')

# if
mascota = 'perro'
if mascota == 'gato':
    print('Tienes un gato')
elif mascota == 'perro':
    print('Tienes un perro')
else:
    print('No se quie animal tienes')

# if
edad = 16
calificacion = 9

if edad < 18:
    print('Eres menor de edad')
    if calificacion >= 7 :
        print('Aprovado')
    else:
        print('No aprovado')
else:
    print('Eres adulto')