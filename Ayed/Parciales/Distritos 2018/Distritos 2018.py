import os
def menu():    
    os.system('cls')
    mostrarmenu = '1 - Total de habitantes en Rosario. \n2 - Cantidad de habitantes por tipo de vivienda. \n3 - Distrito con mayor ingreso mensual \n4 - Salir'
    opcion = input(f'{mostrarmenu} \nIngresar opcion: ');os.system('cls')
    while opcion < '1' or opcion > '4':
        opcion = input(f'{mostrarmenu} \nIngresar opcion: ');os.system('cls')
    while opcion != '4':
        if opcion == '1':
            print(f'Total de habitantes {casa + dto}')
        elif opcion == '2':
            print(f'Cantidad de habitantes en casas: {casa} \nCantidad de habitantes en departamentos: {dto}')
        elif opcion == '3':
            print(f'Distrito con mayor ingreso mensual: {maxDist}.')
        input(); os.system('cls')
        opcion = input(f'{mostrarmenu} \nIngresar opcion: '); os.system('cls')
        while opcion < '1' or opcion > '4':
            opcion = input(f'{mostrarmenu} \nIngresar opcion: '); os.system('cls')

casa = dto = max = 0
for distrito in range(1,6):
    acumS = 0
    nro = input('Ingresar numero de vivienda: ')
    while nro != '0':
        tipo = input('Ingresar tipo de vivienda: ').upper()
        while tipo != 'C' and tipo != 'D':
            tipo = input('Ingresar tipo de vivienda: ').upper()
        salario = float(input('Ingresar salario: '))
        acumS = acumS + salario
        habitantes = int(input('Ingresar cantidad de habitantes: '))
        if tipo == 'C':
            casa = casa + habitantes
        else:
            dto = dto + habitantes
        nro = input('Ingresar numero de vivienda: ')
    if acumS > max:
        max = acumS
        maxDist = distrito
menu()
