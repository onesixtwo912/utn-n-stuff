def carga(x):
    for i in range(f):
        for j in range(c):
            x[i][j] = float(input(f'fila {i} columna {j}: '))

def suma(x,y):
    suma = 0
    for i in range(c):
        suma += x[y][i]
    return suma        

f, c = 2, 2
a = [[0]*f for k in range(c)]
carga(a)
nro = int(input('numero de fila a sumar: '))
print(f'La suma es {suma(a,nro)} ')
