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
        self.minmax = [0.00]*2  #10

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

def validar_fecha():
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
    global alOperaciones,alProductos,alRubros,afRubros,alRubrosXproducto,alSilos,afProductos,afOperaciones,afRubrosXproducto,afSilos

    afOperaciones = 'K:\\ayed\\Operaciones.dat'
    afProductos = 'K:\\ayed\\Prod.dat'
    afRubros = 'K:\\ayed\\Rubros.dat'
    afRubrosXproducto = 'K:\\ayed\\RubrosXproducto.dat'
    afSilos = 'K:\\ayed\\Silos.dat'

    alOperaciones = abrir(afOperaciones)
    alProductos = abrir(afProductos)
    alRubros = abrir(afRubros)
    alRubrosXproducto = abrir(afRubrosXproducto)
    alSilos = abrir(afSilos)
    
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
            msj(None)
        elif op == '7':
            validaciones('B',Registro_tara)
        elif op == '8':
            Reportes()
        elif op == '9':
            max_silo(),input(),os.system('cls')
            listado_rechazos(),input()
        op = valid_chr(m,'0123456789','Ingresar opcion')
    alOperaciones.close(), alProductos.close(), alRubros.close(), alRubrosXproducto.close(), alSilos.close()

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
        validaciones_prod(reg_p,baja_producto)
    elif op == 'C':
        lista_productos(reg_p), input()
    elif op == 'M':
        validaciones_prod(reg_p,modifica_producto)

def busca_producto(cod,reg_p):
    alProductos.seek(0)
    flag = False
    while not flag and alProductos.tell() < os.path.getsize(afProductos):
        pos = alProductos.tell()
        aux = pickle.load(alProductos)
        flag = True if int(aux.cod) == cod else False
    if flag:
        reg_p.cod = aux.cod
        reg_p.nombre = aux.nombre
        reg_p.activo = aux.activo
        return pos
    return -1

def validaciones_prod(reg_p,acceso):    
    cod = valid_int('codigo de producto')
    while cod != 0 :
        pos = busca_producto(cod,reg_p) 
        if pos == -1:
            print('El codigo no existe'), input()
        else:
            muestra_producto(reg_p), input()
            if not reg_p.activo:
                print('El producto ya fue dado de baja.'), input()
            else:
                acceso(reg_p,pos)
        cod = valid_int('codigo de producto')                        

def alta_producto(reg_p):  
    cod = valid_int('Codigo de producto')
    while cod != 0:
        if os.path.getsize(afProductos) == 0  or busca_producto(cod,reg_p) == -1:
            reg_p.nombre = input('Ingresar nombre de producto: ').capitalize()            
            reg_p.cod = cod
            reg_p.activo = True
            format_producto(reg_p); pickle.dump(reg_p,alProductos);alProductos.flush()            
        else:
            print('El producto ya existe'),input()
        cod = valid_int('Codigo de producto')

def muestra_producto(p):
    print(f'Codigo de producto: {p.cod} \nNombre : {p.nombre} \nEstado : {p.activo}')

def modifica_producto(reg_p,pos):
    if valid_chr('','SN','Modificar?S/N') == 'S':
        reg_p.nombre = input('Nombre: ')
        alProductos.seek(pos,0)
        format_producto(reg_p)
        pickle.dump(reg_p, alProductos)
        alProductos.flush()
        muestra_producto(reg_p), input()

def baja_producto(reg_p,pos):
    if valid_chr('','SN','Dar de baja?S/N') == 'S':
        reg_p.activo = False
        alProductos.seek(pos,0)
        pickle.dump(reg_p, alProductos)
        alProductos.flush()
        muestra_producto(reg_p), input()

def lista_productos(p):
    t = os.path.getsize(afProductos)
    if t != 0:
        alProductos.seek(0)
        print(' '*6,'PRODUCTO',' '*10,'CODIGO DE PRODUCTO',' '*10,'ESTADO\n','--'*35)
        while alProductos.tell() < t:
            p = pickle.load(alProductos)
            aux = 'Activo' if p.activo else 'Inactivo'
            print (f'\t{p.nombre.strip().ljust(26)} {p.cod.ljust(21)} {aux}')

