import math
n1 = int(input('ingresar nro: '))
n2 = int(input('ingresar nro: '))
#n1 = 40
#n2 = 10
n3 = 0
while n1 != 0:
	if n1 % 2 == 0:
		print(f'{n1}         {n2}')
	else:
		n3 = n3 + n2
		print(f'{n1}x       {n2}  {n3}')
	n1 = math.floor(n1/2)
	n2 = n2 * 2		
print(f'{math.floor(n1/2)}')#,'        ', n2)		