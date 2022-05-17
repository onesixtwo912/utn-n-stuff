menores_total = total = 0
zona = input('Igresar zona: ')
while zona != '0':
    aux = zona
    cont = m15 = 0
    while zona == aux:
        sexo = input('Ingresar sexo: ').upper()
        while sexo != 'M' and sexo != 'F':
            sexo = input('Ingresar sexo: ').upper()
        edad = int(input('Ingresar edad: '))
        if sexo == 'M':
            cont, total = cont + 1, total + 1
            if edad < 15:
                m15, menores_total = m15 + 1, menores_total + 1 
        zona = input('Igresar zona: ')
    print(f'Zona:{aux}: %{m15/cont*100} varones menores de 15 años.') 
print(f'% {menores_total/total*100} varones menores de 15 años en el municipio.')