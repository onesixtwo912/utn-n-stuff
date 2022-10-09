import os, os.path, pickle, datetime
from datetime import date

class operaciones:
    def __init__(self):
        self.patente = ''       #7
        self.cod = 0            #10
        self.fecha_cupo = ''    #10
        self.estado = ''        #1
        self.bruto = 0          #10
        self.tara = 0           #10

class productos:
    def __init__(self):
        self.cod = 0        #10
        self.nombre = ''    #30
        self.activo = False

class rubros:
    def __init__(self):
        self.cod = 0        #10
        self.nombre = ''    #50

class rubrosXproducto:
    def __init__(self):
        self.cod_rubro = 0      #10
        self.cod_producto = 0   #10
        self.min = 0.00         #10
        self.max = 0.00         #10

class silos:
    def __init__(self):
        self.cod_s = 0   #10
        self.nombre = '' #30
        self.cod = 0     #10
        self.stock = 0   #10

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

def valid_MinMax(min,max,x):
    k = input(x)
    while not k.isdigit() or (float(k) < min or float(k) > max):
        k = input(x)
    return float(k)

def msj(n):
    print('Proceso en construcción.'), input()

def abrir(af):
    if not os.path.exists(af):
        al = open(af,'w+b')
    else:
        al = open(af,'r+b')
    return al

def principal():
    global aOperaciones,aProd,aRubros,afRubros,aRubrosXproducto,aSilos,afProd,afOperaciones,afRubrosXproducto,afSilos

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
    

    m = '''Menu Principal \n\n 1 - Administracion \n 2 - Entrega de cupos \n 3 - Recepcion \n 4 - Registrar calidad \n 5 - Registrar peso bruto \n 6 - Registrar descarga \n 7 - Registrar tara \n 8 - Reportes \n 9 - Listado de silos y rechazos \n 0 - Salir\n\n '''
    op = '-1'
    while op != '0':
        if op == '1':
            Administraciones()
        elif op == '2':
            Entrega_cupos()
        elif op == '3':
            validaciones('P',recepcion)
        elif op == '4':
            validaciones('A',registro_calidad)
        elif op == '5':
            validaciones('C',Registro_bruto)
        elif op == '6':
            debug()
        elif op == '7':
            validaciones('B',Registro_tara)
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
    aProd.seek(0)
    aux = productos()
    while int(aux.cod) != cod and aProd.tell() < os.path.getsize(afProd):
        pos = aProd.tell()
        aux = pickle.load(aProd)
    if int(aux.cod) == cod:
        reg_p.cod = aux.cod
        reg_p.nombre = aux.nombre
        reg_p.activo = aux.activo
        return pos
    else: return -1

def alta_producto(reg_p):  
    cod = valid_int('Codigo de producto')
    while cod != 0:
        if os.path.getsize(afProd) == 0  or busca_producto(cod,reg_p) == -1:
            reg_p.nombre = input('Ingresar nombre de producto: ').capitalize()            
            reg_p.cod = cod
            reg_p.activo = True
            format_producto(reg_p)
            pickle.dump(reg_p,aProd)
            aProd.flush()
            
        else:
            print('El producto ya existe'),input()
        cod = valid_int('Codigo de producto')

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
    t = os.path.getsize(afProd);i = 0
    if t != 0:
        aProd.seek(0)
        print(' '*6,'PRODUCTO',' '*10,'CODIGO DE PRODUCTO',' '*10,'ESTADO\n','--'*35)
        while aProd.tell() < t:
            p = pickle.load(aProd)
            aux = 'Activo' if p.activo else 'Inactivo'
            i += 1
            print (f'\t{p.nombre.strip().ljust(26)} {p.cod.ljust(21)} {aux}')

def format_producto(f):
    f.cod = str(f.cod).ljust(10,' ')
    f.nombre = f.nombre.ljust(30,' ')

