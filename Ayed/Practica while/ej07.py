for k in range(ord('A'),ord('H')+1):	
	acum = 0
	importe = float(input(f'ingresar importe del vendedor {chr(k)}: '))
	while importe != 0:
		acum += importe
		importe = float(input('ingresar importe: '))
	print(f'Al vendedor {chr(k)} le corresponde como comision ${acum*0.025}')
