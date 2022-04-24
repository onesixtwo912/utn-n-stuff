acum = 0
for k in range(304):
	legajo = input('ingresar legajo: ')
	cms = float(input('ingresar estatura : '))
	acum = acum + cms
	if cms < 165:
		print(legajo)
print(f'promedio: {acum/k} cms')	