letra = input('ingresar letra: ')
while letra != '*':
	cont = 0
	aux = letra 
	while letra == aux:
		cont = cont + 1
		letra = input('ingresar letra: ')
	print(f'La letra {aux} se ingreso {cont} veces') 	