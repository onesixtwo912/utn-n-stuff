codigo = input('Ingresar codigo de producto: ')
while codigo !='*':
    aux = codigo
    while aux == codigo:
        cant_vend = int(input('Ingresar cantidad vendida: '))
        precio = float(input('Ingresar precio por unidad: '))
        descuento = input('descuento S/N: ')
        while descuento != 'S' and descuento != 'N':
            descuento = input('descuento S/N: ')
        if descuento == 'S':
            valor_desc = int(input('%:'))
            importe_venta = cant_vend * precio *valor_desc/100
        else:
            importe_venta = cant_vend * precio
        codigo = input('Ingresar codigo de producto: ')               
    print(f'producto: {aux} importe de ventas total : {importe_venta}')