cat1 = catR = 0
for i in range(50):
    importe = float(input('Ingresar importe: '))
    categoria = input('Ingresar categoria: ')
    if categoria == '1':
        print(f'Importe a abonar {importe - importe * 0.15} ')
        cat1 += importe
    else:
        print(f'Importe a abonar {importe - importe * 0.18} ')                
        catR += importe        
print(f'Importe total de las 50 facturas: {cat1 + catR} ')    
print(f'Importe total de las facturas de la categoria 1: {cat1} ')
print(f'Importe total de las facturas de la categorias restantes: {catR} ')