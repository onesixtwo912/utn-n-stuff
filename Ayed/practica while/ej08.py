max = 0 
codigo = input('ingresar codigo de vendedor: ')
while codigo != '0':
	aux = codigo
	acum = 0
	while codigo == aux:
		importe = float(input('ingresar importe: '))
		acum = acum + importe
		codigo = input('ingresar codigo de vendedor: ')
	if acum > max:
		max = acum
		mayorV = aux
	print(f'el vendedor {aux} total vendido: {acum}')
print(f'{mayorV} fue el vendedor con mayor importe vendido: ${max}')		
		
