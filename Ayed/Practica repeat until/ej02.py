acum = cont = 0; rta = 'C'
while rta == 'C':
    sueldo = float(input('Ingresar sueldo: '))
    cont += 1; acum += sueldo
    rta = input('C/F: ').upper()
    while rta not in 'CF':
        rta = ('C/F: ').upper()
print(f'Promedio {acum/cont} ')