def Altas(op,x):
    if op == 'A':
        x()
    elif op in 'BCM':
        print('no se puede acceder'), input()

def busca_rubros_dico(cod):    
    aRubros.seek(0)
    aux = pickle.load(aRubros)
    flag = False
    tam_reg = aRubros.tell()
    cant_reg = os.path.getsize(afRubros)//tam_reg
    inicio = 0
    fin = cant_reg - 1
    while inicio <= fin and not flag:
        medio = (inicio + fin ) // 2
        aRubros.seek(medio*tam_reg)
        reg = pickle.load(aRubros)
        if int(reg.cod) == cod:
            flag = True
        
        elif int(reg.cod) < cod:
            inicio = medio + 1
        else:
            fin = medio - 1            
    if flag: 
        return medio*tam_reg        
    else:
        return - 1             

def busca_rubro_sec(cod,reg):
    aRubros.seek(0)
    aux = pickle.load(aRubros)
    pos = aRubros.tell()
    while int(aux.cod) != cod and aRubros.tell() < os.path.getsize(afRubros):
        pos = aRubros.tell()
        aux = pickle.load(aRubros)
    if int(aux.cod) == cod:
        reg.cod = aux.cod
        reg.nombre = aux.nombre
        return pos
    return - 1        
     
def orden_rubros():
    aRubros.seek(0)
    auxi = pickle.load(aRubros)
    tam_reg = aRubros.tell()
    t = os.path.getsize(afRubros)
    cant_reg = t // tam_reg
    for i in range(cant_reg - 1):
        for j in range(i+1, cant_reg):
            aRubros.seek(i*tam_reg)
            auxi = pickle.load(aRubros)
            aRubros.seek(j*tam_reg)
            auxj = pickle.load(aRubros)

            if int(auxi.cod) > int(auxj.cod):
                aRubros.seek(i*tam_reg)
                pickle.dump(auxj,aRubros)
                aRubros.seek(j*tam_reg)
                pickle.dump(auxi,aRubros)
                #aRubros.flush()
        
def lista_rubros():
    aRubros.seek(0)
    aux= pickle.load(aRubros)
    print('tamaño tot',os.path.getsize(afRubros),'tam reg',aRubros.tell())
    while True :
        print(f'cod{aux.cod}  {aux.nombre} {aRubros.tell()}')
        if aRubros.tell() == os.path.getsize(afRubros):
            break
        aux = pickle.load(aRubros)
    input()        

def alta_Rubros():
    rubro = rubros()
    if os.path.getsize(afRubros) != 0:
        aRubros.seek(0)
        rubro = pickle.load(aRubros)
        aRubros.seek(os.path.getsize(afRubros)-aRubros.tell())
        rubro = pickle.load(aRubros)
    nombre = input('Ingresar nombre de rubro: ').capitalize()
    while nombre != '*' :
        cod = int(rubro.cod); cod += 1
        rubro.cod = cod
        rubro.nombre = nombre
        format_rubros(rubro)
        pickle.dump(rubro,aRubros)
        aRubros.flush() 
        nombre = input('Ingresar nombre de rubro: ').capitalize()           

def format_rubros(rubro):
    rubro.cod = str(rubro.cod).ljust(10)
    rubro.nombre = rubro.nombre.ljust(50)

def nombre_rubro(k):
    aRubros.seek(0)
    aux = pickle.load(aRubros)
    tam_reg = aRubros.tell()
    print(tam_reg)     ,input()
    aRubros.seek(k*tam_reg)
    reg = pickle.load(aRubros)
    return reg.nombre.strip()

