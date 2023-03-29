print("\n\n")
import os

dicEstudiantes = {
    1: {
    "nombres": "aa",
    "apellidos": "aa",
    "correo": "a@abcd.com",
    },
    2: {
    "nombres": "bb",
    "apellidos": "bb",
    "correo": "b@abcd.com",
    },
    3: {
    "nombres": "cc",
    "apellidos": "cc",
    "correo": "c@abcd.com",
    },
    4: {
    "nombres": "dd",
    "apellidos": "dd",
    "correo": "d@abcd.com"
    },
}

dicMaterias = {
    1: {
    "nombre": "Matemáticas"
    },
    2: {
    "nombre": "Física"
    },
    3: {
    "nombre": "Lengua"
    },
    5: {
    "nombre": "Química"
    },
}

def verMenu():
    os.system("cls") #Limpia consola
    print("********** SISTEMA **********\n")
    print('''Selecciones alguna de las siguientes opciones: 
    1. Notas        2. Estudiantes
    3. Materias     0. Salir''')

#           MATERIAS

def verMenuMaterias(materias):
    os.system("clear") #Limpia consola
    print("********* MATERIAS *********\n")
    print("CÓDIGO\t\t\tNOMBRE")
    for materia in materias:
        print(materia,"\t\t\t",materias[materia]["nombre"])
    print('''Seleccione alguna de las siguientes opciones: 
    1. Crear        2. Editar
    3. Eliminar     0. Salir''')

def verMenuEstudiantes(estudiantes):
    os.system("clear") #Limpia consola
    print("********* ESTUDIANTES *********\n")
    print("CODIGO\t\t\tNOMBRE")
    for estudiante in estudiantes:
        print(estudiante, "\t\t\t",estudiantes[estudiante]["nombre"])
    print('''Seleccione alguna de las siguientes opciones: 
    1. Agregar      2. Editar
    3. Eliminar     0. Salir''')

verMenu()
opcMenu = input()
while opcMenu != "0":
    if opcMenu == "1":
        print("********* SISTEMA *********\n")
    elif opcMenu == "2":
        print("******** ESTUDIANTES ********\n")
        verMenuEstudiantes(dicEstudiantes)
        opc = input()
        while opc != "0":
            if opc == "1":
                print("********* AGREGAR *********\n")
                id = list(dicEstudiantes.keys())[len(dicEstudiantes)-1]+1
                print("Por favor ingrese el nombre del estudiante: ")
                nombre = input()
                dicEstudiantes[id] = {"nombre": nombre}
            elif opc == "2":
                print("********* EDITAR *********\n")
                id = list(dicEstudiantes.keys())[len(dicEstudiantes)-1]+1
                print("Por favor ingrese el nombre del nuevo estudiante: ")
                dicEstudiantes[id]["nombre"] = input()
            elif opc == "3":
                print("********* ELIMINAR *********\n")
                print("Por favor ingrese el codigo del estudiante a eliminar: ")
                id = int(input())
                del (dicEstudiantes[id])
                #dicEstudiantes[id]["nombre"] = input()
                #opc = input()

    elif opcMenu == "3":
        print("********* MATERIAS **********\n")
        verMenuMaterias(dicMaterias)
        opc = input()
        while opc != "0":
            if opc == "1":
                print("********* CREAR *********\n")
                id = list(dicMaterias.keys())[len(dicMaterias)-1]+1
                print("Por favor ingrese el nombre de la nueva materia: ")
                nombre = input()
                dicMaterias[id] = {"nombre": nombre}
            elif opc == "2":
                print("********* EDITAR *********\n")
                print("Por favor ingrese el código de la materia a editar: ")
                id = int(input())
                print("Por favor ingrese el nuevo nombre de la materia: ")
                dicMaterias[id]["nombre"] = input()
            elif opc== "3":
                print("******** ELIMINAR ********\n")
                print("Por favor ingrese el código de la materia a eliminar: ")
                id = int(input())
                del (dicMaterias[id])
                #dicMaterias[id]["nombre"] = input()
                #opc = input()
            else:
                print("Por favor, seleccione una opción válida\n")
            verMenuMaterias(dicMaterias)
            opc = input ()        
    else:
        print("Por favor, seleccione una opción válida\n")
    verMenu()
    opcMenu = input()