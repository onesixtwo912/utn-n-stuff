for k in range(20):
    acum = cont = 0
    elemento = int(input('Ingresar elemento: '))
    while elemento != 0:
        acum += elemento; cont += 1
        elemento = int(input('Ingresar elemento: '))
    print(f'El promedio del subconjunto {k} es {acum/cont}.')