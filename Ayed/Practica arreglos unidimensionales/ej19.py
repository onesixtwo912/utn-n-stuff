def carga(x):
    codigo = validar('A','L','*')
    while codigo != '*':
        horas = float(input('horas: '))
        pos = busqueda(codigo)
        x [pos] += horas
        codigo = validar('A','L','*')

def busqueda(x):
    i = 0
    while x != b[i] and i < len(b)-1:
        i += 1
    return i        

def validar(min,max,y):
    k = input('codigo: ').upper()
    while not (k >= min and k <= max or k == y):
        k = input('codigo: ').upper()
    return k

def orden(x,y):
    for i in range(len(b)-1):
        for k in range(i+1,len(b)):
            if x[i] < x[k]:
                aux = x[i]; x[i] = x[k]; x[k] = aux
                aux2 = y[i]; y[i] = y[k]; y[k] = aux2

def muestra (x,y):
    print(f'\tCODIGO DE AVION\t   TIEMPO DE VUELO')
    for i in range(len(b)):
        print(f'\t\t{y[i]}\t\t{x[i]}')

a,b = 12*[0], ['A','B','C','D','E','F','G','H','I','J','K','L']
carga(a), orden(a,b), muestra(a,b)
