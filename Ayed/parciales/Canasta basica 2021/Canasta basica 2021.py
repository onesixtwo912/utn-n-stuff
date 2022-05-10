import os
def menu(): 
    mostrarmenu = '1 - Cantidad de supermercados que cumplen con la canasta basica. \n2 - Supermercado de menor costo total de compra. \n3 - Cantidad de supermercados que ofrecen lacteos y carnes. \n4 - Salir'
    opcion = input(f'{mostrarmenu} \nIngresar opcion: '); os.system('cls')	
    while opcion < '1' or opcion > '4': 
        opcion = input(f'{mostrarmenu} \nIngresar opcion: '); os.system('cls')
    while opcion != '4':
        if opcion == '1':
            print(f'{cumplen} supermercados cumplen con la canasta basica.')
        elif opcion == '2':
            print(f'El supermercado con menor costo de compra es: {minSuper}.')
        elif opcion == '3':
            print(f'{lc} supermercado/s ofrecen lacteos y carnes') 
        input(); os.system('cls')
        opcion = input(f'{mostrarmenu} \nIngresar opcion: ') ;os.system('cls')	
        while opcion < '1' or opcion > '4':
            opcion = input(f'{mostrarmenu} \nIngresar opcion: ') ;os.system('cls')	

def carga():
    global contR, acumPrecio, stock, cantidad, precio,l,c,lc
    contR = acumPrecio = stock = 0 ; l = c = False
    rubro = input('Ingresar rubro: ').upper()
    while rubro != 'C' and rubro != 'L' and rubro != 'A' and rubro != '*':
        rubro = input('Ingresar rubro: ').upper() 
    while rubro != '*' and contR <= 2:
        l = True if rubro == 'C' else 0 ; c = True if rubro == 'L' else 0
        cantidad = int(input('Ingresar cantidad: '))
        precio = float(input('Ingresar precio: '))
        stock, acumPrecio, contR = (stock + cantidad), (acumPrecio + precio), (contR + 1)
        if contR <= 2:
            rubro = input('Ingresar rubro: ').upper()
            while rubro != 'C' and rubro != 'L' and rubro != 'A' and rubro != '*':
                rubro = input('Ingresar rubro: ').upper()
    lc = lc + 1 if l and c else 0

def proceso():
    global minSuper, cumplen ; os.system('cls')
    if stock > 1000:
        print(F'{super} cumple con la canasta basica.')
        cumplen = cumplen + 1
    else:
        print(F'{super} No cumple con la canasta basica.')
    input()
    min, minSuper = acumPrecio, super if acumPrecio < min or min == 0 else 0

min = lc = cumplen = 0
os.system('cls')
super = input('Ingresar el nombre del supermercado: ')
while super != '*':
    carga()
    proceso(); os.system('cls')
    super = input('Ingresar el nombre del supermercado: ')
menu()