import os, os.path, pickle, datetime
from datetime import date

class operaciones:
    def __init__(self):
        self.patente = ''
        self.cod = 0
        self.fecha_cupo = ''
        self.estado = ''
        self.bruto = 0
        self.tara = 0

class productos:
    def __init__(self):
        self.cod = 0 # 10
        self.nombre = '' #30
        self.activo = False
        self.cant_c = 0 #10
        self.acum_neto = 0 #10

class rubros:
    def __init__(self):
        self.cod_producto = 0
        self.nombre = 0

class rubrosXproducto:
    def __init__(self):
        self.cod_rubro = 0
        self.cod_producto = 0
        self.min = 0.00        
        self.max = 0.00

class silos:
    def __init__(self):
        self.cod_s = 0   #10
        self.nombre = '' #30
        self.cod = 0   #10
        self.stock = 0   #10

class report:
    def __init__(self):
        self.cant_cupos = 0
        self.cant_fin = 0
        self.ca

def valid_chr(k,valores_validos,i):
    os.system('cls')
    y = input(f'{k}{i}: ').upper() ; os.system('cls')
    while y not in valores_validos:
        y = input(f'{k}Ingresar {i}: ').upper() ; os.system('cls')
    return y

def valid_int(i):
    y = input(f'{i}: ')
    while not y.isdigit():
        y = input(f'{i}: ')
    return int(y)

def valid_str(y):
    os.system('cls')
    texto = input(f'{y}: ').upper(); os.system('cls')
    while ((len(texto) < 6 or len(texto) > 7) or not texto.isalnum()) and texto != '*' :
        texto = input(f'{y} : ').upper(); os.system('cls')
    return texto

def validarFecha():
    flag = True
    while flag:
        try:
            fecha = input("Ingresa una fecha en el formato DD/MM/AAAA: ")
            datetime.datetime.strptime(fecha, '%d/%m/%Y')
            flag = False
        except ValueError:
            print("Fecha invalida")
    return fecha

def validaciones(pat,pos,estado,e):
    if pos == -1:
        print(f'La patente {pat} no tiene cupo.')
    elif pos != -1 and estado != e:
        print(f'Estado invalido.')

def msj(n):
    print('Proceso en construcción.'), input()

def abrir(af):
    if not os.path.exists(af):
        al = open(af,'w+b')
    else:
        al = open(af,'r+b')
    return al

def principal():
    global aOperaciones,aProd,aRubros,afRubros,aRubrosXproducto,aSilos,afProd,afOperaciones,afRubrosXproducto,afSilos,fecha_actual

    afOperaciones = 'K:\\ayed\\Operaciones.dat'
    afProd = 'K:\\ayed\\Prod.dat'
    afRubros = 'K:\\ayed\\Rubros.dat'
    afRubrosXproducto = 'K:\\ayed\\RubrosXproducto.dat'
    afSilos = 'K:\\ayed\\Silos.dat'

    aOperaciones = abrir(afOperaciones)
    aProd = abrir(afProd)
    aRubros = abrir(afRubros)
    aRubrosXproducto = abrir(afRubrosXproducto)
    aSilos = abrir(afSilos)

    fecha_actual = date.today().strftime('%d/%m/%Y')

    m = '''Menu Principal \n\n 1 - Administracion \n 2 - Entrega de cupos \n 3 - Recepcion \n 4 - Registrar calidad \n 5 - Registrar peso bruto \n 6 - Registrar descarga(DEBUG BORRAR ANTES DE ENTREGAR!) \n 7 - Registrar tara \n 8 - Reportes \n 9 - Listado de silos y rechazos \n 0 - Salir\n\n '''
    op = '-1'
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
            debug()
        elif op == '7':
            Registro_tara()
        elif op == '8':
            Reportes()
        elif op == '9':
            max_silos()
            listado_rechazos(),input()
        op = valid_chr(m,'0123456789','Ingresar opcion')
    aOperaciones.close(), aProd.close(), aRubros.close(), aRubrosXproducto.close(), aSilos.close()

