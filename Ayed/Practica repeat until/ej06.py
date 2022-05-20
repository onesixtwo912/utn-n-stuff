pos = 1
n = int(input('Cantidad de numeros: '))
nro = int(input('Ingresar numero: '))
while nro > 0 and pos != n:
    pos += 1
    nro = int(input('Ingresar numero: '))
print(f'El primer valor negativo se encontro en la posicion {pos} ') if nro < 0 else print('No se encontraron valores negativos.')