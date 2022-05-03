import os
def menu():    
	os.system('cls')
	mostrarmenu = '1 - Cantidad de obras. \n2 - Escuela que presento mas obras. \n3 - Cantidad de obras de cada genero. \n4 - Salir'
	opcion = input(f'{mostrarmenu} \nIngresar opcion: ')	
	while opcion < '1' or opcion > '4':
		os.system('cls')
		opcion = input(f'{mostrarmenu} \nIngresar opcion: ')	
	while opcion != '4':	
		if opcion == '1':
			print(f'Total de obras presentadas: {totalF + totalC + totalP}')
		elif opcion == '2':
			print(f'La escuela {mayorEsc} presento la mayor cantidad de obras.')
		elif opcion == '3':
			print(f'Fabula: {totalF} \nCuento: {totalC} \nPoesia: {totalP}')
		input()	
		os.system('cls')	
		opcion = input(f'{mostrarmenu} \nIngresar opcion: ')	
		while opcion < '1' or opcion > '4':
			opcion = input(f'{mostrarmenu} \nIngresar opcion: ')	

mayor = totalF = totalC = totalP = 0
for escuela in range(1,11):
	cantE = 0
	print(f'Escuela N° {escuela}')
	dni= input('ingresar dni: ')
	while dni != '0':
		genero = input('ingresar genero: ').upper()
		while (genero != 'F') and (genero != 'C') and (genero != 'P'):
			genero = input('ingresar genero: ').upper()
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
menu()