def Administraciones():
    m = 'Menu de administracion \n\n A - Titulares \n B - Productos \n C - Rubros \n D - Rubros por producto  \n E - Silos  \n F - Sucursales \n G - Producto por titular \n V - Volver al menu principal\n\n '
    op = '-1'
    while op != 'V':
        if op in 'AFG':
            msj(None)
        elif op == 'B' :
            ABMC('productos',Productos,None)
        elif op == 'C' :
            ABMC('Rubros',Altas,alta_Rubros) 
        elif op == 'D' :
            ABMC('Rubros X producto',Altas,alta_RubrosxProductos) 
        elif op == 'E' :
            ABMC('Silos',Altas,alta_Silos) 
        op = valid_chr(m,'ABCDEFGV','Ingresar opcion')        

def ABMC(k,x,acceso):
    m = (f'Menu de {k} \n\n A - Alta \n B - Baja \n C - Consulta \n M - Modificacion \n V - Volver al menu anterior\n\n ')
    op = '-1'
    while op != 'V':
        if 'A' >= op <= 'C' or 'M':
            x(op,acceso)
        op = valid_chr(m,'ABCMV','Ingresar opcion')

def Productos(op,z):
    reg_p = productos()
    if op == 'A':
        alta_producto(reg_p)
    elif op == 'B':
        baja_producto(reg_p)
    elif op == 'C':
        lista_productos(reg_p), input()
    elif op == 'M':
        modifica_producto(reg_p)

def busca_producto(cod,reg_p):
    size = os.path.getsize(afProd)
    aProd.seek(0)
    aux = productos()
    while int(aux.cod) != cod and aProd.tell() < size:
        pos = aProd.tell()
        aux = pickle.load(aProd)
    if int(aux.cod) == cod:
        reg_p.cod = aux.cod
        reg_p.nombre = aux.nombre
        reg_p.cant_c = aux.cant_c
        reg_p.acum_neto = aux.acum_neto
        reg_p.activo = aux.activo
        return pos
    else: return -1

def alta_producto(reg_p):    
    nomb = input('Ingresar nombre de producto: ')
    while nomb != '*':
        #cod = int(reg_p.cod) + 10
        #if os.path.getsize(afProd) == 0:# or busca_producto(cod,reg_p) == -1:
        reg_p.nombre = nomb.capitalize()
        cod = int(reg_p.cod)
        cod += 10
        reg_p.cod = cod
        reg_p.activo = True
        format_producto(reg_p)
        pickle.dump(reg_p,aProd)
        aProd.flush()
        #else:
        #    print('El producto ya existe'),input()
        nomb = input('Ingresar nombre de producto: ')

def muestra_producto(p):
    print(f'Codigo de producto: {p.cod} \nNombre : {p.nombre} \nEstado : {p.activo}')

def modifica_producto(reg_p):
    cod = valid_int('codigo de producto')
    while cod != 0 :
        pos = busca_producto(cod,reg_p) 
        if pos != -1:
            aProd.seek(pos,0)
            muestra_producto(reg_p), input()
            if reg_p.activo:
                if valid_chr('','SN','Modificar?S/N') == 'S':
                    reg_p.nombre = input('Nombre: ')
                    aProd.seek(pos,0)
                    format_producto(reg_p)
                    pickle.dump(reg_p, aProd)
                    aProd.flush()
                    muestra_producto(reg_p), input()
            else: print('El producto ya fue dado de baja.'), input()              
        else: print('El codigo no existe'), input()
        cod = valid_int('codigo de producto')

def baja_producto(reg_p):
    cod = valid_int('codigo de producto')
    while cod != 0 :
        pos = busca_producto(cod,reg_p)
        if pos != -1:
            aProd.seek(pos,0)
            muestra_producto(reg_p), input()
            if reg_p.activo:
                if valid_chr('','SN','Dar de baja?S/N') == 'S':
                    reg_p.activo = False
                    aProd.seek(pos,0)
                    pickle.dump(reg_p, aProd)
                    aProd.flush()
                    muestra_producto(reg_p), input()
            else: 
                print('El producto ya fue dado de baja.'), input()
        else:
            print('el codigo no es valido.'), input()
        cod = valid_int('codigo de producto')

