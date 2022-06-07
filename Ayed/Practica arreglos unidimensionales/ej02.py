def carga(lista):
    for i in range(n):
        lista[i] = (float(input(f'Ingresar nro: ')))        

def suma(lista):
    acum = 0
    for i in range(n):
        acum += lista[i]
    return acum

n = 4 ; A = n*[0]
carga(A); suma(A)
print (f'Total: {suma(A)}')