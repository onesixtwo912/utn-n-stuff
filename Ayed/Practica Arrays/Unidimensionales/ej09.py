def carga(x):
    for i in range(n):
        x[i] = (int(input(f'Ingresar nro: ')))  

def calculo(x,y):
    for i in range(n-1):
        y [i] = x [i+1] - x [i]

def muestra(x):
    for i in range(n-1):
        print(x [i])    

n = 50 ; X,DX = n*[0], (n-1)*[0]
carga(X)
calculo(X,DX)
muestra(DX)
calculo(X,X)
muestra(X)