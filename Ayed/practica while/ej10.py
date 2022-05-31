com = input('ingresar comision: ')

while com != '0':
	acum = cont = 0
	aux = com
	while com == aux:
		nota = int(input('ingresar nota: '))
		cont += 1
		acum += nota
		com = input('ingresar comision: ')
	print (f'Comision: {aux} promedio: {acum/cont}')	