def carga(x):
    for i in range(n):
        x[i] = int(input('Ingresar nro: '))

def busqueda(x,y):
    inicio, fin, flag = 0, n-1, False
    while not flag and inicio <= fin:
        medio = (inicio + fin) // 2
        if x [medio] == y:
            flag = True
        elif x [medio] > y:
            fin = medio - 1
        else: inicio = medio + 1        
    print(f'Se encontro en la posicion {medio}.') if flag else print('No se encontro.')

n = 5; e = n*[0]
carga(e)
nro = int(input('\nBusqueda \nIngresar nro: '))
busqueda(e,nro)