def format_producto(f):
    f.cod = str(f.cod).ljust(10,' ')
    f.nombre = f.nombre.ljust(30,' ')

def Altas(op,x):
    if op == 'A':
        x()
    elif op in 'BCM':
        print('no se puede acceder'), input()

def busca_dico(cod,reg_r):         
    alRubros.seek(0)
    reg = pickle.load(alRubros)
    flag = False
    tam_reg = alRubros.tell()
    cant_reg = os.path.getsize(afRubros)//tam_reg    
    inicio = 0
    fin = cant_reg - 1
    while inicio <= fin and not flag:
        medio = (inicio + fin ) // 2
        alRubros.seek(medio*tam_reg)
        reg = pickle.load(alRubros)
        if int(reg.cod) == cod:
            flag = True        
        elif int(reg.cod) < cod:
            inicio = medio + 1
        else:
            fin = medio - 1            
    if flag: 
        reg_r.cod = reg.cod
        reg_r.nombre = reg.nombre
        return medio*tam_reg        
    else:
        return - 1   

def alta_Rubros():
    rubro = rubros()
    codigo = valid_int('codigo de rubro')
    while codigo != 0:
        if os.path.getsize(afRubros) == 0 or busca_dico(codigo,rubro) == -1:
            rubro.cod = codigo
            rubro.nombre = input('Ingresar nombre de rubro: ').capitalize()
            alRubros.seek(os.path.getsize(afRubros))
            format_rubros(rubro)
            pickle.dump(rubro,alRubros)  
            alRubros.flush()
            orden(alRubros,afRubros)
        else:
            print('rubro ya existe:')             
        codigo = valid_int('codigo de rubro')

def orden(al,af):
    al.seek(0)
    aux_i = pickle.load(al)
    tam_reg = al.tell()
    t = os.path.getsize(af)
    cant_reg = t // tam_reg
    for i in range(cant_reg - 1):
        for j in range(i+1, cant_reg):
            al.seek(i*tam_reg)
            aux_i = pickle.load(al)
            al.seek(j*tam_reg)
            aux_j = pickle.load(al)

            if int(aux_i.cod) > int(aux_j.cod):
                al.seek(i*tam_reg)
                pickle.dump(aux_j,al)
                al.seek(j*tam_reg)
                pickle.dump(aux_i,al) 

def format_rubros(rubro):
    rubro.cod = str(rubro.cod).ljust(10,' ')
    rubro.nombre = rubro.nombre.ljust(60,' ')

def alta_RubrosxProductos():
    reg_p = productos()
    rubrosX = rubrosXproducto()
    reg_rubro = rubros()
    cod_prod = producto_existe()    
    while cod_prod != 0:        
        cod_rubro = valid_int('Codigo de rubro')
        while busca_dico(cod_rubro,reg_rubro) == -1:
            cod_rubro = valid_int('El codigo de rubro no existe. Ingresar nuevamente')
        aux = busca_producto(cod_prod,reg_p)
        rubrosX.cod_rubro = cod_rubro        
        rubrosX.cod_producto = cod_prod              
        rubrosX.minmax[0] = valid_MinMax(0,100,f'Ingresar el nivel minimo de {reg_rubro.nombre.strip()} admitido para {reg_p.nombre.strip()}: ')            
        rubrosX.minmax[1] = valid_MinMax(0,100,f'Ingresar el nivel maximo de {reg_rubro.nombre.strip()} admitido para {reg_p.nombre.strip()}: ')
        format(rubrosX)
        pickle.dump(rubrosX,alRubrosXproducto);alRubrosXproducto.flush();os.system('cls')
        cod_prod = producto_existe()
    
def format_alRubrosXproducto(rubrosX):
    rubrosX.cod_rubro = str(rubrosX.cod_rubro).ljust(10)
    rubrosX.cod_producto = str(rubrosX.cod_producto).ljust(10)
    for i in range(2):
        rubrosX.minmax[i] = str(rubrosX.minmax[i]).ljust(10)

