totalH = 0
max = 0
dniMax = ' '
dia = input('ingrese dia: ')

while dia != '0':
	cont = 0
	horasD = 0
	aux = dia
	while dia == aux:
		dni = input('ingrese dni: ')
		horas = int(input('ingrese horas trabajadas: '))
		cont = cont + 1
		horasD = horasD + horas
		if horas > max:
			max = horas
			dniMax = dni

		dia = input('Ingrese dia: ')
	print(f'{dniMax} trabajo la mayor cantidad de horas')
	print(f'Promedio de horas trabajadas: {horasD/cont}')
	totalH = totalH + horasD

print(f'Cantidad de horas trabajadas: {totalH}')
