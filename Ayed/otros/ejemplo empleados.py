import os, os.path, pickle, datetime, io

class empleado:
    def __init__(self):
        self.legajo = 0
        self.nombre = ''
        self.sueldo = 0
        self.activo = True

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

def valid_MinMax(min,max,texto):
    k = valid_int(texto)
    while k < min or k > max:
        k = valid_int(texto)
    return k

def busqueda(leg):
    global afEmpleado,alEmpleado
    size = os.path.getsize(afEmpleado)
    alEmpleado.seek(0,0)
    flag = False
    aux = empleado()
    while not flag and alEmpleado.tell() < size:
        pos = alEmpleado.tell()
        aux = pickle.load(alEmpleado)
        flag = True if aux.legajo == leg else False
    if aux.legajo == leg:
        return pos
    return - 1


def alta_empleado():
    os.system('cls')
    legajo = valid_MinMax(1,999,'legajo')
    if busqueda(legajo) == -1:
        emp.legajo = legajo
        emp.nombre = input('Nombre: ')
        emp.sueldo = valid_int('Sueldo')
        pickle.dump(emp, alEmpleado)
        alEmpleado.flush()
    else: print('el empleado ya existe en el archivo.'),input()


def baja_empleado():
    print ('---'),input()

def muestra_empleado(emp):
    print(f'legajo: {emp.legajo}')
    print(f'nombre: {emp.nombre}')
    print(f'sueldo: {emp.sueldo}')
    print(f'estado: {emp.activo}'),input(), os.system('cls')


def modifica_empleado():
    global alEmpleado, afEmpleado
    legajo = valid_MinMax(1,999,'legajo')
    pos = busqueda(legajo)
    if pos >= 0:
        emp = pickle.load(alEmpleado)
        alEmpleado.seek(pos)
        muestra_empleado(emp)
        if emp.activo:
            emp.nombre = input('Nombre: ')
            emp.sueldo = valid_int('Sueldo')
            pickle.dump(emp, alEmpleado)
            alEmpleado.flush()
            muestra_empleado(emp)
    else:
        print('el legajo no existe.'), input()            


def listar_empleados():
    print ('---'),input()    


def ABM():
    m = (f'ABM Empleados \n\n 1 - Alta \n 2 - Baja \n 3 - Modificacion \n 4 - Listado de empleados activos \n 5 - Salir\n\n ')
    op = '-1'
    while op != '5':
        if op == '1':
            alta_empleado()
        if op == '2':
            baja_empleado()
        if op == '3':
            modifica_empleado()
        if op == '4':
            listar_empleados()
        op = valid_chr(m,'12345','opcion')

def main():
    global afEmpleado, emp, alEmpleado
    emp = empleado()
    afEmpleado = 'K:\\ayed\\emp.dat'
    #arEmpleado = open(arEmpleado,'w+b') if not os.path.exists(arEmpleado) else open(arEmpleado,'r+b')
    if not os.path.exists(afEmpleado):
        alEmpleado = open(afEmpleado,'w+b')
    else:
        alEmpleado = open(afEmpleado,'r+b')
    ABM()

main()
alEmpleado.close()