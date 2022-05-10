import os
def menu():    
    os.system('cls')
    mostrarmenu = '1 - Grupo con mas puntos. \n2 - Porcentaje... \n3 - Cantidad de grupos que obtuvieron 10. \n4 - Salir'
    opcion = input(f'{mostrarmenu} \nIngresar opcion: ')	
    while opcion < '1' or opcion > '4':
        os.system('cls')
        opcion = input(f'{mostrarmenu} \nIngresar opcion: ')	
    while opcion != '4':
        if opcion == '1':
            print(aux_grupo)
        elif opcion == '2':
            print(f'{total_t/total_comp*100}%')
        elif opcion == '3':
            print(cantidad_10)
        input()
        os.system('cls')
        opcion = input(f'{mostrarmenu} \nIngresar opcion: ')	
        while opcion < '1' or opcion > '4':
            os.system('cls')
            opcion = input(f'{mostrarmenu} \nIngresar opcion: ')

total_t = cantidad_10 = total_comp = maxPuntos = 0
nombre_grupo = input('ingresar nombre de grupo: ')
while nombre_grupo != '*':
    acum_resultado = 0
    vuelta = 0
    r10 = False
    tipo = input('ingresar tipo de competencia: ')
    while tipo != 'T' and tipo != 'E' and tipo != 'M' and tipo != '*': # tipo = '*' indica el fin de datos en vez de preguntar si continua o no(como pide el enunciado)
        tipo = input('ingresar tipo de competencia: ') 
    while vuelta < 3 and tipo != '*':        
        if tipo == 'T':
            total_t = total_t + 1
        total_comp = total_comp + 1 
        resultado = int(input('ingresar resultado: '))
        while   resultado <= 1 and resultado >= 10:
               resultado = int(input('ingresar resultado: '))       
        if not r10 and resultado == 10:
            cantidad_10 = cantidad_10 + 1
            r10 = True
        acum_resultado = acum_resultado + resultado
        vuelta = vuelta + 1
        tipo = input('ingresar otro tipo de competencia: ')
        while tipo != 'T' and tipo != 'E' and tipo != 'M' and tipo != '*':
            tipo = input('ingresar otro tipo de competencia: ')
    if acum_resultado > maxPuntos:
        aux_grupo = nombre_grupo
        maxPuntos = acum_resultado
    if vuelta == 3:
        print(f'{nombre_grupo} se presento en todas las competencias.')
    else:
        print(f'{nombre_grupo} no se presento en todas las competencias.')
    nombre_grupo = input('ingresar nombre de grupo: ')
menu()
