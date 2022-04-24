legajo = int(input('ingresar legajo: '))
while legajo != 0:
	a = 0
	for p in range(5):
		nota = float(input('ingresar nota: '))
		if nota > 5:
			a = a + 1
	if a >= 4:
		print('Regular')
	elif a == 3:
		print('A recuperatorio')
	elif a < 3:
		print('A recursar')
	legajo = input('ingresar legajo: ')		
