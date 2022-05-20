total = 0
codigo = input('Ingresar codigo: ')
while codigo != '*':
    cantidad = int(input('Ingresar cantidad: ')) 
    precio = float(input('Ingresar precio: '))
    total += cantidad*precio
    codigo = input('Ingresar codigo: ')
print(f'Total: {total}')