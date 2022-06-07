def resultado(x,fin):
    i = 0
    while x [i] == x [fin-1-i] and i < fin // 2:
        i = i + 1
    print ('Es un palindromo') if x [i] == x [fin-1-i] else print ('No es un palindromo')

texto = input('ingresar texto: ').replace(' ','').lower()
while texto != '*':
    fin = len(texto)
    resultado(texto, fin)
    texto = input('ingresar texto: ').replace(' ','').lower()