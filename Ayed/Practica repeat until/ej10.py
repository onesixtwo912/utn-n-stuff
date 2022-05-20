cheques = max = 0 
saldo = float(input('Ingresar saldo: '))
def leer_cod():
	global codigo
	codigo = input('Ingresar codigo: ').upper()
	while codigo not in 'CVF':
		codigo = input('Ingresar codigo: ').upper()
leer_cod()
while codigo != 'F':
	importe = float(input('Ingresar importe: '))
	if codigo == 'C':
		if saldo >= importe:
			saldo = saldo - importe
		else:
			print(f'Saldo insuficiente. Valor faltante:{importe -saldo}')
			cheques = cheques + 1
	else:
		saldo = saldo + importe 
		max = importe if importe > max else 0
	leer_cod()		
print(f' Saldo: {saldo} \n Cheques emitidos: {cheques} \n Valor de venta maxima: {max}')