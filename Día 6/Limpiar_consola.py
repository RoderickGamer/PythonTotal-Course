#
from os import system

nombre = input('Dime tu nombre: ')
edad = input('Dime tu edad: ')

# Limpiar en windows ('cls')
# Limpiar en otro sistema ('clear')
system('cls')

print(f'Tu nombre es {nombre} y tienes {edad} años')