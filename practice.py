'''Duplicar un numero leido. Esta tarea la debe realizar 15 veces'''


'''Leer nombre del estudiante y tres notas para calcular el promedio de las tres notas y 
mostrar el resultado junto al nombre, ademas indicar si gano o perdio la materia. 
Se gana a partir de 3.0. EL programa debe realizar esta misma taread para 50 estudiantes.'''

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


'''Elabore un DF que realice la sumatoria de los numeros enteros comprendidos 
entre 1 y el 10, es decir, 1 + 2 + 3 + ... + 10'''
