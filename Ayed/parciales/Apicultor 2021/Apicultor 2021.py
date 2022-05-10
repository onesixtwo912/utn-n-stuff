import os
def menu():    
    os.system('cls')
    mostrarmenu = '1 - Produccion total. \n2 - Colmena mas productiva y cantidad que produjo. \n3 - Porcentaje de colmenas activas. \n4 - Salir'
    opcion = input(f'{mostrarmenu} \nIngresar opcion: ')	
    while opcion < '1' or opcion > '4':
        os.system('cls')
        opcion = input(f'{mostrarmenu} \nIngresar opcion: ')	
    while opcion != '4':
        if opcion == '1':
            print(f'Produccion total: {prodTotal} Kgs')
        elif opcion == '2':
            print(F'La mas productiva fue: {auxC} con {max} kgs')
        elif opcion == '3':
            print(f'{cont/n*100}% del total') 
        input()
        os.system('cls')
        opcion = input(f'{mostrarmenu} \nIngresar opcion: ')	
        while opcion < '1' or opcion > '4':
            os.system('cls')
            opcion = input(f'{mostrarmenu} \nIngresar opcion: ')	
    
prodTotal = max = cont = 0
n = int(input('Ingresar cantidad de colmenas: '))
for c in range(n):
    mayorC = 0
    codigo = input('Ingresar codigo: ')
    while codigo < '0' or codigo > '999':
        codigo = input('Ingresar codigo: ')
    prodAct = input('¿produccion activa? S/N: ').upper()
    while prodAct != 'S' and prodAct != 'N':
        prodAct = input('¿produccion activa? S/N: ').upper()
    if prodAct == 'S':
        kgs = float(input('Ingresar cantidad de Kgs recolectados: '))
        mayorC = mayorC + kgs
        prodTotal = prodTotal + kgs
        cont = cont + 1
        if mayorC > max:
            max = mayorC
            auxC = codigo
menu()