def alta_RubrosxProductos():
    reg_p = productos()
    rubrosX = rubrosXproducto()
    reg_rubro = rubros()
    cod_prod = valid_int('Codigo de producto')     
    while cod_prod != 0:        
        while busca_producto(cod_prod,reg_p) == -1:
            cod_prod = valid_int('El codigo de producto no existe. Ingresar nuevamente')
        cod_rubro = valid_int('Codigo de rubro')
        while busca_rubro_sec(cod_rubro,reg_rubro) == -1:
            cod_rubro = valid_int('El codigo de rubro no existe. Ingresar nuevamente')     
        rubrosX.cod_rubro = cod_rubro        
        rubrosX.cod_producto = cod_prod                
        rubrosX.min = valid_MinMax(0,100,f'Ingresar el nivel minimo de {reg_rubro.nombre.strip()} admitido para {reg_p.nombre.strip()}: ')            
        rubrosX.max = valid_MinMax(0,100,f'Ingresar el nivel maximo de {reg_rubro.nombre.strip()} admitido para {reg_p.nombre.strip()}: ')
        format(rubrosX)
        pickle.dump(rubrosX,aRubrosXproducto)
        aRubrosXproducto.flush()
        cod_prod = valid_int('Codigo de producto')
    
def format_aRubrosXproducto(rubrosX):
    rubrosX.cod_rubro = str(rubrosX.cod_rubro).ljust(10)
    rubrosX.cod_producto = str(rubrosX.cod_producto).ljust(10)
    rubrosX.max = str(rubrosX.max).ljust(10)
    rubrosX.min = str(rubrosX.min).ljust(10)

def alta_Silos():
    s = silos()
    reg_p = productos()
    cod = valid_int('Ingresar codigo de silo')
    while cod != 0:
        s.cod_s = cod
        s.nombre = input('Ingresar nombre de silo: ')
        codigo = valid_int('codigo de producto')
        while busca_producto(codigo,reg_p) == -1 or (busca_producto(codigo,reg_p) == -1 and not reg_p.activo):
            codigo = valid_int('El codigo de producto no existe. Ingresar nuevamente')
        s.cod = codigo        
        format_silos(s)
        pickle.dump(s,aSilos)
        aSilos.flush()
        cod = valid_int('Ingresar codigo de silo')

def lista_silos():
    aSilos.seek(0)
    t = os.path.getsize(afSilos)
    s = pickle.load(aSilos)
    if t != 0:
        aSilos.seek(0)
        print('lista de silos')
        pregunta = valid_chr('','SN','poner stock en 0?: ')        
        while aSilos.tell() < t:
            if pregunta == 'S':
                s.stock = 0
                format_silos(s)
                pickle.dump(s,aSilos)
                aSilos.flush()
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

def Entrega_cupos():
    reg_op = operaciones(); reg_p = productos()
    patente = valid_str('patente')
    while patente != '*':
        fecha = validarFecha()        
        if os.path.getsize(afOperaciones) == 0 or busca_op(patente,reg_p) == -1:
            cod = valid_int('codigo de producto')
            while busca_producto(cod,reg_p) == -1 or (busca_producto(cod,reg_p) == -1 and not reg_p.activo):
                cod = valid_int('El codigo de producto no existe. Ingresar nuevamente')
            reg_op.patente = patente
            reg_op.cod = cod
            reg_op.fecha_cupo = fecha
            reg_op.estado = 'P'
            format_operaciones(reg_op)
            pickle.dump(reg_op,aOperaciones)
            orden_operaciones()
            aOperaciones.flush()
        elif busca_op(patente,reg_p) != -1 and reg_op.fecha.strip() == fecha: 
            print(f'La patente {patente} ya tiene cupo para esa fecha.'),input()
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
            aux_i = pickle.load(aOperaciones)
            aOperaciones.seek(j*tam_reg)
            aux_j = pickle.load(aOperaciones)

            if int(aux_i.cod) > int(aux_j.cod):
                aOperaciones.seek(i*tam_reg)
                pickle.dump(aux_j,aOperaciones)
                aOperaciones.seek(j*tam_reg)
                pickle.dump(aux_i,aOperaciones)                

