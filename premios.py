''' 1.1 Registrar Expert Trainer del grupo basico
    1.4 Lista de Campers
    1.7 Reportar Campers de mayor y menor edad
'''
import os
import platform

dicCampers = {
        0: {
        "nombre": "Igmar",
        "apellido": "Lozada",
        "edad": "18",
        "correo": "losadabolivar@gmail.com"
    }
}
dicTrainers = {
    0: {
        "nombre": "Igmar",
        "apellido": "Lozada",
        "edad": "18",
        "correo": "losadabolivar@gmail.com"
    }
}

def clear_screen():
    if platform.system() == 'Windows':
        os.system('cls')
    else:
        os.system('clear')

def verMenu():
    clear_screen() 
    print('------------------------------------------------------------')
    print("          MANTENIMIENTO Y PREMIOS CAMPERS CAMPUS            ")
    print('------------------------------------------------------------\n')
    print('''SELECCIONE UNA DE LAS SIGUIENTES OPCIONES: 
    1. CREAR GRUPO BASICO CON CAMPERS Y SUS DATOS PERSONALES
    2. REGISTRAR EXPERT TRAINER DEL GRUPO BASICO       
    3. LISTA DE CAMPERS
    4. REPORTAR CAMPERS DE MAYOR Y MENOR DE EDAD     
    0. SALIR''')

def datosCampers(campers):
    clear_screen()
    print("------------------------------------------")
    print('           DATOS DE LOS CAMPERS           ')
    print("------------------------------------------\n")
    print("CODIGO\t\tNOMBRE\t\tAPELLIDO\t\tEDAD\t\tCORREO")
    for camper in campers:
        print(camper,"\t\t",campers[camper]["nombre"],"\t\t",campers[camper]["apellido"],"\t\t",campers[camper]["edad"],"\t\t",campers[camper]["correo"])
    print('''\nSELECCIONE UNA DE LAS SIGUIENTES OPCIONES: 
    1. AGREGAR DATOS DEL CAMPER
    2. EDITAR DATOS DEL CAMPER
    3. ELIMINAR DATOS DEL CAMPER
    ''')

def datosTrainer(trainers):
    clear_screen()
    print("-------------------------------------------")
    print('           DATOS DE LOS TRAINERS           ')
    print("-------------------------------------------\n")
    print("CODIGO\t\tNOMBRE\t\tAPELLIDO\t\tEDAD\t\tCORREO")
    for trainer in trainers:
        print(trainer,"\t\t",trainers[trainer]["nombre"],"\t\t",trainers[trainer]["apellido"],"\t\t",trainers[trainer]["edad"],"\t\t",trainers[trainer]["correo"])
    print('''\nSELECCIONE UNA DE LAS SIGUIENTES OPCIONES: 
    1. AGREGAR DATOS DEL TRAINER
    2. EDITAR DATOS DEL TRAINER
    3. ELIMINAR DATOS DEL TRAINER
    ''')

def reportarEdadCampers(edades):
    clear_screen()
    print("------------------------------------")
    print("          LISTA DE CAMPERS          ")
    print("------------------------------------")
    for edad in edades:
        print(edad,"\t\t",edades[edad]["nombre"],"\t\t",edades[edad]["apellido"],"\t\t",edades[edad]["edad"])
    print('''\nSELECCIONE UNA DE LAS SIGUIENTES OPCIONES: 
    1. MOSTRAR LISTA DE CAMPERS MAYORES DE EDAD
    2. MOSTRAR LISTA DE CAMPERS MENORES DE EDAD
    ''')

