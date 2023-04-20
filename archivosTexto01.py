'''
Elabore un Programa Python que lea la ruta y nombre de un archivo y muestre por pantalla la línea M del archivo.
La línea a mostrar también debe ser un dato ingresado por el usuario del programa.
Si el archivo no existe debe mostrar un mensaje por pantalla informando de ello.
'''

import sys

print('''\n-----------------------
LECTOR DE RUTAS ARCHIVOS
------------------------''')

archivo = input('\nIngrese la ruta y el nombre del archivo para leer: ')

linea = int(input('Ingrese el número de línea a mostrar: '))

try:
    with open(archivo, "r") as archivoLeer:
        lineas = archivoLeer.readlines()

        if linea > len(lineas):
            print('''¡EL ARCHIVO NO CONTIENE LA LINEA INGRESADA,
            VERFIQUE EL NUMERO DE LA LINEA QUE DESEA LEER!''')
            sys.exit()

        print(f"La linea {linea} del archivo '{archivo}':\n")
        print(lineas[linea - 1])

except FileNotFoundError:
    print('''\n¡ARCHIVO NO EXISTENTE, VERIFIQUE LA DIRECCION DEL ARCHIVO A LEER!\n''')
