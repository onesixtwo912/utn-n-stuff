import os
def menu():
    mostrarmenu = '1 - Total de personas encuestadas. \n2 - Código de censo de la vivienda con mayor cantidad de personas \n3 - Porcentaje de viviendas habitadas respecto del total de viviendas asignadas. \n4 - Salir'
    opcion = input(f'{mostrarmenu} \nIngresar opcion: ');os.system('cls')
    while opcion < '1' or opcion > '4':
        opcion = input(f'{mostrarmenu} \nIngresar opcion valida: ');os.system('cls')
    while opcion != '4':
        if opcion == '1':
            print(acum_h)
        elif opcion == '2':
            print(max_codigo)
        elif opcion == '3':
            print(tot_h/c_viviendas*100)
        input() ; os.system('cls')
        opcion = input(f'{mostrarmenu} \nIngresar opcion: ');os.system('cls')
        while opcion < '1' or opcion > '4':
            opcion = input(f'{mostrarmenu} \nIngresar opcion valida: ');os.system('cls')

def proceso():
    global k, acum_h,max_codigo,tot_h,c_viviendas
    acum_h = max = 0
    c_viviendas = int(input('Ingresar cantidad de viviendas: '))
    for k in range(1,c_viviendas):
        codigo = int(input('Ingresar codigo de vivienda: '))
        while codigo < 1 or codigo > 999:
            codigo = int(input('Ingresar codigo de vivienda: '))
        vh = input('¿Vivienda habitada? S/N').upper()
        while vh not in 'SN':
            vh = input('¿Vivienda habitada? S/N: ').upper()
        if vh == 'S':
            habitantes = int(input('Ingresar cantidad de habitantes: '))
            acum_h += habitantes
            tot_h += 1
            if acum_h > max:
                max = acum_h
                max_codigo = tot_h

tot_h = 0
censista = input('Ingresar codigo de cencista: ')
while censista != '0':
    proceso ()
    menu()
    censista = input('Ingresar codigo de cencista: ')
print (f'total general de viviendas habitadas:{tot_h} ') 