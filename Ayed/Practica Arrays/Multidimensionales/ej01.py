def carga(x):
    for i in range(f):
        print(i)
        for k in range(c):
            x [i][k] = float(input('nro: '))

def suma(x,y):
    suma = 0
    for i in range(c):
        suma += x[y][i]
    return suma        

f, c = 30, 12
a = f*[c*[0]]
carga(a)
nro = int(input('numero de fila a sumar: '))
print(f'La suma es {suma(a,nro)} ')
