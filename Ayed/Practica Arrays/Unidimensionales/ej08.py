def muestra(x):
    print (f'Texto de {len(x)} caracteres.')
    for i in range(len(x)):   
        print(x[i], end='' '\n') if texto [i] == '.' else print(x[i], end='')            

texto = input('Ingresar texto: ')
muestra(texto)
