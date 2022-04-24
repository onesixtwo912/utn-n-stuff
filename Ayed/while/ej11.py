totalH = 0
mayor = 0
dia = (int(input('ingrese dia: ')))

while dia != 0:
	cont = 0
	horasD = 0
	aux = dia
	while dia == aux:
		dni = input('ingrese dni: ')
		horas = int(input('ingrese horas trabajadas: '))
		cont = cont + 1
		horasD = horasD + horas
		if horas > mayor:
			dnimax = dni

		dia = (int(input('Ingrese dia: ')))	
	print(f'{dnimax} trabajo la mayor cantidad de horas')
	print(f'promedio de horas trabajadas: {horasD/cont}')
	totalH = totalH + horasD

print(f'Cantidad de horas trabajadas: {totalH}')		