verMenu()
menu = int(input())
while menu != 0:
    if menu == 1:
        print('-----------------------------------------')
        print('             REGISTRO DE TRAINER             ')
        print('-----------------------------------------')
        datosCampers(dicCampers)
        subMenuCampers = int(input())
        while subMenuCampers != 0:
            if subMenuCampers == 1:
                print('---------------------------------')
                print('             AGREGAR             ')
                print('---------------------------------\n')
                id = list(dicCampers.keys())[len(dicCampers.keys())-1]+1
                print('Por favor ingrese el nombre del trainer: ')
                nombre = input()
                print('¡Nombre agregado con exito!')
                print('Por favor ingrese el apellido del trainer: ')
                apellido = input()
                print('¡Apellido agregado con exito!')
                print('Por favor ingrese la edad del trainer: ')
                edad = int(input())
                print('¡Edad ingresa con exito!')
                print('Por favor ingrese el correo del trainer: ')
                correo = input()
                print('¡Correo agregado con exito!')
                dicCampers[id] = {"nombre": nombre, "apellido": apellido, "edad": edad, "correo": correo}
            elif subMenuCampers == "2":
                print("             EDITAR             \n")
                print("Por favor ingrese el código del trainer a editar: ")
                id = int(input())
                print("¡Codigo ingresado!")
                print("Por favor ingrese el nombre del nuevo trainer: ")
                dicCampers[id]["nombre"] = input()
                print("¡Nombre editado con exito!")
                print("Por favor ingrese el apellido del trainer: ")
                dicCampers[id]["apellido"] = input()
                print("¡Apellido editado con exito!")
                print("Por favor ingrese la edad del trainer: ")
                dicCampers[id]["edad"] = int(input())
                print("¡Edad editada con exito!")
                print("Por favor ingrese el correo del trainer: ")
                dicCampers[id]["correo"] = input()
                print("¡Correo editado con exito!")
            elif subMenuCampers == "3":
                print("             ELIMINAR             \n")
                print("Por favor ingrese el codigo del trainer a eliminar: ")
                id = int(input())
                del (dicCampers[id])
                print("¡Estudiante eliminado con exito!")
            else:
                print("Por favor, seleccione una opcion valida\n")
            datosCampers(dicCampers)
    elif menu == 2:
        print('----------------------------------------------')
        print('             REGISTRO DE TRAINERs             ')
        print('----------------------------------------------')
        datosTrainer(dicTrainers)
        subMenuTrainers = int(input())
        while subMenuTrainers != 0:
            if subMenuTrainers == 1:
                print('---------------------------------------')
                print('             AGREGAR             ')
                print('---------------------------------------\n')
                id = list(dicTrainers.keys())[len(dicTrainers.keys())-1]+1
                print('Por favor ingrese el nombre del trainer: ')
                nombre = input()
                #icTrainers.append(nombre)
                print('¡Nombre agregado con exito!')
                print('Por favor ingrese el apellido del trainer: ')
                apellido = input()
                #apellido.append(dicTrainers)
                print('¡Apellido agregado con exito!')
                print('Por favor ingrese la edad del trainer: ')
                edad = int(input())
                #edad.append(dicTrainers)
                print('¡Edad ingresa con exito!')
                print('Por favor ingrese el correo del trainer: ')
                correo = input()
                #correo.append(dicTrainers)
                print('¡Correo agregado con exito!')
                dicTrainers[id] = {"nombre": nombre, "apellido": apellido, "edad": edad, "correo": correo}
            elif subMenuTrainers == "2":
                print("             EDITAR             \n")
                print("Por favor ingrese el código del trainer a editar: ")
                id = int(input())
                print("¡Codigo ingresado!")
                print("Por favor ingrese el nombre del nuevo trainer: ")
                dicTrainers[id]["nombre"] = input()
                print("¡Nombre editado con exito!")
                print("Por favor ingrese el apellido del trainer: ")
                dicTrainers[id]["apellido"] = input()
                print("¡Apellido editado con exito!")
                print("Por favor ingrese la edad del trainer: ")
                dicTrainers[id]["edad"] = int(input())
                print("¡Edad editada con exito!")
                print("Por favor ingrese el correo del trainer: ")
                dicTrainers[id]["correo"] = input()
                print("¡Correo editado con exito!")
            elif subMenuTrainers == "3":
                print("             ELIMINAR             \n")
                print("Por favor ingrese el codigo del trainer a eliminar: ")
                id = int(input())
                del (dicTrainers[id])
                print("¡Estudiante eliminado con exito!")
            else:
                print("Por favor, seleccione una opcion valida\n")
            datosTrainer(dicTrainers)
    elif menu == 3:
        print('             LISTA DE CAMPERS             ')
        print(dicCampers)
