def carga(x):
    for i in range(n):
        x[i] = int(input('Ingresar nro: '))

def cambio(x,y):
    for i in range(n//2):
        aux = x[i]
        y[i] = x[n-1-i]
        y[n-1-i] = aux

def muestra(x):
    for i in range(n):
        print(x[i])

n = 5; a = b = n*[0]
carga(a)
cambio(a,b)
muestra(b)
cambio(a,a)
muestra(a)