def lista_productos(p):
    t = os.path.getsize(afProd)
    if t != 0:
        aProd.seek(0)
        while aProd.tell() < t:
            p = pickle.load(aProd)
            print (f'codigo: {p.cod}  nombre: {p.nombre} activo? {p.activo} cant camiones {p.cant_c} acum neto {p.acum_neto}')

def format_producto(f):
    f.cod = str(f.cod).ljust(10,' ')
    f.nombre = f.nombre.ljust(30,' ')
    f.cant_c = str(f.cant_c).ljust(10,' ')
    f.acum_neto = str(f.acum_neto).ljust(10,' ')

def actualizar_producto(cod,peso_neto):
    reg_p = productos()
    aProd.seek(0)
    pos = busca_producto(cod,reg_p)
    acum, cont = int(reg_p.acum_neto), int(reg_p.cant_c)
    acum += peso_neto
    cont += 1
    reg_p.acum_neto,reg_p.cant_c = acum, cont
    aProd.seek(pos)
    format_producto(reg_p)
    pickle.dump(reg_p, aProd)
    aProd.flush()



def Altas(op,Alta_go):
    if op == 'A':
        Alta_go()
    elif op in 'BCM':
        print('no se puede acceder'), input()

def alta_RubrosxProductos():
    print('alta rubros x prod'), input()

def alta_Rubros():
    print('alta rubros'), input()

def alta_Silos():
    s = silos()
    reg_p = productos()
    cod = valid_int('codigo de silo')
    while cod != 0:
        s.cod_s = cod
        s.nombre = input('Ingresar nombre de silo: ')
        codigo = valid_int('codigo de producto')
        while busca_producto(codigo,reg_p) == -1:
            codigo = valid_int('El codigo de producto no existe. Ingresar nuevamente')
        s.cod = codigo        
        format_silos(s)
        pickle.dump(s,aSilos)
        aSilos.flush()
        cod = valid_int('codigo de silo')

def lista_silos():
    t = os.path.getsize(afSilos)
    if t != 0:
        aSilos.seek(0)
        print('lista de silos')
        #pregunta = valid_chr('','SN','poner stock en 0?: ')
        while aSilos.tell() < t:
            s = pickle.load(aSilos)
            '''if pregunta == 'S':
                s.stock = 0
                format_silos(s)
                pickle.dump(s,aSilos)
                aSilos.flush()'''
            print (f'{s.cod} {s.cod_s} {s.nombre} {s.stock}')


def format_silos(s):
    s.cod_s = str(s.cod_s).ljust(10,' ')
    s.nombre = s.nombre.ljust(30,' ')
    s.cod = str(s.cod).ljust(10,' ')
    s.stock = str(s.stock).ljust(10,' ')

def busca_silo(s,cod):
    aSilos.seek(0)
    flag = False
    while not flag:
        pos = aSilos.tell()
        aux = pickle.load(aSilos)
        flag = True if int(aux.cod) == cod else False   
    s.cod_s = aux.cod_s
    s.nombre = aux.nombre
    s.cod = aux.cod
    s.stock = aux.stock
    return pos

def actualizar_silo(cod,peso_neto):
    s = silos()
    aSilos.seek(0)
    pos = busca_silo(s,cod)
    stock = int(s.stock)
    aSilos.seek(pos)
    stock += peso_neto
    s.stock = stock
    format_silos(s)
    pickle.dump(s,aSilos)
    aSilos.flush()

