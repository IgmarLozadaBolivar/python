#personas = ["Juan Manuel", "Maria Paula", "Lina Maria", "Jhon Ceballos"]
#print("\n\n\n")
#for i in range(4):
    #print(personas[i])
    
"""num =  [[2, 8, 9, 8], 
        [5, 8, 7, 5], 
        [2, 8, 9, 6]]  
for i in num:
    for j in i:
        print(j, end = " ")
    print()"""
    
''' Crear una matriz como lista, ingresando nombre de estudiantes, nota 1, nota 2, nota 3, luego imprima la nota final'''


students = []
list = []
n1 = []
n2 = []
n3 = []
notes = []
nF1 = []
nF = []

for i in range(2):
    print("\n")
    list = str(input("Enter your name: "))
    n1 = float(input("Enter your note 1: "))
    n2 = float(input("Enter your note 2: "))
    n3 = float(input("Enter your note 3: ")) 
    for j in range(1):
        students.append(list)
        students.append(n1)
        students.append(n2)
        students.append(n3)
        nF1 = (n1 + n2 + n3)
        nF = (nF1/3)
        students.append(nF)

print("\n")        
print("STUDENTS", " N1", "  N2", "  N3", "  NF")
print(students)
print("\n")
