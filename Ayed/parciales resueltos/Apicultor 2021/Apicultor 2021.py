import os
def mostrarMenu():
    os.system('cls')
    print('1 - Produccion total')
    print('2 - Colmena mas productiva y cantidad que produjo.')
    print('3 - Porcentaje de colmenas activas.')
    print('4 - Salir')

def menu():
    mostrarMenu()
    opcion = input('ingresar opcion: ')
    while opcion < '1' or opcion > '4':
        os.system('cls')
        mostrarMenu()
        opcion = input('ingresar opcion:')

    while opcion != '4':
        if opcion == '1':
            print(f'Produccion total: {prodTotal} Kgs')
        elif opcion == '2':
            print(F'La mas productiva fue: {auxC} con {max} kgs')
        elif opcion == '3':
            print(f'{cont/n*100}% del total') 
        input()
        os.system('cls')
        mostrarMenu()
        opcion = input('Ingresar opcion: ')
        while opcion < '1' or opcion > '4':
            os.system('cls')
            mostrarMenu()
            opcion = input('Ingresar opcion: ')
    
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
