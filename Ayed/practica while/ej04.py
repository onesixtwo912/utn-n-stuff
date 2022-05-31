aux = 0
vendedor = (input('ingresar vendedor: '))
while vendedor != '*':
	importe = float(input('ingresar importe: '))
	if importe > aux:
		vMayor = vendedor 
		iMayor = importe
	vendedor = (input('ingresar vendedor: '))
print(f'el vendedor {vMayor} obtuvo la venta con mayor importe : ${iMayor}')		