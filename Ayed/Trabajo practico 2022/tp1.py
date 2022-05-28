import os
def valido_ingreso(x,valores_validos,i):
    os.system('cls')
    if x == 1: k = 'Menu Principal \n\n 1 - Administracion. \n 2 - Entrega de cupos. \n 3 - Recepcion. \n 4 - Registrar calidad. \n 5 - Registrar peso bruto. \n 6 - Registrar descarga. \n 7 - Registrar tara. \n 8 - Reportes. \n 0 - Salir.\n\n '
    elif x == 2: k = 'Menu de administracion \n\n A - Titulares. \n B - Productos. \n C - Rubros \n D - Rubros por producto.  \n E - Silos.  \n F - Sucursales. \n G - Producto por titular. \n V - Volver al menu principal.\n\n '
    elif x == 3: k = 'Menu de titulares \n\n A - Alta. \n B - Baja. \n C - Consulta. \n M - Modificacion. \n V - Volver al menu anterior.\n\n '
    else: k = ''
    y = input(f'{k}Ingresar {i}: ').upper() ; os.system('cls')
    while y not in valores_validos:
        y = input(f'{k}Ingresar {i}: ').upper() ; os.system('cls')
    return y

def ingresoNro(i):
    y = input(f'Ingresar {i}: ')
    while not y.isdigit() or float(y) < 0: 
        y = input(f'Ingresar {i}: ')
    return float(y)

def mensaje():
    print('Esta funcionalidad esta en construcción.'); input()

def administraciones():
    op = valido_ingreso(2,'ABCDEFGV','opcion')
    while op != 'V':
        titulares() if op == 'A' else mensaje() if op in 'BCDEFGV' else 0
        op = valido_ingreso(2,'ABCDEFGV','opcion')

def titulares():
    op = valido_ingreso(3,'ABCMV','opcion')
    while op != 'V':
        mensaje() if op in 'ABCM' else 0
        op = valido_ingreso(3,'ABCMV','opcion')

def recepcion():
    global patente,producto,pesoNeto,camionM,pesoM,patenteMin,camionS,pesoS,max,min,patenteMax,pesoBruto,tara
    patente = input('Ingresar patente: ')
    while patente != '*':
        producto = valido_ingreso(0,'SM','producto')
        pesoBruto = ingresoNro('peso bruto'); tara = ingresoNro('tara')
        pesoNeto = pesoBruto - tara ; print(f'El peso neto es {pesoNeto}'); input(); os.system('cls')
        if producto == 'S':
            camionS = camionS + 1 ; pesoS = pesoS + pesoNeto
            if pesoNeto > max:
                patenteMax = patente ; max = pesoNeto
        else:
            camionM += 1 ; pesoM += pesoNeto
            if camionM == 1 or pesoNeto < min:
                patenteMin = patente ; min = pesoNeto
        patente = input('Ingresar patente: ')

def reportes():
    if camionS > 0 and camionM > 0:
        print(f'Reporte: \n\n Cantidad total de camiones: {camionS + camionM} \n Total de camiones de soja: {camionS} \n Total de camiones de maíz: {camionM}')
        print(f' Peso neto total de soja: {pesoS} Kgs \n Peso neto total de maíz: {pesoM} Kgs')
        print(f' Promedio del peso neto de soja por camión: {pesoS/camionS} Kgs\n Promedio del peso neto de maíz por camión: {pesoM/camionM} Kgs')
        print(f' Patente del camión de soja que mayor cantidad descargo: {patenteMax} \n Patente del camión de maíz que menor cantidad descargo: {patenteMin}'); input()
    else: print('Aun no se cargaron datos.'); input()

max = camionS = camionM = pesoS = pesoM = 0
op = valido_ingreso(1,'012345678','opcion')
while op != '0':
    if op == '1':
        administraciones()
    elif op in '24567':
        mensaje()
    elif op == '3':
        recepcion()
    elif op == '8':
        reportes()
    op = valido_ingreso(1,'012345678','opcion')
