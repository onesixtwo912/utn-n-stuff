com = input('ingresar comision: ')

while com != '0':
	acum = 0
	cont = 0
	aux = com
	while com == aux:
		nota = int(input('ingresar nota: '))
		cont = cont + 1
		acum = acum + nota
		com = input('ingresar comision: ')
	print (f'Comision: {aux} promedio: {acum/cont}')	