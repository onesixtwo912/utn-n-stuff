def carga(x):
    rta = 'C'
    while rta != 'F':
        com = int(input('comision: '))
        while com < 0 or com > f:
            com = int(input('comision: '))
        edad = int(input('Edad: '))
        x[com][0] += 1
        x[com][1] += edad
        rta = input('C/F: ').upper()
        while rta not in 'CF':
            rta = input('C/F: ').upper()

def listado(x):
    max = 0
    print('Nro. Comision   Cantidad de estudiantes    Promedio de edad \n')
    for i in range (f):
        prom = (x[i][1]) / (x[i][0])
        print(' '*5,i,' '*15,x[i][0],' '*20,prom,'\n')
        if prom >= max:
            max = prom
            maxCom = i
    print(f'Comision con promedio mas alto: {maxCom}; {max}')            

f = 10; c = 2
a = [[0]*c for k in range(f)]
carga(a)
listado(a)