max = 0
n = int(input('N° de vueltas: '))
nro = int(input('ingresar nro: '))
for i in range(n-1):
	ant = nro
	nro = int(input('ingresar nro: '))
	if (nro - ant) > max:
		max = nro - ant
print(f'La maxima diferencia es de: {max}')		