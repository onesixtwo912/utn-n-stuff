def carga(lista):
    for i in range(n):
        lista[i] = (int(input(f'Ingresar nro: ')))   

def suma(lista):
    acum = 0
    for i in range(n):
        acum += lista[i] if lista[i] > 0 else 0
    return acum

n = 5; AN = n*[0]
carga(AN); suma(AN)
print(f'{suma(AN)}')