cont = 0
nro = int(input('ingresar un numero: '))
while nro != 0:
	if nro >= 100:
		cont += 1
	nro = int(input('ingresar un numero: '))	
print (f'Hay {cont} numeros mayores o iguales a 100')