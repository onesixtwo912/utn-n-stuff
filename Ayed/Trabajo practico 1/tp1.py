import os
def leerOp(x,menuop):
    global op ; os.system('cls')
    if x == 1: 
        k = 'Menu Principal \n\n 1 - Administracion. \n 2 - Entrega de cupos. \n 3 - Recepcion. \n 4 - Registrar calidad. \n 5 - Registrar peso bruto. \n 6 - Registrar descarga. \n 7 - Registrar tara. \n 8 - Reportes. \n 0 - Salir.'
    elif x == 2:
         k = 'Menu de administracion \n\n A - Titulares. \n B - Productos. \n C - Rubros \n D - Rubros por producto.  \n E - Silos.  \n F - Sucursales. \n G - Producto por titular. \n V - Volver al menu principal.'
    else: 
        k = 'Menu de titulares \n\n A - Alta. \n B - Baja. \n C - Consulta. \n M - Modificacion. \n V - Volver al menu anterior.'
    op = input(f'{k}\n\n Seleccione una opcion: ').upper() ; os.system('cls')
    while op not in menuop:
        op = input(f'{k}\n\n Seleccione una opcion valida: ').upper() ; os.system('cls')

def ingresoNro(i):
    y = input(f'Ingresar {i}: ')
    while not y.isdigit() or float(y) < 0: 
        y = input(f'Ingresar {i}: ')
    y = float(y) ; return y

def mensaje():
    print('Esta funcionalidad esta en construcción.');input()

def administraciones():
    leerOp(2,'ABCDEFGV')
    while op != 'V':
        titulares() if op == 'A' else mensaje() if op >= 'B' and op <= 'G' else 0
        leerOp(2,'ABCDEFGV')

def titulares():
    leerOp(3,'ABCMV')
    while op != 'V':
        mensaje() if   op >= 'A' and op <= 'C' or op == 'M' else 0
        leerOp(3,'ABCMV')

def recepcion():
    global patente,producto,pesoNeto,camionM,pesoM,patenteMin,camionS,pesoS,max,min,patenteMax,pesoBruto,tara
    patente = input('Ingresar patente: ')
    while patente != '*':
        producto = input('Ingresar producto: ').upper()
        while producto != 'S' and producto != 'M':
            producto = input('Ingresar producto: ').upper()
        pesoBruto = ingresoNro('peso bruto'); tara = ingresoNro('tara')
        pesoNeto = pesoBruto - tara ; print(f'El peso neto es {pesoNeto}'); input(); os.system('cls')
        if producto == 'S':
            camionS = camionS + 1 ; pesoS = pesoS + pesoNeto
            if pesoNeto > max:
                patenteMax = patente ; max = pesoNeto
        else:
            camionM = camionM + 1 ; pesoM = pesoM + pesoNeto
            if camionM == 1 or pesoNeto < min:
                patenteMin = patente ; min = pesoNeto
        patente = input('Ingresar patente: ')

def reportes():
    if camionS > 0 and camionM > 0:
        print(f'Reporte: \n\n Cantidad total de camiones: {camionS + camionM} \n Total de camiones de soja: {camionS} \n Total de camiones de maíz: {camionM}')
        print(f' Peso neto total de soja: {pesoS} Kgs \n Peso neto total de maíz: {pesoM} Kgs')
        print(f' Promedio del peso neto de soja por camión: {pesoS/camionS} Kgs\n Promedio del peso neto de maíz por camión: {pesoM/camionM} Kgs')
        print(f' Patente del camión de soja que mayor cantidad descargo: {patenteMax} \n Patente del camión de maíz que menor cantidad descargo: {patenteMin}');input()        
    else:
        print('Todavia no se cargaron datos.');input()

max = camionS = camionM = pesoS = pesoM = 0
leerOp(1,'012345678')
while op != '0':
    if op == '1': 
        administraciones()
    elif op == '2' or op >= '4' and op <= '7': 
        mensaje()
    elif op == '3': 
        recepcion()
    elif op == '8': 
        reportes()
    leerOp(1,'012345678')
