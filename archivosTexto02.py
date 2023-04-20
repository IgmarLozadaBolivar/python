'''
Escribir un programa para gestionar un listado telefónico con los nombres 
y los teléfonos de los clientes de una empresa.
El programa debe incorporar funciones para: 
1. crear el archivo si este no existe 
2. para consultar el teléfono de un cliente 
3. añadir el teléfono de un nuevo cliente 
4. eliminar el teléfono de un cliente. 
El listado debe estar guardado en el archivo de texto Directorio.txt donde el nombre del cliente 
y su teléfono deben aparecer separados por comas y cada cliente en una línea distinta.
'''


import os

def crearArchivo():
    if not os.path.exists('directorio.txt'):
        archivo = open('directorio.txt', 'w')
        archivo.close()
        print('\n¡PROCESO DE CREACION DEL ARCHIVO!')
        print('¡ARCHIVO CREADO EXITOSAMENTE!')

def consultarTelefono(nombre):
    if os.path.exists("directorio.txt"):
        archivo = open("directorio.txt", "r")
        for linea in archivo:
            datos = linea.strip().split(",")
            if datos[0] == nombre:
                print('\n--------------------------')
                print('LISTADO DE CLIENTES XUANET')
                print('--------------------------')
                print('CLIENTES','\t\t','NUMERO DE TELEFONO')
                print(nombre,'\t\t\t',datos[1])
                archivo.close()
                return
        archivo.close()
        print("¡NO SE ENCONTRO EL CLIENTE EN EL ARCHIVO!")
    else:
        print("¡EL ARCHIVO NO EXISTE, VERIFICA SU RUTA!")

def añadirCliente(nombre, telefono):
    archivo = open("directorio.txt", "a")
    archivo.write(nombre +  ","  + telefono + "\n")
    archivo.close()
    print("¡CLIENTE AÑADIDO EXITOSAMENTE!")

def eliminarCliente(nombre):
    if os.path.exists("directorio.txt"):
        archivo = open("directorio.txt", "r")
        lineas = archivo.readlines()
        archivo.close()
        encontrado = False
        archivo = open("directorio.txt", "w")
        for linea in lineas:
            datos = linea.strip().split(",")
            if datos[0] != nombre:
                archivo.write(linea)
            else:
                encontrado = True
        archivo.close()
        if encontrado:
            print("¡CLIENTE ELIMINADO EXITOSAMENTE!")
        else:
            print("¡NO SE HA ENCONTRADO NINGUN CLIENTE EN EL ARCHIVO!")
    else:
        print("¡EL ARCHIVO NO EXISTE, VERIFICA SU RUTA!")

while True:
    crearArchivo()
    print('''\nSISTEMA DE LISTADO TELEFONICO XUANET
1. CONSULTAR NUMERO DE TELEFONO
2. AÑADIR CLIENTE A LA BASE DE DATOS
3. ELIMINAR CLIENTE DE LA BASE DE DATOS
4. SALIR DEL PROGRAMA''')
    opcion = int(input("SELECCIONE UNA DE LAS SIGUIENTES OPCIONES DISPONIBLES: "))
    if opcion == 1:
        nombre = input("INGRESE EL NOMBRE DEL CLIENTE: ")
        consultarTelefono(nombre)
    elif opcion == 2:
        nombre = input("INGRESE EL NOMBRE DEL NUEVO CLIENTE: ")
        telefono = input("INGRESE EL NUMERO DE TELEFONO DEL CLIENTE: ")
        añadirCliente(nombre, telefono)
    elif opcion == 3:
        nombre = input("INGRESE EL NOMBRE DEL CLIENTE QUE DESEA ELIMINAR: ")
        eliminarCliente(nombre)
    elif opcion == 4:
        print("¡HA SELECCIONADO SALIR DEL PROGRAMA, VUELVE PRONTO!")
        break
    else:
        print("¡OPCION INVALIDA, INGRESE UNA OPCION DISPONIBLE!")