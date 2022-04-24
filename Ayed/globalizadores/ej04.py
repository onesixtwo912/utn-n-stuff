silaba = input('ingresar silaba: ')
texto = input('ingresar texto: ')
k = 0
cont = 0
while texto[k] != '.':
	if texto[k] == silaba[0] and texto[k+1] == silaba[1]:
		cont = cont + 1
	k = k + 1
print(f'la silaba {silaba} se ingreso {cont} veces')	
