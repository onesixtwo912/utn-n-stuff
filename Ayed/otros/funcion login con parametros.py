import os
def login(password,acceso):
    global pw, intentos
    os.system('cls')
    pw = input('ingresar password: ')
    intentos = 0
    while intentos < 2 and pw != password:
        intentos = intentos + 1
        print('password incorrecto. Intente nuevamente')
        pw = input('ingresar password: ')
    if pw == password:
        return acceso()
    else:
        print('Ha superado el limite de ingresos erroneos.')
