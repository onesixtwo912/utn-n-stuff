cont = positivos = negativos = n = 0
for k in range (10):
    nro = int(input('Ingresar un numero: '))
    if nro > 0:
        positivos, cont = positivos + nro , cont + 1
    elif nro < 0:
        negativos = negativos + nro
    else:
        n += 1
print(f'Promedio de los valores positivos {positivos/cont} ')
print (f'La suma de los valores negativos es :{negativos} ')
print(f'cantidad de valores nulos: {n}')