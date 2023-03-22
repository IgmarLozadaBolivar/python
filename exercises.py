students = [[], []]

size = 3
for i in range(size):
    print("Ingrese sus datos")
    student = input("Enter your name: ")
    n1 = float(input("Enter your note #1: "))
    n2 = float(input("Enter your note #2: "))
    n3 = float(input("Enter your note #3: "))
    nF1 = (n1 + n2 + n3)
    nF = (nF1/3)
    students[0].append(student)
    students[1].append(nF)


for i in range(size):
    print("Nombre:", students[0][i])
    print("Nota Final:", students[1][i])
