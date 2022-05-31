totalH = max = 0
dniMax = ' '
dia = input('ingrese dia: ')

while dia != '0':
	cont = horasD = 0
	aux = dia
	while dia == aux:
		dni = input('ingrese dni: ')
		horas = int(input('ingrese horas trabajadas: '))
		cont += 1
		horasD += horas
		if horas > max:
			max = horas
			dniMax = dni

		dia = input('Ingrese dia: ')
	print(f'{dniMax} trabajo la mayor cantidad de horas')
	print(f'Promedio de horas trabajadas: {horasD/cont}')
	totalH += horasD

print(f'Cantidad de horas trabajadas: {totalH}')