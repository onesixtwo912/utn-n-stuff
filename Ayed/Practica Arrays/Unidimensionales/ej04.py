def carga(lista):
    for i in range(n):
        lista[i] = (input(f'Ingresar caracter: '))

def muestra(lista):
    for i in range(n):
        print(f'Valor: {lista[i]}; posicion {i}.' ) if lista[i] != '*' else 0

n = 3; A = n*['']
carga(A)
muestra(A)