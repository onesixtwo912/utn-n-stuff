import os
def login(password,acceso):
    global pw, intentos;os.system('cls')
    pw = input('ingresar password: ')
    intentos = 0
    while intentos < 2 and pw != password:
        intentos = intentos + 1
        pw = input('password incorrecto. Intente nuevamente: ')
    if pw == password:
        acceso()
    else:
        print('Ha superado el limite de ingresos erroneos.')
