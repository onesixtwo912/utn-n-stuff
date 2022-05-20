print('f(x) = 3 * x + 2' )
rta = 'C'
while rta != 'F':
	x = float(input('ingresar un valor para x: '))
	fx = 3 * x + 2
	print (f'f({x}) = {fx}')
	rta = input('C/F: ')
	while rta not in 'CF':
		rta = input('C/F: ')