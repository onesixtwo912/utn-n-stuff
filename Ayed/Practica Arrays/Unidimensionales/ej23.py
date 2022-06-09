def carga(x,k):
    for i in range(k):
        x[i] = int(input('Ingresar nro: '))

def merge(x,y,z):
    pos = posX = posY = 0
    while posX < m and posY < n:
        if x[posX] < y[posY]:
            z[pos] = x[posX]
            posX += 1
        else:
            z[pos] = y[posY]
            posY += 1
        pos += 1 
    if posX >= m:
        while posY < n:
            z[pos] = y[posY]
            posY += 1
            pos += 1
    else:
        while posX < m:
            z[pos] = x[posX]
            posX += 1
            pos += 1      

def muestra(x):
    for i in range(n+m):
        print(x [i])     

m, n = 5, 3; a, b, c = m*[0], n*[0], (m+n)*[0]
carga(a,m)        
carga(b,n)
merge(a,b,c)
muestra(c)