def format_operaciones(operacion):
    operacion.patente = operacion.patente.ljust(7,' ')
    operacion.cod = str(operacion.cod).ljust(10,' ')
    operacion.fecha_cupo = operacion.fecha_cupo.ljust(10,' ')
    operacion.bruto = str(operacion.bruto).ljust(10,' ')
    operacion.tara = str(operacion.tara).ljust(10,' ')

            
def busca_op(patente,reg_op):
    t = os.path.getsize(afOperaciones)
    aOperaciones.seek(0)
    flag = False
    while not flag and aOperaciones.tell() < t:
        pos = aOperaciones.tell()
        reg = pickle.load(aOperaciones)
        if reg.patente.strip() == patente:
            flag = True          
    if flag:
        reg_op.patente = reg.patente
        reg_op.cod = reg.cod
        reg_op.fecha_cupo = reg.fecha_cupo
        reg_op.estado = reg.estado
        reg_op.bruto = reg.bruto
        reg_op.tara = reg.tara
        return pos
    return -1        

def mostrar_registro_actual(ops):
    print (f'{ops.patente}  {ops.cod} {ops.fecha_cupo}  {ops.estado}'),input()

def validaciones(e,acceso):
    reg_op = operaciones()
    fecha_actual = date.today().strftime('%d/%m/%Y')
    patente = valid_str('Ingresar patente')
    while patente != '*':
        pos = busca_op(patente,reg_op)
        if pos == -1:
            print(f'La patente {patente} no tiene cupo.'),input()
        elif pos != -1 and reg_op.fecha_cupo.strip() != fecha_actual:
            print(f'La patente {reg_op.patente} no tiene cupo para el dia de hoy.'),input()
        elif pos != -1 and reg_op.estado != e:
            print(f'Estado invalido.'),input()
        else:            
            acceso(reg_op,pos)
        patente = valid_str('Ingresar patente')

def recepcion(reg_op,pos):
    reg_op.estado = 'A' #valid_chr('','CR','Ingresar nuevo estado')
    aOperaciones.seek(pos)
    pickle.dump(reg_op,aOperaciones)
    aOperaciones.flush()

def busca_cod(i):
    aRubrosXproducto.seek(0)
    aux = pickle.load(aRubrosXproducto)
    tam_reg = aRubrosXproducto.tell()
    aRubrosXproducto.seek(i*tam_reg)

def rxp():
    aRubrosXproducto.seek(0)
    t = os.path.getsize(afRubrosXproducto)
    while aRubrosXproducto.tell() < t:
        rubrosX = pickle.load(aRubrosXproducto)
        print(f'codigo rubro {rubrosX.cod_rubro} cod prod {rubrosX.cod_producto}')
    input()        


def registro_calidad(reg_op,pos):
    rubro = rubros(); rubrosX = rubrosXproducto()
    flag = False
    t = os.path.getsize(afRubrosXproducto)
    aRubrosXproducto.seek(0)
    #rubrosX = pickle.load(aRubrosXproducto)
    tam_reg = aRubrosXproducto.tell()
    lim = 0
    print(f'{int(reg_op.cod)}  {int(rubrosX.cod_producto)}')
    while aRubrosXproducto.tell() < t:
        while  not flag:# and lim < 2: #and aRubrosXproducto.tell() < t:
            rubrosX = pickle.load(aRubrosXproducto)
            pos = aRubrosXproducto.tell()
            aux = busca_rubro_sec(rubrosX.cod_rubro,rubro)
            valor = valid_MinMax(0,100,f'{rubro.nombre.strip()} (max{rubrosX.max} min{rubrosX.min}) pos {aRubrosXproducto.tell()}: ')
            if valor > rubrosX.max or valor < rubrosX.min:
                lim += 1
            if int(reg_op.cod) != int(rubrosX.cod_producto) or pos == t or lim == 2: 
                flag = True  
            else: False
        '''if  aRubrosXproducto.tell() == t and not flag:  
            atras = t - 112 #tam_reg
            aOperaciones.seek(atras)
            flag = True'''
    #if lim < 2:
    #    reg_op.estado = 'C' 
    #else: 
    #    reg_op.estado = 'R'
    print(reg_op.estado,'final',lim,t,aRubrosXproducto.tell()),input()
    #pickle.dump(reg_op,aOperaciones)
    #aOperaciones.flush()

