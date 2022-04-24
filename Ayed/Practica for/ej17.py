min = int(input('ingresar numero: '))
max = min
posMax = 1
posMin = 1

for k in range(2,94):
	nro = int(input('ingresar numero: '))
	if nro > max:
		posMax = k
		max = nro
	elif nro < min:
		posMin = k
		min = nro

print(f'valor maximo: {max} posicion: {posMax}')
print(f'valor minimo: {min} posicion: {posMin}')		