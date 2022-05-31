cont = 0
a = 52000000
b = 85000000
while a < b:
	a = a * 0.06
	b = b * 0.04
	cont = cont + 1
print(f'A tardará {cont} años en superar a la poblacion de B')
