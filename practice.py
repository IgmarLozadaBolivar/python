'''
Duplicar un numero leido. Esta tarea la debe realizar 15 veces.
'''

for i in range(15):
    num = int(input("Ingrese un número: "))
    num_duplicado = num * 2
    print("El número duplicado es:", num_duplicado)

'''
Elabore un DF que realice la sumatoria de 10 numeros entregados por el usuario.
'''

sumatoria = 0

for i in range(10):
    num = int(input("Ingrese un número: "))
    sumatoria += num

print("La sumatoria de los 10 números ingresados es:", sumatoria)

'''
Leer nombre del estudiante y tres notas para calcular el promedio de las tres notas y 
mostrar el resultado junto al nombre, ademas indicar si gano o perdio la materia. 
Se gana a partir de 3.0. EL programa debe realizar esta misma taread para 50 estudiantes.
'''

student = input("Ingrese el nombre del estudiante: ")
n1 = float(input("Ingrese la nota 1 del estudiante: "))
n2 = float(input("Ingrese la nota 2 del estudiante: "))
n3 = float(input("Ingrese la nota 3 del estudiante: "))
prom = (n1 + n2 + n3)/3
note = ()
while True:
    if (prom >= 3.0):
        print('Hola',student, 'tu promedio es: ',prom,)
        print('Felicidades, ganaste la materia!')
        break
    else:
        print('Hola',student,'tu promedio es: ',prom,)
        print('Lo siento, perdiste la materia')
        break

'''
Elabore un DF que realice la sumatoria de los numeros enteros comprendidos 
entre 1 y el 10, es decir, 1 + 2 + 3 + ... + 10.
'''

sumatoria = 0
for i in range(1, 11):
    sumatoria += i
print("La sumatoria es:", sumatoria)


'''
Elabore un algoritmo que lea varios numeros enteros y colocale su sumatoria. 
El proceso termina cuando el numero leido sea CERO. Resolver en pseudocodigo y con Diagrama de Flujo.
'''

sumatoria = 0

while True:
    num = int(input("Ingrese un número entero (0 para terminar): "))
    if num == 0:
        break
    sumatoria += num

print("La sumatoria de los números ingresados es:", sumatoria)

'''
Una pelota rebota varias veces y en cada oportunidad pierde el 10% de la
altura del rebote anterior. Si se dejo caer desde una altura A de 10 metros,
cuantas veces rebotara antes de alcanzar apenas 0,5 metros de altura?
'''

def rebotes_pelota(altura_inicial, factor_reduccion):
    altura_actual = altura_inicial
    rebotes = 0
    
    while altura_actual >= 0.5*altura_inicial:
        altura_actual *= factor_reduccion
        rebotes += 1
        
    return rebotes

rebotes = rebotes_pelota(10, 0.9)
print("La pelota rebota {} veces antes de alcanzar 0.5 metros de altura.".format(rebotes))

'''
Una pelota rebota varias veces y en cada oportunidad pierde el 10% de la
altura del rebote anterior. Si se dejo caer desde una altura A de 10 metros,
cuantas veces rebotara antes de alcanzar apenas 0,5 metros de altura?
'''

altura = 10.0  # altura inicial de la pelota
rebotes = 0    # contador de rebotes

while altura >= 0.5:
    altura = altura * 0.9   # altura del siguiente rebote
    rebotes += 1            # incrementar contador de rebotes

print("La pelota rebota", rebotes, "veces antes de alcanzar una altura de 0.5 metros.")