def Entrega_cupos():
    o = operaciones(); reg_p = productos()
    patente = valid_str('patente')
    while patente != '*':
        fecha = validarFecha()
        if os.path.getsize(afOperaciones) == 0 or busca_op(patente,fecha,reg_p) == -1:
            cod = valid_int('codigo de producto')
            while busca_producto(cod,reg_p) == -1:
                cod = valid_int('El codigo de producto no existe. Ingresar nuevamente')
            o.patente = patente
            o.cod = cod
            o.fecha_cupo = fecha
            o.estado = 'P'
            format_operaciones(o)
            pickle.dump(o,aOperaciones)
            orden_operaciones()
            aOperaciones.flush()
            print(f'operacion exitosa {fecha}'),input()
        else: 
            print('La patente ya tiene cupo en esa fecha.'),input()            
        patente = valid_str('Ingresar patente')

def orden_operaciones():
    aOperaciones.seek(0)
    aux_i = pickle.load(aOperaciones)
    tam_reg = aOperaciones.tell()
    t = os.path.getsize(afOperaciones)
    cant_reg = t // tam_reg
    for i in range(cant_reg - 1):
        for j in range(i+1, cant_reg):
            aOperaciones.seek(i*tam_reg)
            aux_i= pickle.load(aOperaciones)
            aOperaciones.seek(j*tam_reg)
            aux_j = pickle.load(aOperaciones)

            if aux_i.cod > aux_j.cod:
                aOperaciones.seek(i*tam_reg)
                pickle.dump(aux_j,aOperaciones)
                aOperaciones.seek(j*tam_reg)
                pickle.dump(aux_i,aOperaciones)
                #aOperaciones.flush()

def format_operaciones(operacion):
    operacion.patente = operacion.patente.ljust(7,' ')
    operacion.cod = str(operacion.cod).ljust(10,' ')
    operacion.fecha_cupo = operacion.fecha_cupo.ljust(10,' ')
    operacion.bruto = str(operacion.bruto).ljust(10,' ')
    operacion.tara = str(operacion.tara).ljust(10,' ')

def busca_op(patente,fecha,reg_op):
    t = os.path.getsize(afOperaciones)
    aOperaciones.seek(0)
    flag = False
    while not flag and aOperaciones.tell() < t:
        pos = aOperaciones.tell()
        reg = pickle.load(aOperaciones)
        if reg.patente == patente.ljust(7) and reg.fecha_cupo == fecha.ljust(10):
            flag = True          
    if flag:
        reg_op.patente = reg.patente
        reg_op.cod = reg.cod
        reg_op.fecha_cupo = reg.fecha_cupo
        reg_op.estado = reg.estado
        reg_op.bruto = reg.bruto
        reg_op.tara = reg.tara
        return pos
    else: return -1        

def mostrar_registro_actual(ops):
    print (f'{ops.patente}  {ops.cod} {ops.fecha_cupo}  {ops.estado}'),input()

def recepcion():
    reg_op = operaciones()
    patente = valid_str('patente')
    while patente != '*':
        pos = busca_op(patente,fecha_actual,reg_op)
        aOperaciones.seek(0)
        if pos != -1 and reg_op.estado == 'P':
            reg_op.estado = 'C' #valid_chr('','CR','Ingresar nuevo estado')
            aOperaciones.seek(pos)
            pickle.dump(reg_op,aOperaciones)
            aOperaciones.flush()
        else: validaciones(patente,pos,reg_op.estado,'B'),input()                           
        patente = valid_str('patente')

def Registro_bruto():
    reg_op = operaciones()
    patente = valid_str('patente')
    while patente != '*':
        pos = busca_op(patente,fecha_actual,reg_op)
        aOperaciones.seek(0)
        if pos != -1 and reg_op.estado == 'C':
            reg_op.bruto = valid_int('Peso bruto')
            reg_op.estado = 'B'
            aOperaciones.seek(pos)
            format_operaciones(reg_op)
            pickle.dump(reg_op,aOperaciones)
            aOperaciones.flush()
        else: validaciones(patente,pos,reg_op.estado,'C'),input()     
        patente = valid_str('patente')

