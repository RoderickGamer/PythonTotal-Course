#
monedas = 5

while monedas > 0:
    print(f'Tengo {monedas} monedas')
    monedas -= 1
else:
    print('No tengo más monedas')

#
respuesta = 's'

while respuesta == 's':
   respuesta = input('Quieres seguir? (s/n)')
else:
    print('Gracias')

# Dejar una funcion vacia sin que marque error
respuesta = 's'

while respuesta == 's':
   pass

print('Gracias')

#Salir del bucle cuando se cumpla una condicion
nombre = input('Tu nombre')

for letra in nombre:
    if letra == 'r':
        break
    print(letra)

#Saltar a la siguiente iteracion
nombre = input('Tu nombre')

for letra in nombre:
    if letra == 'r':
        continue
    print(letra)