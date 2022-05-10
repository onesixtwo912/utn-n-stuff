import os
def menu():    
    os.system('cls')
    mostrarmenu = '1 - Grupo con mas puntos. \n2 - Porcentaje... \n3 - Cantidad de grupos que obtuvieron 10. \n4 - Salir'
    opcion = input(f'{mostrarmenu} \nIngresar opcion: '); os.system('cls')
    while opcion < '1' or opcion > '4':
        opcion = input(f'{mostrarmenu} \nIngresar opcion: '); os.system('cls')	
    while opcion != '4':
        if opcion == '1':
            print(aux_grupo)
        elif opcion == '2':
            print(f'{total_t/total_comp*100}%')
        elif opcion == '3':
            print(cantidad_10)
        input(); os.system('cls')
        opcion = input(f'{mostrarmenu} \nIngresar opcion: '); os.system('cls')	
        while opcion < '1' or opcion > '4':
            opcion = input(f'{mostrarmenu} \nIngresar opcion: '); os.system('cls')

total_t = cantidad_10 = total_comp = maxPuntos = 0
nombre_grupo = input('ingresar nombre de grupo: ')
while nombre_grupo != '*':
    acum_resultado = vuelta = 0; r10 = False
    tipo = input('ingresar tipo de competencia: ').upper()
    while tipo != 'T' and tipo != 'E' and tipo != 'M' and tipo != '*':
        tipo = input('ingresar tipo de competencia: ').upper()
    while vuelta < 3 and tipo != '*':
        total_t = total_t + 1 if tipo == 'T' else 0    
        total_comp = total_comp + 1 
        resultado = int(input('ingresar resultado: '))
        while resultado < 1 or resultado > 10:
            resultado = int(input('ingresar resultado: '))       
        if not r10 and resultado == 10:
            cantidad_10 = cantidad_10 + 1
            r10 = True
        acum_resultado = acum_resultado + resultado
        vuelta = vuelta + 1
        if vuelta < 3:
            tipo = input('ingresar tipo de competencia: ').upper()
            while tipo != 'T' and tipo != 'E' and tipo != 'M' and tipo != '*':
                tipo = input('ingresar tipo de competencia: ').upper()
    aux_grupo, maxPuntos = nombre_grupo, acum_resultado if acum_resultado > maxPuntos else 0   
    print(f'{nombre_grupo} se presento en todas las competencias.') if vuelta == 3 else print(f'{nombre_grupo} no se presento en todas las competencias.')
    nombre_grupo = input('ingresar nombre de grupo: ')
menu()
