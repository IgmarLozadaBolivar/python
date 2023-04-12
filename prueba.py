import os
import platform

def clear_screen():
    if platform.system() == 'Windows':
        os.system('cls')
    else:
        os.system('clear')

def estudiante(text):
    clear_screen()
    """ funcion para añadir un texto """
    while True:
        nombre = input(text)
        if nombre=="":
            print("Debe ingresar un nombre")
        else:
            return nombre
 
def nota(text):
    clear_screen()
    """ funcion para añadir una nota """
    while True:
        try:
            nota = float(input("{}(0-10): ".format(text)))
            if 0<=nota<=10:
                return nota
            else:
                print("La nota debe ser entre 0 y 10")
        except:
            print("¡ERROR!")
            print("¡Debe ingresar un numero!")


def añadirMateria():
    clear_screen()
    """Funcion para añadir una nueva asignatura"""
    dicMaterias.append(estudiante("Ingrese el nombre de la materia: "))
    # agregamos la nota a cada estudiante
    [dicEstudiantes[key].append(-1) for key in dicEstudiantes.keys()]
    print("\n********* LISTA DE MATERIAS *********")
    print("---------------------------------------")
    print("\n".join([i for i in dicMaterias]))
    print("\nPROCESO")
    print("¡Materia ingresada con exito!\n")
    print("---------------------------------------\n")

def añadirEstudiante():
    clear_screen()
    """Funcion para añadir estudiantes"""
    dicEstudiantes[estudiante("Ingrese el nombre del estudiante: ")]=[-1]*len(dicMaterias)
    print("\n********* LISTA DE ESTUDIANTES *********")
    print("------------------------------------------")
    print("\n".join([i for i in dicEstudiantes]))
    print("\nPROCESO")
    print("¡Datos del estudiante ingresados con exito!\n")
    print("------------------------------------------\n")
 
def seleccionarEstudiante():
    clear_screen()
    """
    Funcion para seleccionar un estudiante
    Devuelve el nombre del estudiante seleccionado o -1
    """
    count=0
    for i in dicEstudiantes:
        count+=1
        print ("{} - {}".format(count, i))
    try:
        estudiante=int(input("Ingrese el codigo del estudiante a agregar notas: "))
        if 0<estudiante<=len(dicEstudiantes):
            return list(dicEstudiantes.keys())[estudiante-1]
    except:
        print("¡ERROR!")
        print("¡Has seleccionado un estudiante que no se encuentra en la lista!")
    return -1
 
def agregarNota():
    clear_screen()
    """Funcion para agregar todas las notas a uno de los estudiantes"""
    if len(dicEstudiantes)== 0 or len(dicMaterias)== 0:
        return
    estudiante = seleccionarEstudiante()
    if estudiante==-1:
        return
    for i in range(len(dicMaterias)):
        notaActual="sin nota" if dicEstudiantes[estudiante][i]==-1 else dicEstudiantes[estudiante][i]
        dicEstudiantes[estudiante][i]=nota("Introduce la nota para '{}' ({}): ".format(dicMaterias[i], notaActual))
 
def listaMaterias():
    clear_screen()
    """listado de las asignaturas"""
    print("********* LISTA DE MATERIAS *********")
    print("-------------------------------------")
    print("\n".join([i for i in dicMaterias]))
    print("-------------------------------------")
 
def listaEstudiantes():
    clear_screen()
    """Listado de los estudiantes con sus asignaturas"""
    print("********* LISTA DE ESTUDIANTES *********")
    print("----------------------------------------")
    for el in dicEstudiantes:
        print(el)
        for i in range(len(dicMaterias)):
            print("\t{} - {}".format(dicMaterias[i], "Sin nota" if dicEstudiantes[el][i] ==-1 else dicEstudiantes[el][i]))
    print("----------------------------------------")
 
def notaMediaMateria():
    clear_screen()
    print("********** Nota media de las materias **********")
    print("------------------------------------------------")
    if len(dicEstudiantes)==0 or len(dicMaterias)==0:
        return
    for i in range(len(dicMaterias)):
        valores=list(filter(lambda x: x!=-1, list(map(lambda x: x[i], dicEstudiantes.values()))))
        print("{} - {}".format(dicMaterias[i], sum(valores)/len(valores)))
    print("------------------------------------------------")
 
def notaMediaEstudiantes():
    clear_screen()
    print("********** Nota media de los estudiantes **********")
    print("---------------------------------------------------")
    for estudiante in dicEstudiantes:
        valores = list(filter(lambda x: x!=-1, dicEstudiantes[estudiante]))
        if len(valores):
            print("{} - {}".format(estudiante, sum(valores)/len(valores)))
    print("---------------------------------------------------\n")
 
def eliminarMateria():
    clear_screen()
    print("********* ELIMINAR MATERIA *********")
    print("------------------------------------")
    if len(dicMaterias) == 0:
        return
    print("Por favor ingrese el codigo de la materia a eliminar: ")
    for i in range(len(dicMaterias)):
        print("\r{} - {}".format(i+1, dicMaterias[i]))
    try:
        eliminarMateria = int(input("Materia a eliminar: "))
        if 0 <eliminarMateria <= len(dicMaterias):
            eliminarMateria -= 1
            # eliminamos la asignatura
            del dicMaterias[eliminarMateria]
            # eliminamos la nota en los estudiantes
            for key in dicEstudiantes.keys():
                del dicEstudiantes[key][eliminarMateria]
    except:
        pass
    print("------------------------------------\n")
 
def eliminarEstudiante():
    clear_screen()
    print("********* ELIMINAR ESTUDIANTE *********")
    print("---------------------------------------")
    if len(dicEstudiantes) == 0 or len(dicMaterias) == 0:
        return
    print("Por favor ingrese el codigo del estudiante que desea eliminar: ")
    estudiante = seleccionarEstudiante()
    if estudiante == -1:
        return
    del dicEstudiantes[estudiante]
    print("---------------------------------------\n")

def verMenu():
    clear_screen()
    print ('''\n********** SISTEMA ESCOLAR DE ESTUDIANTES **********
----------------------------------------------------
1. Añadir materia
2. Añadir estudiante
3. Añadir/editar notas a los estudiantes
4. Lista de los asignaturas
5. Lista de los estudiantes
6. Mostrar la media de las notas por materias
7. Mostrar la media de las notas por estudiante
8. Eliminar una materia
9. Eliminar un estudiante
10. Salir
----------------------------------------------------
''')
    
dicNotas = {

}
dicEstudiantes = {}
dicMaterias = []

verMenu()
while True:
    #verMenu()

    try:
        option = int(input("\nIngrese la accion que desea realizar: "))
    except:
        break

    if option == 1:
        añadirMateria()
    elif option == 2:
        añadirEstudiante()
    elif option == 3:
        agregarNota()
    elif option == 4:
        listaMaterias()
    elif option == 5:
        listaEstudiantes()
    elif option == 6:
        notaMediaMateria()
    elif option == 7:
        notaMediaEstudiantes()
    elif option == 8:
        eliminarMateria()
    elif option == 9:
        eliminarEstudiante()
    elif option == 10:
        break
    else:
        print("¡OPCION INVALIDA!")