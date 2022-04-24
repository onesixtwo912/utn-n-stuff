max = 0
aux = 0
for k in range(1,94):
	nro = int(input('ingresar numero: '))
	if nro > max:
		aux = k
		max = nro
print(f'valor maximo: {max} posicion: {aux}')		