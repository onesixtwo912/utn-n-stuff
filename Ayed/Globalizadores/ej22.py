total = max = 0
art = input('Ingresar articulo: ')
while art != '0':
    aux = art; cantidad_vendida = 0
    while art == aux:
        cantidad =int('Ingresar cantidad: ')
        precio =float('Ingresar precio: ')
        total += precio; cantidad_vendida += cantidad
        art = input('Ingresar articulo: ')
    print(cantidad_vendida,aux)
    max, art_max = cantidad_vendida, aux if cantidad_vendida > max else 0
print(total)
print(art_max,max)