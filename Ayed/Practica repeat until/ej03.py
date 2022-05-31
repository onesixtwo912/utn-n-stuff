print('f(x) = 3 * x + 2' )
fx = float(input('Ingresar un valor para x: '))
aux = fx + 1
while aux != fx:
	aux = fx
	y = 3 * fx + 2
	print (f'f({fx}) = {y}')
	fx = float(input('Ingresar un valor para x: '))
