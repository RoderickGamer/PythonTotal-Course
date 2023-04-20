#Esto se hacia antes
serie = 'N-02'

if serie == 'N-01':
    print('Samsung')
elif serie == 'N-02':
    print('Nokia')
elif serie == 'N-03':
    print('Motorola')
else:
    print('No existe ese producto')

#Ahora con match
match serie:
    case 'N-01':
        print('Samsung')
    case 'N-02':
        print('Nokia')
    case 'N-03':
        print('Motorola')
    case _:
        print('No existe ese producto')


cliente = {'nombre': 'federico',
           'edad': 45,
           'ocupación': 'instructor'}
pelicula = {'titulo': 'Matrix',
            'ficha tecnica': {'protagonista': 'Keani Reeves',
                              'director': 'Lana y Lilly Wachowski'}}
elementos = [cliente, pelicula, 'libro']

for e in elementos:
    match e:
        case {'nombre': nombre,
              'edad': edad,
              'ocupación': ocupacion}:
            print('Es un cliente')
            print(nombre, edad, ocupacion)
        case {'titulo': titulo,
              'ficha tecnica': {'protagonista': protagonista,
                                 'director': director}}:
            print('Es una pelicula')
            print(titulo, protagonista, director)
        case _:
            print('No se que es esto')