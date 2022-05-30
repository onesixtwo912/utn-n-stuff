n1 = int(input('ingresar nro: '))
n2 = int(input('ingresar nro: '))
n3 = 0
print('columna 1     columna 2')
while n1 != 0:
	if n1 % 2 == 0:
		print(f'   {n1}            {n2}')
	else:
		n3 = n3 + n2
		print(f'   {n1} x         {n2}     {n3}')
	n1 = n1//2
	n2 = n2 * 2		
print(f'   {n1//2}')
