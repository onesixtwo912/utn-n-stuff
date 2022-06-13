def inicio():
    for i in range(m):
        hmax[i] = float(input(f'Horas maximas sin mantenimiento para la clase {chr(i+65)}: '))

def carga():
    for i in range(k):
        maq[i] = input(f'Clase: ').upper()
        while maq[i] < 'A' or maq[i] > chr(m+64):
            maq[i] = input(f'Clase: ').upper()
        hs[i] = float(input(f'Horas sin mantenimiento: '))

def lista():
    print(f'\t\t\t\tMaquinas que necesitan mantenimiento \n')
    print('                         Cantidad maxima')
    print('                           de horas sin        Cantidad de horas')
    print('Nro. Maquina   Clase       mantenimiento            que lleva        Exceso relativo')
    print('                           para su clase           funcionando')
    print('__________________________________________________________________________________\n')
    for i in range(k):
        t = hs[i]
        n = hmax[ord(maq[i])-65]
        if t > n:
            e = (t-n)/n
            print(f'{i:7}          {maq[i]:9} {n:7} {t:22} {e:20}')

k, m = 50,17 ;hmax, maq, hs = m*[0], k*[''], k*[0]
inicio()
carga()
lista()