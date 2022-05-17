saldo_cc = saldo_ca = cc = ca = saldo_total = 0
cantidad_ctas = int(input('Ingresar cantidad de cuentas: '))
for k in range(cantidad_ctas):
    tipo_cta = input('Ingresar tipo de cuenta: ').upper()
    while tipo_cta not in 'AC':
        tipo_cta = input('Ingresar tipo de cuenta: ').upper()
    saldo = float(input('Ingresar saldo: '))        
    saldo_total += saldo
    if tipo_cta == 'A':
        saldo_ca += saldo ; ca += 1
    else:
        saldo_cc += saldo ; cc += 1
print(f'Promedio de saldo CA: ${saldo_ca/ca} \nPromedio de saldo CC: ${saldo_cc/cc} ')
print(f'Saldo total del banco: ${saldo_cc + saldo_ca}.')      