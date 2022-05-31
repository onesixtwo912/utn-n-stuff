for k in range(1,51):
	max = 0
	importe = float(input('Ingresar importe: '))
	while importe != 0:
		if importe > max:
			max = importe
		importe = float(input('Ingresar importe: '))
	print(f'Viajante N°: {k}; Maximo importe: {max}')		

