import os
def valid_chr(k,valores_validos,i):
    os.system('cls')
    y = input(f'{k}Ingresar {i}: ').upper() ; os.system('cls')
    while y not in valores_validos:
        y = input(f'{k}Ingresar {i}: ').upper() ; os.system('cls')
    return y

def valid_int(i):
    y = input(f'{i}: ')
    while not y.isdigit() or int(y) < 0:
        y = input(f'{i}: ')
    return int(y)

def valid_str(y):
    os.system('cls')
    texto = input(f'{y}: ').upper(); os.system('cls')
    while ((len(texto) < 6 or len(texto) > 7) or not texto.isalnum()) and texto != '*' :
        texto = input(f'{y} : ').upper(); os.system('cls')
    return texto

def valid_MinMax(min,max,texto):
    k = valid_int(texto)
    while k < min or k > max:
        k = valid_int(texto)
    return k

def busqueda(x,y):
        pos = 0
        while y != x [pos] and pos < cant_cupos - 1:
            pos += 1
        k = pos if y == x [pos] else -1
        return k

def calculoMinMax(pos):
    if camiones[pos][2] > camm[camiones[pos][3]][3]:
        pat_mm[camiones[pos][3]][1] = cupos[pos]
        camm[camiones[pos][3]][3] = camiones[pos][2]
    if camiones[pos][2] < camm[camiones[pos][3]][2] or camm[camiones[pos][3]][2] == 0:
        pat_mm[camiones[pos][3]][0] = cupos[pos]
        camm[camiones[pos][3]][2] = camiones[pos][2]

def ordenamiento():
    for i in range(cant_cupos-1):
        for j in range(i+1,cant_cupos):
            if camiones[i][2] < camiones[j][2]:
                for k in range(4):
                    aux = camiones[i][k]
                    camiones[i][k] = camiones[j][k]
                    camiones[j][k] = aux
                aux2 = cupos[i]
                cupos[i] = cupos[j]
                cupos[j] = aux2
                aux3 = estado[i]
                estado[i] = estado[j]
                estado[j] = aux3

def Principal():
    global prod,cupos,estado,camiones,pat_mm,camm,cant_cupos
    prod = 3*['']; cupos = 8*['']; estado = 8*[''] 
    camiones = [[0]*4 for k in range(8)]
    pat_mm = [['']*2 for k in range(3)]
    camm = [[0]*4 for k in range(3)]
    cant_cupos = 0

    m = 'Menu Principal \n\n 1 - Administracion \n 2 - Entrega de cupos \n 3 - Recepcion \n 4 - Registrar calidad \n 5 - Registrar peso bruto \n 6 - Registrar descarga \n 7 - Registrar tara \n 8 - Reportes \n 0 - Salir\n\n '
    op = valid_chr(m,'012345678','opcion')
    while op != '0':
        if op == '1':
            Administraciones()
        elif op == '2':
            Entrega_cupos()
        elif op == '3':
            recepcion()
        elif op == '4':
            msj(0)
        elif op == '5':
            Registro_bruto()
        elif op == '6':
            msj(0)
        elif op == '7':
            Registro_tara()
        elif op == '8':
            Reportes()
        op = valid_chr(m,'012345678','opcion')

def Administraciones():
    m = 'Menu de administracion \n\n A - Titulares \n B - Productos \n C - Rubros \n D - Rubros por producto  \n E - Silos  \n F - Sucursales \n G - Producto por titular \n V - Volver al menu principal\n\n '
    op = valid_chr(m,'ABCDEFGV','opcion')
    while op != 'V':
        if op == 'A':
            ABMC('titulares',msj) 
        elif op == 'B' :
            ABMC('productos',Productos) 
        elif op == 'C' :
            ABMC('Rubros',msj) 
        elif op == 'D' :
            ABMC('Rubros por producto',msj) 
        elif op == 'E' :
            ABMC('Silos',msj) 
        elif op == 'F' :
            ABMC('Sucursales',msj) 
        elif op == 'G' :
            ABMC('Producto por titular',msj) 
        op = valid_chr(m,'ABCDEFGV','opcion')

def ABMC(k,x):
    m = (f'Menu de {k} \n\n A - Alta \n B - Baja \n C - Consulta \n M - Modificacion \n V - Volver al menu anterior\n\n ')
    op = valid_chr(m,'ABCMV','opcion')
    while op != 'V':
        if 'A' >= op <= 'C' or 'M':
            x(op)
        op = valid_chr(m,'ABCMV','opcion')

def msj(n):
    print('Esta funcionalidad esta en construcción.'), input()

