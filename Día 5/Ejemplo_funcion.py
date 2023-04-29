#
precios_cafe = [('capuchino', 1.5), ('expresso', 1.2), ('moka', 1.9)]

for elemento in precios_cafe:
    print(elemento)

#
precios_cafe = [('capuchino', 1.5), ('expresso', 1.2), ('moka', 1.9)]

for cafe, precio in precios_cafe:
    print(cafe)

#
precios_cafe = [('capuchino', 1.5), ('expresso', 1.2), ('moka', 1.9)]

for cafe, precio in precios_cafe:
    print(precio * .45)

#
precios_cafe = [('capuchino', 1.5), ('expresso', 1.2), ('moka', 1.9)]
def cafe_mas_caro(lista_precios):

    precio_mayor = 0
    cafe_mas_caro = ''

    for cafe, precio in lista_precios:
        if precio > precio_mayor:
            precio_mayor = precio
            cafe_mas_caro = cafe
        else:
            pass

    return (cafe_mas_caro, precio_mayor)

cafe, precio = cafe_mas_caro(precios_cafe)
print(cafe)
print(precio)