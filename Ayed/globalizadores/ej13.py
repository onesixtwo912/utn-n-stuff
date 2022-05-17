impuestos = 0
n = int(input('Ingresar cantidad de empleados: '))
remuneracion = float(input('Ingresar remuneracion: '))
for k in range(1,n):
    horas = float(input('Ingresar horas: '))
    if horas > 140:
        salario = horas * remuneracion * 1.5
    else:  salario = horas * remuneracion
    impuesto = (salario-1000)*0.2 if salario > 1000 else 0
    print(f'Empleado {k} : {salario-impuesto} ')