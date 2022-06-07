def carga(lista):
    for i in range(n):
        lista[i] = float(input(f'Ingresar nota: '))

def calculo(lista):
    prom =  cont = 0
    for i in range(n):
        prom += lista[i]
    prom /= n
    for i in range(n):
        cont += 1 if lista[i] > prom else 0
    return cont

n = 5; notas = n*[0]    
carga(notas)
print(f'{calculo(notas)} alumnos superaron el promedio de notas.')