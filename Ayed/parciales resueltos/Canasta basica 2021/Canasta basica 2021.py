import os
def menu():    
    os.system('cls')
    mostrarmenu = '1 - Cantidad de supermercados que cumplen con la canasta basica. \n2 - Supermercado de menor costo total de compra. \n3 - Cantidad de supermercados que ofrecen lacteos y carnes. \n4 - Salir'
    print(mostrarmenu)
    opcion = input('Ingresar opcion: ')
    while opcion < '1' or opcion > '4':
        os.system('cls')
        print(mostrarmenu)
        opcion = input('Ingresar opcion: ')

    while opcion != '4':
        if opcion == '1':
            print(f'{cumplen} supermercados cumplen con la canasta basica.')
        elif opcion == '2':
            print(f'El supermercado con menor costo de compra es: {minSuper}.')
        elif opcion == '3':
            print(f'{lc} supermercado/s ofrecen lacteos y carnes') 
        input()
        os.system('cls')
        print(mostrarmenu)
        opcion = input('Ingresar opcion: ')
        while opcion < '1' or opcion > '4':
            os.system('cls')
            print(mostrarmenu)
            opcion = input('Ingresar opcion: ')

def carga():
    global contR, acumPrecio, stock, cantidad, precio,l,c,lc
    contR = acumPrecio = stock = 0
    l = False
    c = False
    rubro = input('Ingresar rubro: ').upper()
    while rubro != 'C' and rubro != 'L' and rubro != 'A' and rubro != '*':
        rubro = input('Ingresar rubro: ').upper() 
    while rubro != '*' and contR <= 2:
        if rubro == 'C':
            l = True
        elif rubro == 'L': 
            c = True  
        cantidad = int(input('Ingresar cantidad: '))
        precio = float(input('Ingresar precio: '))
        stock = stock + cantidad
        acumPrecio = acumPrecio + precio
        contR = contR + 1
        if contR <= 2:
            rubro = input('Ingresar rubro: ').upper()
            while rubro != 'C' and rubro != 'L' and rubro != 'A' and rubro != '*':
                rubro = input('Ingresar rubro: ').upper()
    if l and c:
        lc = lc + 1

def proceso():
    global minSuper, cumplen,min
    os.system('cls')
    if stock > 1000:
        print(F'{super} cumple con la canasta basica.')
        cumplen = cumplen + 1
    else:
        print(F'{super} No cumple con la canasta basica.')
    input()
    if acumPrecio < min or min == 0:
        min = acumPrecio
        minSuper = super    

min = lc = cumplen = 0
os.system('cls')
super = input('Ingresar el nombre del supermercado: ')
while super != '*':
    carga()
    proceso()
    os.system('cls')
    super = input('Ingresar el nombre del supermercado: ')
menu()
