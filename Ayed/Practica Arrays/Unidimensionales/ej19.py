def inicio(x):
    for i in range(n):
            x[i] = (chr(i+65))

def carga(x):
    codigo = validar('A',chr(n+65),'*') 
    while codigo != '*':
        horas = float(input('horas: '))
        x [ord(codigo)-65] += horas
        codigo = validar('A',chr(n+65),'*')    

def validar(min,max,fin):
    k = input('codigo: ').upper()
    while (k < min or k > max) and k != fin:
        k = input('codigo: ').upper()
    return k

def orden(x,y):
    for i in range(n-1):
        for k in range(i+1,n):
            if x[i] < x[k]:
                aux = x[i]; x[i] = x[k]; x[k] = aux
                aux2 = y[i]; y[i] = y[k]; y[k] = aux2

def muestra (x,y):
    print(f'\tCODIGO DE AVION\t   TIEMPO DE VUELO TOTAL\n')
    for i in range(len(b)):
        print(f'\t\t{y[i]}\t\t  {x[i]}')

n = 12; a,b = n*[0], n*['']
inicio(b), carga(a), orden(a,b), muestra(a,b)
