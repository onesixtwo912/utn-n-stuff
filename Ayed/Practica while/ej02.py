ventas = cont = acum = 0
importe = float(input('ingresar importe: '))
while importe != 0:
	ventas += 1 
	acum = acum + importe
	if importe > 30:
		cont += 1
	importe = float(input('ingresar importe: '))	
print (f'Se realizaron  {ventas} ventas')
print(f'{cont} ventas superan los $30')
print (f'Promedio de ventas: {acum/ventas}')		