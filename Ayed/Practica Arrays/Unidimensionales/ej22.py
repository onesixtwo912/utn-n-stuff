def carga(x,L):
    for i in range(L):
        x[i] = int(input('Ingresar nro: '))

def resultado(x,y):
    for i in range(n+1):
        inicio, fin, flag = 0, m, False
        while not flag and inicio <= fin:
            medio = (inicio + fin) // 2
            if x [medio] == y[i]:
                flag = True
            elif x [medio] > y[i]:
                fin = medio - 1
            else: inicio = medio + 1        
        print(f'{y[i]} se encontro en la posicion {medio}.') if flag else print(f'{y[i]} No se encontro.')         
m, n = 6, 3; V, W = m*[0], n*[0]
carga(V,m)
carga(W,n)
resultado(V,W)