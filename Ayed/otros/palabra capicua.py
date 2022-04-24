import math
palabra = input('ingresar palabra: ')
while palabra != '*': 
    palabra = palabra.replace(' ','')
    k = 0
    c = (math.ceil((len(palabra)-1-k)/2))
    while palabra[k] == palabra[len(palabra)-1-k] and c != k:
        k = k + 1       
    if palabra[k] == palabra[len(palabra)-1-k]:
        print ('es capicua')
    else: 
        print ('no es capicua')
    palabra = input('ingresar otra palabra: ')           
print('fin')
