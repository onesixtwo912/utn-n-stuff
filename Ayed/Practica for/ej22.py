cont = 0 
texto = input('Ingresar texto: ')
for k in range(len(texto)-1):	
	if texto[k] == 'p' and texto[k+1] == 'a':
		cont = cont + 1
print(f'La silaba "pa" se repite:{cont} veces')	