max = 0
cat = int(input('ingresar categoria: '))

while (cat >= 1) and (cat <= 20):
	aux = cat 
	totalKm = 0
	while cat == aux:
		auto = input('ingresar auto: ')
		km = float('ingresar kilometraje: ') 
		monto = float('ingresar monto: ')
		totalKm = totalKm + km 
		if monto > max:
			mayorCat = cat
			max = monto
		cat = int(input('ingresar categoria: '))
	print(f'La categoria {aux} recorrio: {totalKm}')	
print(f'La categoria {mayorCat} realizo el viaje con mayor monto')
