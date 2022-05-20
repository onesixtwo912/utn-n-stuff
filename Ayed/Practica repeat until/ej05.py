pos = 0
texto = input('ingresar Texto: ')
while texto[pos] != ';' and pos != len(texto)-1:
    pos += 1
print(f'Se encontro en la posicion: {pos}') if texto[pos] == ';' else print(f'No se encontro.')