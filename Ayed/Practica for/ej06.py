acum = 0
cantM = int(input('ingresar cantidad de materias: '))
for k in range(cantM):
	nota = float(input('ingresar nota: '))
	acum = acum + nota
print (f'promedio: {acum/cantM}')	

