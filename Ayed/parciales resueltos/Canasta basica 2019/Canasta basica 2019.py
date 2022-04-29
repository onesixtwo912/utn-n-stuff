import os
def menu():    
    os.system('cls')
    mostrarmenu = '1 - Cantidad de supermercados que cumplen con la canasta basica. \n2 - Supermercado de mayor costo total de compra. \n3 - Cantidad de supermercados que ofrecen lacteos. \n4 - Salir'
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
            print(f'El supermercado con mayor costo de compra es: {maxSuper}.')
        elif opcion == '3':
            print(f'{contL} supermercado/s cuentan con productos lacteos') 
        input()
        os.system('cls')
        print(mostrarmenu)
        opcion = input('Ingresar opcion: ')
        while opcion < '1' or opcion > '4':
            os.system('cls')
            print(mostrarmenu)
            opcion = input('Ingresar opcion: ')

def proceso():
    global acumCosto, contS, lact,rubro,precio
    acumCosto = contS = 0
    lact = False 
    for i in range (60):
        stock = input(f'El producto {i} esta en existencia? S/N: ').upper()
        while stock != 'S' and stock != 'N':
            stock = input(f'El producto {i} esta en existencia? S/N: ').upper()
        if stock == 'S':
            rubro = input('Ingresar rubro: ').upper()
            while rubro != 'C' and rubro != 'L' and rubro != 'A' and rubro != 'V':
                rubro = input('Ingresar rubro: ').upper()

            contS = contS + 1
            precio = float(input('Ingresar precio: '))
            acumCosto = acumCosto + precio
            if rubro == 'L':
                lact = True

def proceso2():
    global maxSuper,max,contL
    print (f'El costo de productos en existencia es {acumCosto}.')
    if contS/60*100 > 75:
        print(F'{super} cumple con la canasta basica.')
        cumplen = cumplen + 1
    else:
        print(F'{super} No cumple con la canasta basica.')
    if acumCosto > max:
        max = acumCosto
        maxSuper = super
    if lact:
        contL = contL + 1        

max = contL = cumplen = 0
super = input('Ingresar el nombre del supermercado: ')
while super != '*':
    proceso()
    proceso2()
    super = input('Ingresar el nombre del supermercado: ')
menu()
