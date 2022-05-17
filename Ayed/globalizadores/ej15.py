max = 0 
for k in range (1,11):
    monto = float(input('Ingresar monto: ')) 
    max, maxS = monto, k if monto < 30000 else print(f'Sucursal {k} recaudo mas de 30000. ')
print(f'Máximo monto facturado entre las sucursales que recaudaron menos de $30000: {max}')