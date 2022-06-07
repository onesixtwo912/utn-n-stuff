def carga(x):
    for i in range(n):
        x[i] = (int(input(f'Ingresar nro: ')))  

def busqueda(x,y):
    pos = 0
    while y != x[pos] and pos < n-1:
        pos += 1
    print(f'Se encontro en la posicion {pos} ') if y == x[pos] else print('No se encontro.')

n = 3; e = n*[0]
carga(e)
nro = int(input('Ingresar nro: '))
busqueda(e,nro)