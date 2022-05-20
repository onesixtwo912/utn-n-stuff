cont = 1
n = int(input('Cantidad de numeros: '))
while n < 2:
    n = int(input('Cantidad de numeros: '))
aux = int(input('Ingresar numero: '))
nro = aux - 1
while nro < aux and nro != aux and n != cont:
    cont += 1
    nro = int(input('Ingresar numero: '))
print ('Estan ordenados.') if nro < aux else print ('No estan ordenados.')