import os
def cambio(x,y):
    for i in range(len(x)):
        if x[i] != '.':
            for k in range(i):
                y[i] += 
        else: y[i] += x[i]          
def muestra(x):
    print (f'Texto de {len(x)} caracteres.')
    for i in range(len(x)):
        print(x[i])

texto = input('Ingresar texto: ')
a = len(texto)*['']
muestra(texto,a)