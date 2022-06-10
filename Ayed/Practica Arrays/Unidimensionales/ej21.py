def inicio(x,y):
    for i in range(n):
        y[i] = 0
        x[i] = int(input('codigo de colectivo: '))
        while (x[i] < min or x[i] > max) and x[i] != 0:
            x[i] = int(input('codigo de colectivo: '))

def carga(x,y):
    cod = validar(x)
    while cod != 0:
        pos = busquedaPos(x,cod)
        cant_b = int(input('Cantidad de boletos: '))
        y[pos] += cant_b
        cod = validar(x)

def validar(x):
    cod = int(input('codigo de colectivo: '))
    while cod not in x and cod != 0:
        cod = int(input('codigo de colectivo: '))
    return cod

def busquedaPos(x,k):
    i = 0
    while k != x[i] and i < n-1:
        i += 1
    pos = i if k == x[i] else 0
    return pos

def muestra(x,y):
    print(f'\tCODIGO DE COLECTIVO \t  CANTIDAD DE BOLETOS\n')
    for i in range(n):
        print(f'\t\t{x[i]}\t\t\t  {y[i]}')     

n = 25; codigo, boletos = n*[0], n*[0]
inicio(codigo,boletos)
carga(codigo,boletos)
muestra(codigo,boletos)