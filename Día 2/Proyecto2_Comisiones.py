nombre = input('¿Cuál es tu nombre? ')
ventas_mes = round(float(input('¿Cuánto vendiste este mes? ')),2)

print(f'¡Muchas gracias por tu esfuerzo en las ventas de este mes!\n'
      f'Tus ventas fueron de ${ventas_mes}\n'
      f'Tu comisión será de ${round(ventas_mes * 0.13,2)}\n'
      f'Tu ganancia total es de ${round(ventas_mes * 1.13,2)}')