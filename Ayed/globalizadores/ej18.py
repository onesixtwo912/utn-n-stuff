max, max_dia = 0 , ''
dia = input('Ingresar dia: ')
while dia != '0':
    aux = dia; cont_pacientes = acum_edad = 0
    while aux == dia:
        edad = int(input('Ingresar edad: '))
        cont_pacientes += 1
        acum_edad += edad
        dia = input('Ingresar dia: ')
    print(f'Promedio de edad {acum_edad/cont_pacientes} ')
    if cont_pacientes > max:      
        max, max_dia = cont_pacientes, aux
print (f'En el dia {max_dia} se registro la mayor cantidad de pacientes.')