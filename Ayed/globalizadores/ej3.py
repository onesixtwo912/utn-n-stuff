n = int(input('ingresar nro: '))
for i in range(0,n+1):
	aux = i
	for k in range(1,i):
		aux = aux * k
	print(f'!{i}: {aux}')