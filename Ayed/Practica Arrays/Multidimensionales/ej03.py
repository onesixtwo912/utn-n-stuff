def carga(x):
    for i in range(f):
        for j in range(c):
            x[i][j] = int(input(f'fila {i} columna {j}: '))

def suma(x,y,z):
    for i in range(len(x)):
        for j in range(c):
            z[i][j] = x[i][j] + y[i][j]           
           
def muestra(x):
    for i in range(f):
        for j in range(c):
            print(x[i][j], end=' ')
        print('\n')

f,c = 30,15
a,b,r = [[0]*f for k in range(c)], [[0]*f for k in range(c)], [[0]*f for k in range(c)]
carga(a); muestra(a)
carga(b); muestra(b)
suma(a,b,r)
muestra(r)