contF = 0
contM = 0
acumE = 0
acumC = 0
cantSoc = int(input('ingresar cantidad de socios: '))
for k in range(cantSoc):
	nroS = input('ingresar numero de socio: ')
	edad = int(input('ingresar edad: '))
	sexo = input('ingresar sexo: ')
	importe = float(input('ingresar importe: '))
	acumE = acumE + edad
	acumC = acumC + importe
	if sexo == 'm':
		contM = contM + 1
	else:
		contF = contF + 1
print (f'Hombres: {contM} Mujeres: {contF}')
print(f'El promedio de edad de los socios es: {acumE/cantSoc}')
print(f'Total recaudado: {acumC}')		

		
