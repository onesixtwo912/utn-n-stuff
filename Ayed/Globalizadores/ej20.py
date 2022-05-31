acum = cont = 0; rta = ''
while rta != 'F':
    for k in range(5):
        elemento = int(input('Ingresar elemento: '))
        acum += elemento; cont += 1
    print(f'El promedio del subconjunto {k} es {acum/cont}.')
    rta = input('C/F: ').upper()
    while rta not in 'CF': 
        rta = input('C/F: ').upper()