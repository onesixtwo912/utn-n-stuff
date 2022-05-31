cod_planta = input('Ingresar codigo de planta: ')
while cod_planta != '*':
    aux = cod_planta
    while aux == cod_planta:
        contOp = 0
        horasTotal = 0
        cod_secc = input('Ingresar codigo de seccion: ')
        auxS = cod_secc
        while cod_secc == auxS and aux == cod_planta:
            horas = int(input('Ingresar horas: '))
            horasTotal = horasTotal + horas
            contOp = contOp + 1
            cod_planta = input('Ingresar codigo de planta: ')
            if cod_planta != '*':
                cod_Secc = input('Ingresar codigo de seccion: ')
    print(f'Planta {aux} Seccion {auxS}: \n Cantidad de operarios {contOp} \n Cantidad de horas trabajadas {horasTotal}')              
