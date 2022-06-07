def carga(lista):
    for i in range(n):
        lista[i] = int(input(f'Ingresar nro: '))

def cambio(lista):
    k = lista[n-1] % 2
    for i in range(n):
        if lista[i] % 2 == k:
            lista[i] = 0
        
def muestra(lista):
    for i in range(n):
        print(lista[i])

n = 10; a= n*[0] 
carga(a)
cambio(a)
muestra(a)