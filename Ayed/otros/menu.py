import os
def menu():
    mostrarmenu = '1 - xxx \n2 - yyy \n3 - zzz \n4 - Salir'
    opcion = input(f'{mostrarmenu} \nIngresar opcion: ');os.system('cls')
    while opcion < '1' or opcion > '4':
        opcion = input(f'{mostrarmenu} \nIngresar opcion valida: ');os.system('cls')
    while opcion != '4':
        if opcion == '1':
            print(f'xxx')
        elif opcion == '2':
            print(f'yyy')
        elif opcion == '3':
            print(f'zzz')
        input() ; os.system('cls')
        opcion = input(f'{mostrarmenu} \nIngresar opcion: ');os.system('cls')
        while opcion < '1' or opcion > '4':
            opcion = input(f'{mostrarmenu} \nIngresar opcion valida: ');os.system('cls')
menu()
