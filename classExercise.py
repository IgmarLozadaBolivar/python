# CODIGO SIMPLE

""" n = int(input('Ingrese el valor de N: '))
r = int(input('Ingrese el valor de R: '))
fn = 1
for i in range(1, n +1):
    fn = fn * i
nr = n-r
fnr = 1
for i in range(1, nr +1):
    fnr = fnr * i
fr = 1
for i in range(1, r +1):
    fr = fr * i
c = fn/(fnr * fr)
print(c)
 """

# DEFINIR FUNCION FACTORIAL

""" def fact(n):
    f = 1
    for i in range(1,n+1):
        f=f*i
    return(f)

n = int(input('Ingrese el valor de N: '))
r = int(input('Ingrese el valor de R: '))

c = fact(n)/(fact(n-r)*fact(r))
print(c)
 """

# DEFINIR FUNCION/JUEGO TORRES DE HANOI

def hanoi(p1,p2,p3,n):
    if n > 1:
        hanoi(p1,p2,p3,n -1)
        hanoi(p1,p2,p3, 1)
        hanoi(p1,p2,p3,n -1)
    else:
        print('Mover de', p1, 'a', p3)

n = int(input('Ingrese el valor de N: '))
hanoi('A','C','B',n)