nro = int(input('Ingresar cantidad de valores a evaluar: '))
print('f(x) = 3 * x + 2' )
cont = 0
while cont != nro:
	x = float(input('Ingresar un valor para x: '))
	fx = 3 * x + 2
	cont += 1
	print (f'f({x}) = {fx}')