def Registro_bruto(reg_op,pos):
    reg_op.bruto = valid_int('Ingresar peso bruto:')
    reg_op.estado = 'B'
    aOperaciones.seek(pos)
    format_operaciones(reg_op)
    pickle.dump(reg_op,aOperaciones)
    aOperaciones.flush()

def Registro_tara(reg_op,pos):
    peso = valid_int('Ingresar peso tara')
    while peso >= int(reg_op.bruto):
        peso = valid_int('Ingresar peso tara')
    reg_op.tara = peso
    reg_op.estado = 'F'
    actualizar_silo(reg_op.cod,int(reg_op.bruto)-reg_op.tara)
    aOperaciones.seek(pos)
    format_operaciones(reg_op)
    pickle.dump(reg_op,aOperaciones)
    aOperaciones.flush()

def debug():
    #orden_operaciones()
    t = os.path.getsize(afOperaciones)
    #ops = pickle.load(aOperaciones)
    aOperaciones.seek(0)
    ops = pickle.load(aOperaciones)
    tam_reg = aOperaciones.tell()
    aOperaciones.seek(0)

    while aOperaciones.tell() < t:
        ops = pickle.load(aOperaciones)
        print (f'{ops.patente}  {ops.cod} {ops.fecha_cupo}  {ops.estado} {ops.bruto} {ops.tara} pos {aOperaciones.tell()} {t/tam_reg}')
    input()
    #lista_silos()
    rxp()
    input()
    lista_rubros()

def Reportes():
    t = os.path.getsize(afOperaciones)
    aOperaciones.seek(0)
    reg_p = productos()
    reg_op = pickle.load(aOperaciones)
    tam_reg = aOperaciones.tell()
    flag = False
    cant_cupos, total_camiones = 0,0
    print(' '*15,'TOTAL DE CAMIONES',' '*8, 'PESO NETO TOTAL',' '*8, ' PESO NETO PROMEDIO ',' '*8,'PATENTE MINIMA\n','--'*56 )
    while aOperaciones.tell() < t:
        cant_camiones = acum_neto = min = 0
        aux = reg_op.cod
        while  reg_op.cod == aux and aOperaciones.tell() < t:
            if reg_op.estado == 'F':
                neto = int(reg_op.bruto) - int(reg_op.tara)
                cant_camiones += 1                
                acum_neto += neto            
                if neto < min or min == 0:
                    min = neto
                    pat_min = reg_op.patente
            cant_cupos += 1
            reg_op = pickle.load(aOperaciones)  
            pos = aOperaciones.tell()          
            if  pos == t and not flag:
                atras = t - tam_reg
                aOperaciones.seek(atras)
                flag = True
        total_camiones += cant_camiones                    

        pos_prod = busca_producto(int(aux),reg_p); aProd.seek(pos_prod)    
        print(f' {reg_p.nombre.strip().ljust(21)}  {str(cant_camiones).ljust(23)} {str(acum_neto).ljust(26)} {str(round(acum_neto / cant_camiones,2)).ljust(25)} {pat_min.ljust(20)} \n')
    print(f'Total de cupos otorgados: {cant_cupos}')
    print(f'Total de camiones recibidos: {total_camiones}'), input()

def actualizar_silo(cod,peso_neto):
    s = silos()
    aSilos.seek(0)
    pos = busca_silo(s,cod)
    stock = int(s.stock)
    stock += peso_neto
    s.stock = stock
    aSilos.seek(pos)
    format_silos(s)
    pickle.dump(s,aSilos)
    aSilos.flush()

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
