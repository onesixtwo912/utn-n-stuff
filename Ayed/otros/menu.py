#import os
def mostrarMenu():
    os.system('cls')
    print('1 - xxxxxxxxxxx')
    print('2 - yyyyyyyyyyy')
    print('3 - zzzzzzzzzzz')
    print('4 - Salir')

def menu():    
    mostrarMenu()
    opcion = input('Ingresar opcion: ')
    while opcion < '1' or opcion > '4':
        os.system('cls')
        mostrarMenu()
        opcion = input('Ingresar opcion: ')

    while opcion != '4':
        if opcion == '1':
            print('xxxxxxxxxxx')
        elif opcion == '2':
            print('yyyyyyyyyyy')
        elif opcion == '3':
            print('zzzzzzzzzzz') 
        input()
        os.system('cls')
        mostrarMenu()
        opcion = input('Ingresar opcion: ')
        while opcion < '1' or opcion > '4':
            os.system('cls')
            mostrarMenu()
            opcion = input('Ingresar opcion: ')

