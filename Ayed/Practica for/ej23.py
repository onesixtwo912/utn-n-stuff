horas_tm = 0
horas_tt = 0
for k in range(10):	
	cantE = int(input('ingresar cantidad de empleados: '))
	horas_seccion = 0
	for i in range(cantE):
		horas = float(input('ingresar horas: '))
		turno = (input('ingresar turno: '))
		if (turno == 'm'):
			horas_tm = horas_tm  + horas 
		else:
			horas_tt = horas_tt + horas 
		horas_seccion = horas + horas_seccion		
	print (f'el promedio de horas trabajadas en la seccion {k} es: {horas_seccion/cantE}')
print(f'turno mañana: {horas_tm} turno tarde: {horas_tt}')			
			