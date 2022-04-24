cont = 0
acum = 0
for k in range(200):
	importe = float(input('ingresar importe: '))
	if importe >= 100:
		acum = acum + importe
	else:
		cont = cont + 1
print (f'El monto total de las ventas mayor o igual que $ 100 es: {acum}')
print (f'{cont} ventas fueron menor a $100')		