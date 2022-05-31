max, max_destino = 0,''
destino = input('Ingresar destino: ').upper()
while destino not in 'ABCDEFGHI' and destino != '*':
    destino = input('Ingresar destino: ').upper()
while destino != '*':
    aux, cont = destino, 0
    while destino == aux:
        capacidad = int(input('Ingresar capacidad de pasajeros: '))
        combustible = float(input('Ingresar combustible necesario: '))
        cont += 1
        destino = input('Ingresar destino: ').upper()        
        while destino not in 'ABCDEFGHI' and destino != '*':
            destino = input('Ingresar destino: ').upper()
    print(f'Destino {aux}: {cont} vuelos. ')
    if cont > max:
        max, max_destino = cont, aux
print(f'El destino {max_destino} tuvo la mayor cantidad de vuelos.')