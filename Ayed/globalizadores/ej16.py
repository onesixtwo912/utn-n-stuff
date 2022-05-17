cant_a = cant_b = total_a = total_b = 0
n = int(input('Ingresar cantidad de ventas: '))
for k in range(n):
    codigo = input('Ingresar codigo: ').upper()
    while codigo not in 'AB':
        codigo = input('Ingresar codigo: ').upper()  
    precio = float(input('Ingresar precio: '))        
    cantidad = int(input('Ingresar cantidad de productos: '))
    importe = cantidad * precio
    importe -= importe * 0.2 if cantidad > 10 else 0
    if codigo == 'A':
        cant_a += cantidad ; total_a += importe
    else:
        cant_b += cantidad ; total_b += importe
print(f'Cantidad total vendida de los articulos A: {cant_a}; Importe total: {total_a} ')        
print(f'Cantidad total vendida de los articulos B: {cant_b}; Importe total: {total_b} ')        