def Entrega_cupos():
    global cant_cupos
    patente = valid_str('patente')
    while patente != '*' and cant_cupos < 8:
        if cant_cupos == 0 or busqueda(cupos,patente) == -1:
            cupos[cant_cupos], estado[cant_cupos] = patente, 'P'
            cant_cupos += 1
        else: print(f'La patente "{patente}" ya tiene cupo.'),input()
        patente = valid_str('patente nueva') if cant_cupos < 8 else 0

def recepcion():
    patente = valid_str('Patente')
    while patente != '*':
        pos = busqueda(cupos,patente)
        if pos >= 0 and estado[pos] == 'P':
            estado[pos] = 'E'
            muestra_producto()
            camiones[pos][3] = valid_MinMax(1,3,'\nopcion') - 1; os.system('cls')
        else: validaciones(pos,patente,'','P')
        patente = valid_str('Patente')

def Registro_bruto():
    patente = valid_str('patente')
    while patente != '*':
        pos = busqueda(cupos,patente)
        if pos >= 0 and estado[pos] == 'E' and camiones[pos][0] == 0:
            camiones[pos][0] = valid_int('peso bruto')
        else: validaciones(pos,patente,'El peso bruto ya fue registrado.','E')
        patente = valid_str('patente')

def Registro_tara():
    patente = valid_str('patente')
    while patente != '*':
        pos = busqueda(cupos,patente)
        if pos >= 0 and camiones[pos][1] == 0 and camiones[pos][0] != 0 and estado[pos] == 'E':
            camiones[pos][1] = valid_int('tara')
            estado[pos] = 'C'
            Calculos(pos)
        else: validaciones(pos,patente,'El peso bruto aun no fue registrado.','E')
        patente = valid_str('patente')

def validaciones(x,y,z,e):
    if x < 0: 
        print(f'La patente "{y}" no tiene cupo.')
    elif estado[x] != e:
        print('estado invalido')  
    else: 
        print(f'{z}')
    input()

def muestra_producto():
    [print (f'{i+1}. {producto}') if producto != '' else 0 for i,producto in enumerate(prod)]

def Productos(op):
    if op == 'A':
        for i in range(3):
            if prod[i] is '':
                prod[i] = input('Ingresar producto: ').capitalize()
            #elif i == 2: print('Ya se registraron todos los productos.'),input()
    elif op == 'C':
        muestra_producto(), input() 
    elif op in 'BM' and cant_cupos == 0:
        if op == 'B':
            muestra_producto(); opc = valid_MinMax(1,3,'\nCual eliminar') 
            prod[opc-1] = ''
            #[producto, next(producto) = next(producto), '' if producto is '' else 0 for producto in prod]
            for i in range (3):
                if prod[i] == '' and i < 2:
                    prod[i] = prod[i+1];  prod[i+1] = ''
        else:
            muestra_producto(); opc = valid_MinMax(1,3,'\nCual modificar'); os.system('cls')
            prod[opc-1] = input('Ingresar nuevo producto: ').capitalize()    
    else: print('No es posible acceder en este momento.'),input()

def Calculos(pos):
    camiones[pos][2] = camiones[pos][0] - camiones[pos][1] # calculo neto
    camm[camiones[pos][3]][0] += 1 #contador de camiones por producto
    camm[camiones[pos][3]][1] += camiones[pos][2] # acumNeto
    calculoMinMax(pos)

def Reportes():
    ordenamiento()
    print(f'Cantidad de cupos otorgados {cant_cupos}'),input(), os.system('cls')  
    print(f'Cantidad de camiones recibidos {camm[0][0]+camm[1][0]+camm[2][0]}'),input(), os.system('cls')
    
    print(' '*20,'TOTAL DE CAMIONES',' '*10, 'PESO NETO TOTAL',' '*10, ' PESO NETO PROMEDIO ',' '*10,'PATENTE MINIMA',' '*10, 'PATENTE MAXIMA\n' )    
    for i in range(3):
        print(f'{prod[i].ljust(27)} {str(camm[i][0]).ljust(22)} {str(camm[i][1]).rjust(6)} {"Kgs".ljust(24)} {str(round(camm[i][1]/camm[i][0],2)).rjust(6)} {"Kgs".ljust(23)} {pat_mm[i][0].ljust(24)} {pat_mm[i][1]}') if camm[i][0] != 0 else 0
    input(), os.system('cls')
    
    print(' '*10 ,'PATENTE',' '*10 ,'PRODUCTO',' '*10 ,'PESO NETO\n')
    for i in range(cant_cupos):
        print(f'{i+1} {"".ljust(8)} {cupos[i].ljust(18)} {prod[camiones[i][3]].ljust(20)} {str(camiones[i][2]).rjust(5)} kgs') if estado[i] == 'C' else 0
    input()

Principal()