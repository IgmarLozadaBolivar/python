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