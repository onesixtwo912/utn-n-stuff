def total(x,y):
    total = 0
    for i in range(n-1):
        j = 0
        while x[i] != y[j] and j < n-1:
            j += 1
        if x[i] == y[j]:
            total += 1 
    return total
n = 5
a = input('Nombre: ')
b = input('Nombre: ')
print(f'Cnatidad de letras en comun: {total(a,b)}')