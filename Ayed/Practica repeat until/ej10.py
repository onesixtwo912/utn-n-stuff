cheques = max = 0 
saldo = float(input('Ingresar saldo: '))
codigo = input('Ingresar codigo: ').upper()
while codigo not in 'CVF':
	codigo = input('Ingresar codigo: ').upper()
while codigo != 'F':
	importe = float(input('Ingresar importe: '))
	if codigo == 'C':
		if saldo >= importe:
			saldo -= importe
		else:
			print(f'Saldo insuficiente. Dinero faltante: ${importe - saldo}')
			cheques += 1
			saldo = 0
	else:
		saldo += importe
		max = importe if importe > max else 0
	codigo = input('Ingresar codigo: ').upper()
	while codigo not in 'CVF':
		codigo = input('Ingresar codigo: ').upper()
print(f' Saldo: ${saldo} \n Cheques emitidos: {cheques} \n Valor de venta maxima: ${max}')
