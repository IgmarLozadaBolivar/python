print("\n\n")
import os

dicNotas = {
    1: {
    "idEstudiante": "1",
    "idMateria": "2",
    "nota1": 5.0,
    "nota2": 9.0,
    "nota3": "Pendiente",
    "notaF": "Pendiente"
    },
}

dicEstudiantes = {
    1: {
    "nombre": "Juan",
    "apellido": "Garcia",
    "correo": "juan@gmail.com",
    },
    2: {
    "nombre": "Adrian",
    "apellido": "Martinez",
    "correo": "adrian@gmail.com",
    },
    3: {
    "nombre": "Laura",
    "apellido": "Lopez",
    "correo": "laura@gmail.com",
    },
    4: {
    "nombre": "Jessica",
    "apellido": "Muñoz",
    "correo": "jessica@gmail.com",
    }
}

dicMaterias = {
    1: {
    "nombre": "Matemáticas",
    },
    2: {
    "nombre": "Física",
    },
    3: {
    "nombre": "Lengua",
    },
    4: {
    "nombre": "Química",
    }
}

def verMenu():
    os.system("clear" or "cls") 
    print("********** SISTEMA **********\n")
    print('''Seleccione una de las siguientes opciones: 
    1. Notas        2. Estudiantes
    3. Materias     0. Salir''')

#           NOTAS
def verMenuNotas(notas):
    os.system("clear" or "cls")
    print("********* NOTAS *********\n")
    print("CODIGO\t\t\tNOTA 1\t\t\tNOTA 2\t\t\tNOTA 3\t\t\tNOTA FINAL")
    for nota in notas:
        print(nota,"\t\t\t",notas[nota]["nota1"],"\t\t\t",notas[nota]["nota2"],"\t\t\t",notas[nota]["nota3"],"\t\t\t", notas[nota]["notaF"])
    print('''Seleccione una de las siguientes opciones:
    1. Agregar nota                 2. Editar nota
    3. Eliminar nota                0. Salir''')

#           ESTUDIANTES
def verMenuEstudiantes(estudiantes):
    os.system("clear" or "cls") 
    print("********* ESTUDIANTES *********\n")
    print("CODIGO\t\t\tNOMBRE\t\t\tAPELLIDO\t\t\tCORREO")
    for estudiante in estudiantes:
        print(estudiante,"\t\t\t",estudiantes[estudiante][f"nombre"],"\t\t\t",estudiantes[estudiante][f"apellido"],"\t\t\t",estudiantes[estudiante][f"correo"])
    print('''Seleccione una de las siguientes opciones: 
    1. Agregar estudiante       2. Editar estudiante
    3. Eliminar estudiante      0. Salir''')

#           MATERIAS
def verMenuMaterias(materias):
    os.system("clear" or "cls") 
    print("********* MATERIAS *********\n")
    print(f'{"CÓDIGO":<25} {"MATERIA"}')
          #{"\t\t\t"},{"MATERIA"}')
    print(f'{"------":<25} {"-------------"}')
    for materia in materias:
        print(materia,"\t\t\t",materias[materia]["nombre"])
    print('''Seleccione una de las siguientes opciones: 
    1. Crear materia        2. Editar materia
    3. Eliminar materia     0. Salir''')

#           VER NOTAS
def verNotasMateria(nota, materia):
    os.system("clear" or "cls")
    print("********* NOTAS POR MATERIA *********\n")
    print(f'{"CODIGO":<25} {"NOMBRE":^10} {"NOTA 1":^10} {"NOTA 2":^10} {"NOTA 3":^10}')
    print(f'{"------":<25} {"------":^10} {"------":^10} {"------":^10} {"------":^10}')
    for nota in materia:
        print(nota,"\t\t\t",materia[nota]["idEstudiante"],"\t\t\t",materia[nota]["idMateria"],"\t\t\t",materia[nota]["nota1"],"\t\t\t",materia[nota]["nota2"],"\t\t\t",materia[nota]["nota3"])
        print('''Seleccione una de las siguientes opciones: 
        1. Agregar nota     2. Editar nota
        3. Eliminar nota    0. Salir''')
