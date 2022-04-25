cont = 0
contD = 0
importe = float(input('ingresar importe: '))
while importe != 0:
	cont = cont + 1
	if importe > 85:
		impB = importe * 0.05
		contD = contD + 1
		print ('importe bonificado: ',impB)
	else:
		print ('importe: ',importe)
	importe = float(input('ingresar importe: '))
print(f'un {contD*100/cont}% de {cont} ventas tuvieron descuentos')	