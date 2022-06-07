def carga(x):
    for i in range (n):
        pos = int(input('nro de coche: '))
        while pos < 1 or pos > n:
            pos = int(input('nro de coche: '))
        importe = float(input('importe: '))
        while importe > 0:
            x[pos-1] += importe
            importe = float(input('importe: '))
            
def muestra(x):
    print ('\tN° de coche  Costo del viaje')
    for i in range(n):
        print(f'\t    {i+1} \t\t{x[i]}')
        
n = 2 ; total = (n)*[0]
carga(total)
muestra(total)