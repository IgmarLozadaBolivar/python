'''
Se desea realizar un programa en el cual se ingresen números enteros, los cuales
se deben almacenar en una lista. Se debe ingresar números hasta que el número
ingresado sea 99999. Una vez creada la lista, se desea conocer cuales y cuántos
son pares e impares.
'''

'''
Ejercicio utilizando diccionarios, listas, bucles como while y for y utilizando condicionales 
'''

#Initialize an empty dictionary to store even and odd counts (Dictionary)
numCounts = {
    "even": 0,
    "odd": 0
}

#Initialize an empty list to store the numbers (List)
num_list = []

#Keep accepting integers until 99999 is entered (Loop while, function append, break and conditionals)
while True:
    num = int(input("Enter a number until you enter 99999 to finish: "))
    if num == 99999:
        break
    num_list.append(num)

#Count the number of even and odd integers (Loop for and conditionals)
for num in num_list:
    if num % 2 == 0:
        numCounts["even"] += 1
    else:
        numCounts["odd"] += 1

#Print the results (Print)
print("There are", numCounts["even"], "even numbers and", numCounts["odd"], "odd numbers in the list.")

'''
Ejercicio utilizando diccionarios, listas, bucle while y utilizando condicionales 
'''

from collections import Counter

#Initialize an empty list to store the numbers (List)
num_list = []

#Keep accepting integers until 99999 is entered (Loop while and conditionals)
while True:
    num = int(input("Enter an integer (99999 to stop): "))
    if num == 99999:
        break
    num_list.append(num)

#Count even and odd numbers using Counter (Function counter and lambda)
num_counts = Counter(num_list)
even_count = num_counts[lambda x: x % 2 == 0]
odd_count = num_counts[lambda x: x % 2 != 0]

#Print the results (Print)
print("There are", even_count, "even numbers and", odd_count, "odd numbers in the list.")

'''
Dada una lista con nombres completos de personas, realizar un programa que
genere una segunda con la cantidad de palabras de cada uno de los nombres. La
lista de nombres debe llenarse a través de nombres que se ingresan por teclado,
hasta que el nombre ingresado sea “FIN”.
Se debe imprimir la lista de nombres y la lista con la cantidad de palabras de cada
nombre.
'''

'''
Ejercicio utilizando diccionarios, listas, bucles como while, for y utilizando condicionales
'''

#Initialize an empty list to store fully qualified names (List)
name_list = []

#Keep accepting names until "END" is entered (Loop while, function append, break and conditionals)
while True:
    name = input("Type a full name to finish typing END: ")
    if name == "END":
        break
    name_list.append(name)

#Create a dictionary to store the number of words in each name (Dictionary)
word_counts = {}

#Iterate through the names in the list and count the words (Loop for, function split and len)
for name in name_list:
    words = name.split()  # Divide
    num_words = len(words)  # Cuenta
    word_counts[name] = num_words  # Almacena

#Print the results (Print and loop for)
print("List of names:")
for name in name_list:
    print(name)
print()
print("Number of words in each name:")
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

#Function to calculate the final grade of a student (Function and return)
def calculateNote(n1, n2, n3):
    nF = n1 * 0.3 + n2 * 0.3 + n3 * 0.4
    return nF

#List of dictionaries to store student information (List)
students = []

#Cycle to capture student data (Loop while, function append, break and conditionals)
while True:
    StudentCode = int(input("Enter student code to finish, enter 999: "))
    if StudentCode == 999:
        break
    name = input("Enter student name: ")
    n1 = float(input("Enter the student's note 1: "))
    n2 = float(input("Enter the student's note 1: "))
    n3 = float(input("Enter the student's note 1: "))
    nF = calculateNote(n1, n2, n3)
    approved = nF >= 3.0
    student = {"Student Code": StudentCode, "Name": name, "note1": n1, "note2": n2, "note3": n3, "finalNote": nF, "approved": approved}
    students.append(student)

#Printing student information (Print's, loop for and conditionals)
for student in students:
    print("Student Code:", student["Student Code"])
    print("Name:", student["nombre"])
    print("Note 1:", student["note1"])
    print("Note 2:", student["note2"])
    print("Note 3:", student["note3"])
    print("Definitive Note:", student["finalNote"])
    if student["approved"]:
        print("State: Approved")
    else:
        print("State: Reproached")
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

#Dictionary list to store the information of purchased items (Dictionary's)
articles = {1:"Pencil", 2:"Notebooks", 3:"Draft", 4:"Calculator", 5:"Square"}
values = {1:2500, 2:3800, 3:1200, 4:35000, 5:3700}

#Dictionary list to store the information of purchased items (list)
purchase = []

#Cycle to capture data from purchased items (Loop while, function append, break and conditionals)
while True:
    itemCode = int(input("Enter the item code, to finish enter 0: "))
    if itemCode == 0:
        break
    quantity = int(input("Enter the number of units purchased: "))
    name = articles[itemCode]
    unitValue = values[itemCode]
    totalValue = quantity * unitValue
    articles = {"itemCode": itemCode, "Name": name, "Quantity": quantity, "unitValue": unitValue, "totalValue": totalValue}
    purchase.append(articles)

#Printing the information of the purchased items (Print's, loop for)
print("Purchase made:")
for articles in purchase:
    print("Item Code:", articles["itemCode"])
    print("Name:", articles["Name"])
    print("Quantity:", articles["Quantity"])
    print("Unit Value:", articles["unitValue"])
    print("Total Value:", articles["totalValue"])
    print()

#Calculation of the total purchase value (Print)
totalPurchaseValue = sum(articles["totalValue"] for articles in purchase)
print("Total Purchase Value:", totalPurchaseValue)