def Registro_tara():
    reg_op = operaciones()
    patente = valid_str('patente')
    while patente != '*':
        pos = busca_op(patente,fecha_actual,reg_op)
        aOperaciones.seek(0)
        if pos != -1 and reg_op.estado == 'F' or reg_op.estado == 'B':
            peso = 1 #valid_int('peso tara')
            while peso >= int(reg_op.bruto):
                peso = valid_int('peso tara')
            reg_op.tara = peso
            cod = int(reg_op.cod)
            neto = int(reg_op.bruto) - int(reg_op.tara)
            actualizar_silo(cod,neto)
            actualizar_producto(cod,neto)
            reg_op.estado = 'F'
            aOperaciones.seek(pos)
            format_operaciones(reg_op)
            pickle.dump(reg_op,aOperaciones)
            aOperaciones.flush()
        else: validaciones(patente,pos,reg_op.estado,'B'),input()     
        patente = valid_str('patente')   

def debug():
    #orden_operaciones()
    t = os.path.getsize(afOperaciones)
    aOperaciones.seek(0)
    while aOperaciones.tell() < t:
        ops = pickle.load(aOperaciones)
        print (f'{ops.patente}  {ops.cod} {ops.fecha_cupo}  {ops.estado} {ops.bruto} {ops.tara}')
    input()
    lista_silos()
    input()

def Reportes():
    aProd.seek(0)
    aOperaciones.seek(0)
    reg_p, reg_op = pickle.load(aProd), pickle.load(aOperaciones)
    aProd.seek(0)
    aOperaciones.seek(0)
    print(' '*20,'TOTAL DE CAMIONES',' '*10, 'PESO NETO TOTAL',' '*10, ' PESO NETO PROMEDIO ',' '*10,'PATENTE MINIMA\n' )
    pos = 0
    prom = 1
    #tam_reg = aOperaciones.tell()
    while aProd.tell() < os.path.getsize(afProd):  #aOperaciones.tell() < os.path.getsize(afOperaciones):
        cont, min = 0, 0
        pos2 = aProd.tell()
        reg_p = pickle.load(aProd)
        aux = reg_p.cod
        while  reg_op.cod == aux  and aOperaciones.tell() < os.path.getsize(afOperaciones):
            pos = aOperaciones.tell()
            reg_op = pickle.load(aOperaciones)
            #print(f' producto actual {reg_p.nombre} codigo pat{reg_op.cod} codigo prod{reg_p.cod} vueltas {cont}'),input()              
            neto = int(reg_op.bruto) - int(reg_op.tara)
            cont += 1

            if neto < min or min == 0:
                min = neto
                pat_min = reg_op.patente

                            
            #print(f'calculando menor {reg_p.nombre} cod prod {reg_op.cod} {pos}'), input()
        #if reg_op.cod != aux and aOperaciones.tell() > os.path.getsize(afOperaciones):
        #    atras =  tam_reg - pos
        #    #print('atras',atras),input()
        #    aOperaciones.seek(atras,0)
        #prom = float(reg_p.acum_neto) / float(reg_p.cant_c)
        print(f' {reg_p.nombre} {reg_p.cant_c} {reg_p.acum_neto} {str(prom).ljust(30)} {pat_min} {reg_p.cod} pos archivo: {pos}') 

    input()


def listado_rechazos():
    t = os.path.getsize(afOperaciones)
    aOperaciones.seek(0)
    fecha = validarFecha(); os.system('cls')
    print(f'Listado de patentes rechazadas el dia {fecha}: \n')
    while aOperaciones.tell() < t:
        ops = pickle.load(aOperaciones)
        if fecha == ops.fecha_cupo and ops.estado == 'R':
            print(f' {ops.patente}')

def max_silos():
    max,maxPos = 0,0
    t = os.path.getsize(afSilos)
    aSilos.seek(0)
    while aSilos.tell() < t:
        pos = aSilos.tell()
        s = pickle.load(aSilos)
        if int(s.stock) > max:
            max = int(s.stock)
            maxPos = pos
    aSilos.seek(maxPos)            
    print(f'{s.cod_s} {s.cod} {s.stock} '),input()

principal()  
