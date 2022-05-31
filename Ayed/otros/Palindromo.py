texto = input('ingresar texto: ').replace(' ','').lower()
while texto != '*':
    i = 0
    while texto[i] == texto[len(texto)-1-i] and i < len(texto)// 2:
        i = i + 1
    print ('es un palindromo') if texto[i] == texto[len(texto)-1-i] else print ('no es no palindromo')
    texto = input('ingresar texto: ').replace(' ','').lower()
