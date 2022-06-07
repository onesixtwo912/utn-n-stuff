def carga(x,y):
    for i in range(n):
        x[i] = input('alumno: ')
        y[i] = float(input('nota: '))
        while y[i] < 1 or y[i]> 10:
            y[i] = float(input('nota: '))

def busqueda(x,y):
    dni = input('dni: ')
    while dni != '0':
        i = 0
        while dni != x [i] and i < n-1:
            i += 1
        print(f'El alumno con DNI {x[i]} tiene nota: {y[i]} ') if dni == x [i] else print('No tengo alumnos con esa nota')
        dni = input('dni: ')
n = 30; alumno,nota = n*[''], n*[0]
carga(alumno,nota)
busqueda(alumno,nota)