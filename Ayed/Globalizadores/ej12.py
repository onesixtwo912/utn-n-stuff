texto = input('Ingresar texto: ').lower()
letra = input('Ingresar letra: ').lower()
cont = 0 
for pos in range(len(texto)-1):
    cont += 1 if texto [pos] == letra and texto [pos+1] in ',. )"' else 0
if texto[(len(texto)-1)] == letra: 
    print (f'{cont+1} palabras terminan con la letra {letra}. ') 
else: 
    print (f'{cont} palabras terminan con la letra {letra}. ')
