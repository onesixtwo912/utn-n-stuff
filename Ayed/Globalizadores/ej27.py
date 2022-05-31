total = 0
c = int(input('Ingresar cantidad de comisiones: '))
for k in range(c):
    cT = cM = 0
    for com in range(35):
        legajo = input('Ingresar legajo: ')
        nota = int(input('Ingresar nota: '))
        total = total + nota
        turno = input('Ingresar turno: ')
        while turno != 'M' and turno != 'T':
            turno = input('Ingresar turno: ')
        if turno == 'M':
            cM = cM + 1
        else:
            cT = cT + 1
    print(f'Comision {com}: Turno mañana: {cM}; Turno tarde: {cT} ') 
print (f'Promedio total de notas de primer año: {total/35*com}')