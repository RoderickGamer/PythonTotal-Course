dic = {'clave1': 100, 'clave2': 500}

a = dic.popitem()

print(a)
print(dic)

a = ",:_#,,,,,,:::____##Pyt%on_ _Total,,,,,,::#"
b = ',:%_#'
c = a.lstrip(b)
print(c)

marcas_smartphones = {"Samsung", "Xiaomi", "Apple", "Huawei", "LG"}

marcas_tv = {"Sony", "Philips", "Samsung", "LG"}

conjuntos_aislados = marcas_smartphones.isdisjoint(marcas_tv)

print(conjuntos_aislados)