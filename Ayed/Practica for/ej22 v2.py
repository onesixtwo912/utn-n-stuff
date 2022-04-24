cont = 0 
letra = input('Ingresar letra: ')
for k in range(1,190):
	aux = letra
	letra = input('Ingresar letra: ')	
	if aux == 'p' and letra == 'a':
		cont = cont + 1
print(f'La silaba "pa" se repite:{cont} veces')	