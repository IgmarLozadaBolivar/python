print("\n\n")
import os

dicNotas = {

}

dicEstudiantes = {
    1: {
    "nombre": "Juan",
    "apellido": "Garcia",
    "correo": "juan@gmail.com"
    },
    2: {
    "nombre": "Adrian",
    "apellido": "Martinez",
    "correo": "adrian@gmail.com"
    },
    3: {
    "nombre": "Laura",
    "apellido": "Lopez",
    "correo": "laura@gmail.com"
    },
    4: {
    "nombre": "Jessica",
    "apellido": "Muñoz",
    "correo": "jessica@gmail.com"
    }
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
    4: {
    "nombre": "Química"
    }
}

def verMenu():
    os.system("cls") 
    print("********** SISTEMA **********\n")
    print('''Seleccione una de las siguientes opciones: 
    1. Notas        2. Estudiantes
    3. Materias     0. Salir''')

#           NOTAS
def verMenuNotas(notas):
    os.system("clear")
    print("********* NOTAS *********\n")
    print("CODIGO\t\tNOTA")
    for nota in notas:
        print(nota,"\t\t\t",notas[nota]["nombre"])
    print('''Seleccione una de las siguientes opciones:
    1. Agregar        2. Editar
    3. Eliminar     0. Salir''')

#           ESTUDIANTES
def verMenuEstudiantes(estudiantes):
    os.system("clear") 
    print("********* ESTUDIANTES *********\n")
    print("CODIGO\t\t\tNOMBRE\t\t\tAPELLIDO\t\t\tCORREO")
    for estudiante in estudiantes:
        print(estudiante,"\t\t\t",estudiantes[estudiante]["nombre"],"\t\t\t",estudiantes[estudiante]["apellido"],"\t\t\t",estudiantes[estudiante]["correo"])
    print('''Seleccione una de las siguientes opciones: 
    1. Agregar      2. Editar
    3. Eliminar     0. Salir''')

#           MATERIAS
def verMenuMaterias(materias):
    os.system("clear") 
    print("********* MATERIAS *********\n")
    print("CÓDIGO\t\tMATERIA")
    for materia in materias:
        print(materia,"\t\t\t",materias[materia]["nombre"])
    print('''Seleccione una de las siguientes opciones: 
    1. Crear        2. Editar
    3. Eliminar     0. Salir''')

verMenu()
opcMenu = input()
while opcMenu != "0":
    if opcMenu == "1":
        print("********* NOTAS *********\n")
        verMenuNotas(dicNotas)
        opc = input()
        while opc != "0":
            if opc == "1":
                print("********* AGREGAR *********")
    elif opcMenu == "2":
        print("******** ESTUDIANTES ********\n")
        verMenuEstudiantes(dicEstudiantes)
        opc = input()
        while opc != "0":
            if opc == "1":
                print("********* AGREGAR *********\n")
                id = list(dicEstudiantes.keys())[len(dicEstudiantes.keys())-1]+1
                print("Por favor ingrese el nombre del estudiante: ")
                nombre = input()
                print("Por favor ingrese el apellido del estudiante: ")
                apellido = input()
                print("Por favor ingrese el correo del estudiante: ")
                correo = input()
                dicEstudiantes[id] = {"nombre": nombre, "apellido": apellido, "correo": correo}
                """ dicEstudiantes[id] = {"nombre": nombre}
                print("Por favor ingrese el apellido del estudiante: ")
                id2 = list(dicEstudiantes.keys())[len(dicEstudiantes.keys())-1]+1
                apellido = input()
                dicEstudiantes[id2] = {"apellido": apellido}
                print("Por favor ingrese el correo del estudiante: ")
                id3 = list(dicEstudiantes.keys())[len(dicEstudiantes.keys())-1]+1
                correo = input()
                dicEstudiantes[id3] = {"correo": correo} """
            elif opc == "2":
                print("********* EDITAR *********\n")
                print("Por favor ingrese el código del estudiante a editar: ")
                id = int(input())
                print("Por favor ingrese el nombre del nuevo estudiante: ")
                dicEstudiantes[id]["nombre"] = input()
                print("Por favor ingrese el apellido del estudiante: ")
                dicEstudiantes[id]["apellido"] = input()
                print("Por favor ingrese el correo del estudiante: ")
                dicEstudiantes[id]["correo"] = input()

            elif opc == "3":
                print("********* ELIMINAR *********\n")
                print("Por favor ingrese el codigo del estudiante a eliminar: ")
                id = int(input())
                del (dicEstudiantes[id])
                #dicEstudiantes[id]["nombre"] = input()
                #opc = input()
            else:
                print("Por favor, seleccione una opcion valida\n")
            verMenuEstudiantes(dicEstudiantes)
            opc = input()
        else:
            print("Por favor, seleccione una opcion valida\n")

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
            elif opc == "3":
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