def alta_Silos():
    t = os.path.getsize(afSilos)
    s = silos()
    reg_p = productos()
    cod = valid_int('Ingresar codigo de silo')
    while cod != 0:
        if t == 0 or busca_silo(s,cod) == -1:
            s.cod_s = cod
            s.nombre = input('Ingresar nombre de silo: ')
            codigo = producto_existe()
            s.cod = codigo        
            format_silos(s)
            pickle.dump(s,alSilos)
            alSilos.flush()
        else: 
            print('el codigo de silo ya fue registrado.')            
        cod = valid_int('Ingresar codigo de silo')

def format_silos(s):
    s.cod_s = str(s.cod_s).ljust(10,' ')
    s.nombre = s.nombre.ljust(30,' ')
    s.cod = str(s.cod).ljust(10,' ')
    s.stock = str(s.stock).ljust(10,' ')

def busca_silo(s,cod):
    alSilos.seek(0)
    flag = False    
    while not flag and alSilos.tell() < os.path.getsize(afSilos):
        pos = alSilos.tell()
        aux = pickle.load(alSilos)
        flag = True if cod == int(aux.cod) else False
    if flag:
        s.cod_s = aux.cod_s
        s.nombre = aux.nombre
        s.cod = aux.cod
        s.stock = aux.stock
        return pos
    return -1        

def actualizar_silo(cod,peso_neto):
    s = silos()
    pos = busca_silo(s,cod)
    alSilos.seek(pos)
    stock = int(s.stock)
    stock += peso_neto
    s.stock = stock
    format_silos(s)
    pickle.dump(s,alSilos)
    alSilos.flush()

def max_silo():
    max = 0
    t = os.path.getsize(afSilos)
    alSilos.seek(0)
    s = pickle.load(alSilos)
    alSilos.seek(0)
    while alSilos.tell() < t:
        s = pickle.load(alSilos)           
        if int(s.stock) > max:
            max = int(s.stock)            
            maxNomb = s.nombre
    print(f'Silo con mayor stock: {maxNomb.strip()}; {max} Kgs ')

def Entrega_cupos():
    t = os.path.getsize(afOperaciones)
    reg_op = operaciones(); reg_p = productos()
    patente = valid_str('patente')
    while patente != '*':
        fecha = validar_fecha() 
        if t == 0 or busca_op(patente,reg_op) == -1:                      
            reg_op.cod = producto_existe()
            reg_op.patente = patente
            reg_op.fecha_cupo = fecha
            reg_op.estado = 'P'
            print(f'{patente} {alOperaciones.tell()}')               
            format_operaciones(reg_op)
            pickle.dump(reg_op,alOperaciones)            
            alOperaciones.flush()
        elif busca_op(patente,reg_op) != -1 and reg_op.fecha_cupo.strip() == fecha:
            print(f'La patente {patente} ya tiene cupo para esa fecha.'),input()
        patente = valid_str('Ingresar patente')

def producto_existe():
    reg_p = productos()
    cod = valid_int('Ingresar codigo de producto')
    while busca_producto(cod,reg_p) == -1 or not reg_p.activo:
        cod = valid_int(f'El producto no existe. Ingresar nuevamente')
    return cod

def format_operaciones(operacion):
    operacion.patente = operacion.patente.ljust(7,' ')
    operacion.cod = str(operacion.cod).ljust(10,' ')
    operacion.fecha_cupo = operacion.fecha_cupo.ljust(10,' ')
    operacion.bruto = str(operacion.bruto).ljust(10,' ')
    operacion.tara = str(operacion.tara).ljust(10,' ')
    operacion.estado = operacion.estado.ljust(1) 
            
def busca_op(patente,reg_op):
    t = os.path.getsize(afOperaciones)
    alOperaciones.seek(0)    
    flag = False
    while not flag and alOperaciones.tell() < t:
        pos = alOperaciones.tell()        
        reg = pickle.load(alOperaciones)
        flag = True if reg.patente.strip() == patente else False            
    if flag:
        reg_op.patente = reg.patente
        reg_op.cod = reg.cod
        reg_op.fecha_cupo = reg.fecha_cupo
        reg_op.estado = reg.estado
        reg_op.bruto = reg.bruto
        reg_op.tara = reg.tara
        return pos
    return -1

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
    reg_op.estado = 'A'
    alOperaciones.seek(pos)
    pickle.dump(reg_op,alOperaciones)
    alOperaciones.flush()
    
