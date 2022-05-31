cont = contD = 0
importe = float(input('ingresar importe: '))
while importe != 0:
	cont += 1
	if importe > 85:
		impB *= 0.05
		contD += 1
		print ('importe bonificado: ',impB)
	else:
		print ('importe: ',importe)
	importe = float(input('ingresar importe: '))
print(f'un {contD*100/cont}% de {cont} ventas tuvieron descuentos')	