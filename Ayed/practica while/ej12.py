mayorCat = 0
cat = int(input('ingresar categoria: '))

while (cat >= 1) and (cat <= 20):
	aux = cat 
	mayorKm = 0
	while cat == aux:
		auto = input('ingresar auto: ')
		km = float('ingresar kilometraje: ') 
		monto = float('ingresar monto: ')
		if monto > mayorCat:
			mayorCat = cat 
		mayorKm = mayorKm + km 
		cat = int(input('ingresar categoria: '))
	print(f'La categoria {aux} recorrio: {mayorKm}')	
print(f'La categoria {mayorCat} realizo el viaje con mayor monto')