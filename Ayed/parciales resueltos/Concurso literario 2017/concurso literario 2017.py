import os
mayor = 0
totalF = 0
totalC = 0import os
mayor = 0
totalF = 0
totalC = 0
totalP = 0

for escuela in range(11):
	cantE = 0
	print('nro ',escuela)
	dni= input('ingresar dni: ')
	while dni != '0':
		genero = input('ingresar genero: ')
		while (genero != 'F') and (genero != 'C') and (genero != 'P'):
			genero = input('ingresar genero: ')
		if genero == 'F':
			totalF = totalF + 1
		elif genero == 'C':
			totalC = totalC + 1
		elif genero == 'P':
			totalP = totalP + 1
		cantE = cantE + 1	
		
		dni= input('ingresar dni: ')	

	if cantE > mayor:
		cantE = mayor
		mayorEsc = escuela

os.system('cls')
print('1 - Cantidad de obras. ')
print('2 - Escuela que presento mas obras. ')
print('3 - Cantidad de obras de cada genero. ')
print('4 - Salir. ')
opcion = input('ingresar opcion: ')
while opcion < '1' or opcion > '4':
	opcion = input('ingresar opcion: ')
	os.system('cls')

while opcion != '4':	
	if opcion == '1':
		print(f'Total de obras presentadas: {totalF + totalC + totalP}')
	elif opcion == '2':
		print(f'La escuela {mayorEsc} presento la mayor cantidad de obras.')
	elif opcion == '3':
		print(f'Fabula: {totalF} \nCuento: {totalC} \nPoesia: {totalP}')
	input()	
	os.system('cls')	
	print('1 - Cantidad de obras. ')
	print('2 - Escuela que presento mas obras. ')
	print('3 - Cantidad de obras de cada genero. ')
	print('4 - salir. ') 	
	opcion = input('ingresar opcion:')
	while opcion < '1' or opcion > '4':
		opcion = input('ingresar opcion:')
totalP = 0

for escuela in range(11):
	cantE = 0
	print('nro ',escuela)
	dni= input('ingresar dni: ')
	while dni != '0':
		genero = input('ingresar genero: ')
		while (genero != 'F') and (genero != 'C') and (genero != 'P'):
			genero = input('ingresar genero: ')
		if genero == 'F':
			totalF = totalF + 1
		elif genero == 'C':
			totalC = totalC + 1
		elif genero == 'P':
			totalP = totalP + 1
		cantE = cantE + 1	
		
		dni= input('ingresar dni: ')	

	if cantE > mayor:
		cantE = mayor
		mayorEsc = escuela

os.system('cls')
print('1 - Cantidad de obras. ')
print('2 - Escuela que presento mas obras. ')
print('3 - Cantidad de obras de cada genero. ')
print('4 - Salir. ')
opcion = input('ingresar opcion: ')
while opcion < '1' or opcion > '4':
	opcion = input('ingresar opcion: ')
	os.system('cls')

while opcion != '4':	
	if opcion == '1':
		print(f'Total de obras presentadas: {totalF + totalC + totalP}')
	elif opcion == '2':
		print(f'La escuela {mayorEsc} presento la mayor cantidad de obras.')
	elif opcion == '3':
		print(f'Fabula: {totalF} \nCuento: {totalC} \nPoesia: {totalP}')
	input()	
	os.system('cls')	
	print('1 - Cantidad de obras. ')
	print('2 - Escuela que presento mas obras. ')
	print('3 - Cantidad de obras de cada genero. ')
	print('4 - salir. ') 	
	opcion = input('ingresar opcion:')
	while opcion < '1' or opcion > '4':
		opcion = input('ingresar opcion:')
