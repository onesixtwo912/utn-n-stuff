pos = 0
texto = input('Ingresar texto: ').lower()
while texto[pos] != ',' and len(texto)-1 != pos:
    pos += 1
print (f'La primera coma se encontro en la posicion {pos}.') if texto[pos] == ',' else print ('no se encontro ninguna coma en el texto.')