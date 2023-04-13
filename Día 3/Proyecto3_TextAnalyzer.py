text_user = (input('Por favor ingresa tu texto ')).lower()
letters_user = list(input('Por favor ingresa 3 letras al azar ').lower())
word_user = (input('¿Hay alguna palabra en particular que quieras buscar? ')).lower()

letter1 = text_user.count(letters_user[0])
letter2 = text_user.count(letters_user[1])
letter3 = text_user.count(letters_user[2])

list_text_user = text_user.split()

print(f'Tus letras aparecen la siguiente cantidad de veces:\n'
      f'{letters_user[0]}: {letter1} veces\n'
      f'{letters_user[1]}: {letter2} veces\n'
      f'{letters_user[2]}: {letter3} veces\n')

print(f'Además, tu texto tiene {len(list_text_user)} palabras\n'
      f'de las cuales, la primera es "{text_user[0]}" y la última es "{text_user[-1]}".\n')

print(f'Como curiosidad, este es tu texto en orden inverso xd:\n'
      f'{text_user[::-1]}\n'
      f'dato completamente inútil :v\n')

print(f'¿Será que la palabra "{word_user}" se encuentre en el texto?\n'
      f'{word_user}: {word_user in text_user}\n'
      f'¿Cuántas veces? {text_user.count(word_user)} veces')

