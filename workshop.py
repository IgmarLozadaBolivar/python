'''
Se desea realizar un programa en el cual se ingresen números enteros, los cuales
se deben almacenar en una lista. Se debe ingresar números hasta que el número
ingresado sea 99999. Una vez creada la lista, se desea conocer cuales y cuántos
son pares e impares.
'''

#Inicializar un diccionario vacío para almacenar conteos pares e impares (Dictionary)
numCounts = {
    "even": 0,
    "odd": 0
}

#Inicializar una lista vacía para almacenar los números (List)
num_list = []

#Continúe aceptando números enteros hasta que se ingrese 99999 (Loop while, method append, break y conditionals)
while True:
    num = int(input("Ingrese un número hasta ingresar 99999 para finalizar: "))
    if num == 99999:
        break
    num_list.append(num)

#Contar el número de enteros pares e impares (Loop for y conditionals)
for num in num_list:
    if num % 2 == 0:
        numCounts["even"] += 1
    else:
        numCounts["odd"] += 1

#Imprimir los resultados (Imprimir)
print("Hay", numCounts["even"], "números pares y", numCounts["odd"], "números impares en la lista.")

'''
Ejercicio utilizando diccionarios, listas, bucle while y utilizando condicionales 
'''

from collections import Counter

#Inicializar una lista vacía para almacenar los números (List)
num_list = []

#Continúe aceptando números enteros hasta que se ingrese 99999 (Loop while y conditionals)
while True:
    num = int(input("Introduzca un número entero (99999 para detener): "))
    if num == 99999:
        break
    num_list.append(num)

#Cuente números pares e impares usando Counter (Function counter and lambda)
num_counts = Counter(num_list)
even_count = num_counts[lambda x: x % 2 == 0]
odd_count = num_counts[lambda x: x % 2 != 0]

#Imprimir los resultados (Print)
print("Hay", even_count, "números pares y", odd_count, "números impares en la lista.")

'''
Dada una lista con nombres completos de personas, realizar un programa que
genere una segunda con la cantidad de palabras de cada uno de los nombres. La
lista de nombres debe llenarse a través de nombres que se ingresan por teclado,
hasta que el nombre ingresado sea “FIN”.
Se debe imprimir la lista de nombres y la lista con la cantidad de palabras de cada
nombre.
'''

#Inicializar una lista vacía para almacenar nombres completos (List)
name_list = []

#Continúe aceptando nombres hasta que ingrese "FIN" (Loop while, function append, break and conditionals)
while True:
    name = input("Escriba un nombre completo para terminar de escribir FIN: ")
    if name == "FIN":
        break
    name_list.append(name)

#Crear un diccionario para almacenar la cantidad de palabras en cada nombre (Dictionary)
word_counts = {}

#Iterar a través de los nombres en la lista y contar las palabras (Loop for, function split and len)
for name in name_list:
    words = name.split()
    num_words = len(words)
    word_counts[name] = num_words

#Imprime los resultados (Print and loop for)
print("Lista de nombres:")
for name in name_list:
    print(name)
print()
print("Número de palabras en cada nombre:")
for name, count in word_counts.items():
    print(name, "-", count)

'''
Dada la siguiente información sobre las calificaciones de estudiantes de una institución educativa:
• Código
• Nombre
• Nota 1 (Peso de 30%)
• Nota 2 (Peso de 30%)
• Nota 3 (Peso de 40%)
El proceso se termina cuando el código que se ingrese sea 999.(Bandera)
Se pide calcular:
La nota definitiva de cada estudiante e indicar con un mensaje si aprobó o reprobó, utilizando funciones
Para aprobar, la nota deber ser mayor o igual a 3.0 y la información en su totalidad se debe almacenar
en listas.
'''

#Función para calcular la nota final de un alumno (Function and return)
def calculateNote(n1, n2, n3):
    nF = n1 * 0.3 + n2 * 0.3 + n3 * 0.4
    return nF

#Lista de diccionarios para almacenar información de los estudiantes (List)
students = []

#Ciclo para capturar datos de estudiantes (Loop while, function append, break and conditionals)
while True:
    StudentCode = int(input("Ingrese el código de estudiante para terminar, ingrese 999: "))
    if StudentCode == 999:
        break
    name = input("Ingrese el nombre del estudiante: ")
    n1 = float(input("Ingrese la nota 1 del estudiante: "))
    n2 = float(input("Ingrese la nota 2 del estudiante: "))
    n3 = float(input("Ingrese la nota 3 del estudiante: "))
    nF = calculateNote(n1, n2, n3)
    approved = nF >= 3.0
    student = {"Código estudiantil": StudentCode, "Nombre": name, "Nota 1": n1, "Nota 2": n2, "Nota 3": n3, "Nota Definitiva": nF, "Aprobacion": approved}
    students.append(student)

#Imprimir información del estudiante (Print's, loop for and conditionals)
for student in students:
    print("Código estudiantil:", student["Código estudiantil"])
    print("Nombre:", student["Nombre"])
    print("Nota 1:", student["Nota 1"])
    print("Nota 2:", student["Nota 2"])
    print("Nota 3:", student["Nota 3"])
    print("Nota definitiva:", student["Nota Definitiva"])
    if student["Aprobacion"]:
        print("Estado: Aprobado")
    else:
        print("Estado: Reprobado")
    print()

'''
Se realiza la compra de N artículos, en donde se ingresa el código del artículo y la cantidad y
mediante el uso de diccionarios para los nombres y valores unitarios de los artículos, el
programa debe obtener el nombre de cada artículo, cantidad comprada, valor unitario, valor
total de acuerdo a la cantidad comprada y finalmente calcular el valor total de la compra.
Se suministra el diccionario de nombres de artículo y otro con los valores unitarios.
• Articulos = {1:"Lapiz",2:"Cuadernos",3:"Borrador",4:"Calculadora",5:"Escuadra"}
• Valores = {1:2500,2:3800,3:1200,4:35000,5:3700}.
'''

#Lista de diccionarios para almacenar la información de los artículos comprados (Dictionary's)
articles = {1:"Lapiz", 2:"Cuadernos", 3:"Borrador", 4:"Calculadora", 5:"Escuadra"}
values = {1:2500, 2:3800, 3:1200, 4:35000, 5:3700}

#Lista de diccionarios para almacenar la información de los artículos comprados (list)
purchase = []

#Ciclo para capturar datos de artículos comprados (Loop while, function append, break and conditionals)
while True:
    itemCode = int(input("Introduce el código del artículo, para finalizar introduce 0: "))
    if itemCode == 0:
        break
    quantity = int(input("Ingrese el número de unidades compradas: "))
    name = articles[itemCode]
    unitValue = values[itemCode]
    totalValue = quantity * unitValue
    articles = {"Codigo Del Articulo": itemCode, "Nombre": name, "Cantidad": quantity, "Valor Unitario": unitValue, "Valor Total": totalValue}
    purchase.append(articles)

#Impresión de la información de los artículos comprados (Print's, loop for)
print("Purchase made:")
for articles in purchase:
    print("Codigo del articulo:", articles["Codigo Del Articulo"])
    print("Nombre del articulo:", articles["Nombre"])
    print("Cantidad:", articles["Cantidad"])
    print("Valor unitario:", articles["Valor Unitario"])
    print("Valor total:", articles["Valor Total"])
    print()

#Cálculo del valor total de compra (Print)
totalPurchaseValue = sum(articles["Valor Total"] for articles in purchase)
print("Valor total de la compra:", totalPurchaseValue)