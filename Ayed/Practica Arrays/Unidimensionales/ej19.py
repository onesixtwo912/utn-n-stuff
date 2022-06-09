def inicio(x):
    for i in range(12):
            x[i] = (chr(i+65))

def carga(x):
    codigo = validar('A','L','*')
    while codigo != '*':
        horas = float(input('horas: '))
        x [ord(codigo)-65] += horas
        codigo = validar('A','L','*')    

def validar(min,max,y):
    k = input('codigo: ').upper()
    while not (k >= min and k <= max or k == y):
        k = input('codigo: ').upper()
    return k

def orden(x,y):
    for i in range(len(y)-1):
        for k in range(i+1,len(y)):
            if x[i] < x[k]:
                aux = x[i]; x[i] = x[k]; x[k] = aux
                aux2 = y[i]; y[i] = y[k]; y[k] = aux2

def muestra (x,y):
    print(f'\tCODIGO DE AVION\t   TIEMPO DE VUELO\n')
    for i in range(len(b)):
        print(f'\t\t{y[i]}\t\t{x[i]}')

a,b = 12*[0], 12*['']
inicio(b), carga(a), orden(a,b), muestra(a,b)