def registro_calidad(reg_op,pos):
    rubro = rubros(); rubrosX = rubrosXproducto()
    flag = False
    t = os.path.getsize(afRubrosXproducto)
    alRubrosXproducto.seek(0)
    lim = 0
    while alRubrosXproducto.tell() < t and not flag:
        rubrosX = pickle.load(alRubrosXproducto)
        if  int(reg_op.cod) == int(rubrosX.cod_producto):
            pos2 = alRubrosXproducto.tell()
            aux = busca_dico(rubrosX.cod_rubro,rubro)
            valor = valid_MinMax(0,100,f'Ingresar {rubro.nombre.strip()}:  (entre{rubrosX.minmax[0]} y {rubrosX.minmax[1]}): ')
            if valor > rubrosX.minmax[1] or valor < rubrosX.minmax[0]:
                lim += 1
            if pos2 == t or lim == 2: 
                flag = True  
    reg_op.estado = 'C' if lim < 2 else  'R'
    alOperaciones.seek(pos); format_operaciones(reg_op); pickle.dump(reg_op,alOperaciones);alOperaciones.flush()

def Registro_bruto(reg_op,pos):
    reg_op.bruto = valid_int('Ingresar peso bruto')
    reg_op.estado = 'B'
    alOperaciones.seek(pos)
    format_operaciones(reg_op)
    pickle.dump(reg_op,alOperaciones)
    alOperaciones.flush()

def Registro_tara(reg_op,pos):
    peso = valid_int('Ingresar peso tara')
    while peso >= int(reg_op.bruto):
        peso = valid_int('Ingresar peso tara')
    reg_op.tara = peso
    reg_op.estado = 'F'
    actualizar_silo(int(reg_op.cod),int(reg_op.bruto)-reg_op.tara)
    alOperaciones.seek(pos)
    format_operaciones(reg_op)
    pickle.dump(reg_op,alOperaciones)
    alOperaciones.flush()

def Reportes():
    orden(alOperaciones,afOperaciones)
    t = os.path.getsize(afOperaciones)
    alOperaciones.seek(0)
    reg_p = productos()
    reg_op = pickle.load(alOperaciones)
    tam_reg = alOperaciones.tell()
    cant_cupos, total_camiones,flag = 0,0,False
    print(' '*15,'TOTAL DE CAMIONES',' '*8, 'PESO NETO TOTAL',' '*8, ' PESO NETO PROMEDIO ',' '*8,'PATENTE MINIMA\n','--'*56 )
    while alOperaciones.tell() < t:
        cant_camiones = acum_neto = min = 0
        aux = reg_op.cod
        while  reg_op.cod == aux and alOperaciones.tell() < t:
            if reg_op.estado == 'F':
                neto = int(reg_op.bruto) - int(reg_op.tara)
                cant_camiones += 1                
                acum_neto += neto            
                if neto < min or min == 0:
                    min = neto
                    pat_min = reg_op.patente
            cant_cupos += 1
            reg_op = pickle.load(alOperaciones)  
            pos = alOperaciones.tell()          
            if  pos == t and not flag:
                atras = t - tam_reg
                alOperaciones.seek(atras)
                flag = True
        total_camiones += cant_camiones                    

        pos_prod = busca_producto(int(aux),reg_p); alProductos.seek(pos_prod)    
        print(f' {reg_p.nombre.strip().ljust(21)}  {str(cant_camiones).ljust(20)} {str(acum_neto).rjust(6)} {"Kgs".ljust(20)} {str(round(acum_neto / cant_camiones,2)).ljust(6)} {"Kgs".ljust(20)} {pat_min.ljust(20)} \n')
    print(f'\nTotal de cupos otorgados: {cant_cupos} \nTotal de camiones recibidos: {total_camiones}'), input()

def listado_rechazos():
    t = os.path.getsize(afOperaciones)
    alOperaciones.seek(0)
    fecha = validar_fecha(); os.system('cls')
    print(f'Listado de patentes rechazadas el dia {fecha}: \n')
    while alOperaciones.tell() < t:
        ops = pickle.load(alOperaciones)
        if fecha == ops.fecha_cupo and ops.estado == 'R':
            print(f' {ops.patente}')

principal()  