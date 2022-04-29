import os
def menu():    
    os.system('cls')
    mostrarmenu = '1 - xxx \n2 - yyy \n3 - zzz \n4 - Salir'
    print(mostrarmenu)
    opcion = input('Ingresar opcion: ')
    while opcion < '1' or opcion > '4':
        os.system('cls')
        print(mostrarmenu)
        opcion = input('Ingresar opcion: ')
    while opcion != '4':
        if opcion == '1':
            print(f'xxx')
        elif opcion == '2':
            print(f'yyy')
        elif opcion == '3':
            print(f'zzz')
        input()
        os.system('cls')
        print(mostrarmenu)
        opcion = input('Ingresar opcion: ')
        while opcion < '1' or opcion > '4':
            os.system('cls')
            print(mostrarmenu)
            opcion = input('Ingresar opcion: ')
