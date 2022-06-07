import os
def carga(lista):
    for i in range(n):
        lista[i] = int(input(f'Ingresar nro: '))

def calculo(x,y,z):
    for i in range(n):
        z[i] = (x[i] + y [i])

def muestra(lista):
    for i in range(n):
        print(lista [i])

def muestra_listado(x,y,z):
    os.system('cls')
    print(f'\tArray A\t\tArray B\t\tArray C')
    for i in range(n):
        print(f'\t  {x [i]}\t  \t  {y [i]}\t  \t  {z [i]}')

n=2; a,b,c = n*[0], n*[0], n*[0]
carga(a); carga(b); calculo(a,b,c)
muestra(a); muestra(b); muestra(c)
muestra_listado(a,b,c)