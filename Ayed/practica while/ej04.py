aux = 0
vend = (input('ingresar vendedor: '))
while vend != '*':
	importe = float(input('ingresar importe: '))
	if importe > aux:
		vMayor = vend
		iMayor = importe
	vend = (input('ingresar vendedor: '))
print(f'el vendedor {vMayor} obtuvo la venta con mayor importe : ${iMayor}')		