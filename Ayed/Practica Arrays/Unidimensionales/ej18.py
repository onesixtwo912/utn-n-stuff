def carga(x):
    for i in range(n):
        x[i] = int(input(f'Ingresar nro: '))

def muestra(x):
    for i in range(n):
        print(x [i])         

def orden(x):
    for i in range(n-1):
        for k in range (i+1,n):
            if x[i] > x[k]:
                aux = x[i] 
                x[i] = x[k]
                x[k] = aux

n = 25; a = n*[0]
carga(a)
muestra(a)
orden(a)
muestra(a)