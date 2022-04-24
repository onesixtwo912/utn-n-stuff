for k in range(55):
	acum = 0 
	for y in range(6):
		nota = float(input('ingresar nota: '))
		acum = nota + acum	
	print (f'El promedio es: {acum/6}')
	