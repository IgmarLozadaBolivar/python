""" personas = ["Juan Manuel", "Maria Paula", "Lina Maria", "Jhon Ceballos"]
print("\n\n\n")
for i in range(4):
    print(personas[i]) """
    
#num =  [[2, 8, 9, 8], 
        #[5, 8, 7, 5], 
        #[2, 8, 9, 6]]  
#for i in num:
    #for j in i:
        #print(j, end = " ")
    #print()
    
''' Crear una matriz como lista, ingresando nombre de estudiantes, nota 1, nota 2, nota 3, luego imprima la nota final'''

""" students = []
student = []
list = []
prom = []
n1 = []
n2 = []
n3 = []
nF1 = []
nF = []
options = []



print("\n")
print("STEPS TO ADD A STUDENT, THEIR GRADES AND SEE THEIR FINAL GRADE\n 1.Add student\n 2.Add notes\n 3.See final notes\n")
options = input("Press a key to continue: ")

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
print("STUDENTS", " N1", "  N2", "  N3", "  NF") """
#impresion = ""
#for student in students:
    #for i in range(5):
        #impresion += str(student[i]) + "\t\t"
        #impresion += "\n"
#print(impresion)
#print("\n")

"""Determinar en los meses de abril, mayo y junio el promedio 
de lluvias al mes, teniendo en cuenta los centimetros de lluvias por dia
(los valores de la crs de lluvia por dia pueden ser generados por 
medio de un numero aleatorio entre 0 y 11) y determinar cual fue el mes mas lluvioso en promedio"""

from random import randint

abril = []
mayo = []
junio = []
promAbr = 0
promMay = 0
promJun = 0

for i in range(31):
    if i<30:
        abril.append(randint(0,11))
        promAbr +=[i]
        mayo.append(randint(0,11))
        promMay +=[i]
        junio.append(randint(0,11))
        promJun +=[i]
    else:
        mayo.append(randint(11))
        promMay += mayo[i]
        
promAbr = round(promAbr/30, 2)
promMay = round(promMay/31, 2)
promJun = round(promJun/30, 2)

print("Abril\tMay\tJun\t")
print(promAbr, "\t", promMay, "\t", promJun, "\t")
if promAbr > promMay > promJun:
    print("El mes con mas lluvias fue Abril con ", promAbr, " de promedio mensual")
elif promMay > promAbr > promJun:
    print("El mes con mas lluvias fue Mayo con ", promMay, " de promedio mensual")
else:
    print("El mes con mas lluvias fue Junio con ", promJun, " de promedio mensual")
print("\n")
#numEstudiantes = int(input("Numero de estudiantes del grupo: "))
#estudiantes = []
#for i in range(numEstudiantes):
    #nombre = input("Ingrese el nombre del estudiante: ")
    #note1 = float(input("Ingrese su nota 1: "))
    #note2 = float(input("Ingrese su nota 2: "))
    #note3 = float(input("Ingrese su nota 3: "))
    #prom = (note1+note2+note3)/3
    #estudiantes.append(nombre, note1, note2, note3, prom)

#print("\nNOMBRE\t \tN1 \tN2 \tN3 \tNF")
#impresion = ""
#for i in estudiantes:
    #print(i[0], "\t\t", i[1], "\t\t", i[2], "\t\t", i[3], "\t\t", i[4])