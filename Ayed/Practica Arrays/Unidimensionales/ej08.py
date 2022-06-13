def muestra(x):
    print (f'Texto de {len(x)} caracteres.')
    for i in range(len(x)):
        if texto [i] == '.':
            print(x[i], end='' '\n')
        else: 
            print(x[i], end='')            

texto = input('Ingresar texto: ')
muestra(texto)