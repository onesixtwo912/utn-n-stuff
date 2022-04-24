preciokW = float(input(' ingresar kilowatts: '))
for k in range (1000):
	mesAct = int(input('ingresar mes actual: '))
	mesAnt = int(input('ingresar mes anterior: '))
	consumo = mesAct - mesAnt
	importe = consumo * preciokW
	print (f'precio del kw: {preciokW} consumo del mes: {consumo} importe a abonar: {importe}')
