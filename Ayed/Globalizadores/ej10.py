a = e = i = o = u = 0
texto = input('Ingresar texto: ').upper()
for k in range(len(texto)):
    if texto [k] == 'A': a += 1
    elif texto [k] == 'E': e += 1
    elif texto [k] == 'I': i += 1
    elif texto [k] == 'O': o += 1
    elif texto [k] == 'U': u += 1
print (f'A:{a}, E: {e}, I: {i}, O: {o}, U: {u} ')