verMenu()
opcMenu = input()
while opcMenu != "0":
    if opcMenu == "1":
        print("********* NOTAS *********\n")
        #print("********* NOTAS DE MATERIAS Y ESTUDIANTES *********\n")
        verMenuNotas(dicNotas)
        notas = input()
        while notas != "0":
            if notas == "1":
                print("********* AGREGAR *********")
                id = list(dicNotas.keys())[len(dicNotas.keys())-1]+1
                print("Por favor ingrese el codigo a agregar: ")
                codigo = input()
                print("Por favor ingrese la nota 1: ")
                nota1 = float(input())
                print("Nota agregada con exito")        
                print("Por favor ingrese la nota 2: ")
                nota2 = float(input())
                print("Nota agregada con exito")
                print("Por favor ingrese la nota 3: ")
                nota3 = float(input())
                print("Nota agrga con exito")
                dicNotas[id] = {"nota1": nota1, "nota2": nota2, "nota3": nota3}
            elif notas == "2":
                print("********* EDITAR *********")
                print("Por favor ingrese el código de la nota: ")
                id = int(input())
                print("¡Codigo ingresado!")
                print("Por favor ingrese la nueva nota: ")
                nota1 = float(input())
                dicNotas[id]["nota1"] = nota1
                print("Nota editada con exito")
                print("Por favor ingrese la nueva nota: ")
                nota2 = float(input())
                dicNotas[id]["nota2"] = nota2
                print("Nota editada con exito")
                print("Por favor ingrese la nueva nota: ")
                nota3 = float(input())
                dicNotas[id]["nota3"] = nota3
                print("Nota editada con exito")
            elif notas == "3":
                print("********* ELIMINAR *********")
                print("Por favor ingrese el código de la nota: ")
                id = int(input())
                del dicNotas[id]
                print("Notas eliminadas con exito")
            elif notas == "4":
                print("********* NOTAS POR MATERIA *********")
                verMenuNotas(dicNotas)
                #print('''Seleccione una de las siguientes opciones:\n 1. Matematicas\n 2. Fisica\n 3. Lengua\n 4. Quimica\n ''')
                #print("Por favor ingrese el codigo de la lista de materias: ")
                id = int(input())
            elif notas == "5":
                print("********* NOTAS POR ESTUDIANTE *********")
                print("Por favor ingrese el codigo del estudiante: ")
                id = int(input())
            verMenuNotas(dicNotas)
            opc = input()
    elif opcMenu == "2":
        print("******** ESTUDIANTES ********\n")
        verMenuEstudiantes(dicEstudiantes)
        estudiantes = input()
        while estudiantes != "0":
            if estudiantes == "1":
                print("********* AGREGAR *********\n")
                id = list(dicEstudiantes.keys())[len(dicEstudiantes.keys())-1]+1
                print("Por favor ingrese el nombre del estudiante: ")
                nombre = input()
                print("Nombre agregado con exito")
                print("Por favor ingrese el apellido del estudiante: ")
                apellido = input()
                print("Apellido agregado con exito")
                print("Por favor ingrese el correo del estudiante: ")
                correo = input()
                print("Correo agregado con exito")
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
            elif estudiantes == "2":
                print("********* EDITAR *********\n")
                print("Por favor ingrese el código del estudiante a editar: ")
                id = int(input())
                print("¡Codigo ingresado!")
                print("Por favor ingrese el nombre del nuevo estudiante: ")
                dicEstudiantes[id]["nombre"] = input()
                print("¡Nombre editado con exito!")
                print("Por favor ingrese el apellido del estudiante: ")
                dicEstudiantes[id]["apellido"] = input()
                print("¡Apellido editado con exito!")
                print("Por favor ingrese el correo del estudiante: ")
                dicEstudiantes[id]["correo"] = input()
                print("¡Correo editado con exito!")
            elif estudiantes == "3":
                print("********* ELIMINAR *********\n")
                print("Por favor ingrese el codigo del estudiante a eliminar: ")
                id = int(input())
                del (dicEstudiantes[id])
                print("¡Estudiante eliminado con exito!")
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
        materias = input()
        while materias != "0":
            if materias == "1":
                print("********* CREAR *********\n")
                id = list(dicMaterias.keys())[len(dicMaterias)-1]+1
                print("Por favor ingrese el nombre de la nueva materia: ")
                nombre = input()
                dicMaterias[id] = {"nombre": nombre}
                print("¡Materia agregada con exito!")
            elif materias == "2":
                print("********* EDITAR *********\n")
                print("Por favor ingrese el código de la materia a editar: ")
                id = int(input())
                print("¡Codigo ingresado!")
                print("Por favor ingrese el nuevo nombre de la materia: ")
                dicMaterias[id]["nombre"] = input()
                print("¡Materia editada con exito!")
            elif materias == "3":
                print("******** ELIMINAR ********\n")
                print("Por favor ingrese el código de la materia a eliminar: ")
                id = int(input())
                del (dicMaterias[id])
                print("¡Materia eliminada con exito!")
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