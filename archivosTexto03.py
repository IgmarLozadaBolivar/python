'''
El archivo cotizaciones.csv contiene las cotizaciones de las empresas de la 
Bolsa de valores de Colombia con las siguientes columnas: 
Nombre (nombre de la empresa) 
Final (precio de la acción al cierre de bolsa) 
Máximo (precio máximo de la acción durante la jornada)
Mínimo (precio mínimo de la acción durante la jornada), Volumen (Volumen al cierre de bolsa) 
Efectivo (capitalización al cierre en miles de pesos).

Construir una función reciba el archivo de cotizaciones 
y devuelva un diccionario con los datos del archivo por columnas.
Construir una función que reciba el diccionario devuelto por la función anterior 
y cree un archivo en formato csv con el valor promedio de cada columna.
'''

import os

def crearArchivo():
    if not os.path.exists('directorio.txt'):
        archivo = open('directorio.txt', 'w')
        archivo.close()
        print('\n¡PROCESO DE CREACION DEL ARCHIVO!')
        print('¡ARCHIVO CREADO EXITOSAMENTE!')

def consultarTelefono(codigo):
    if os.path.exists("directorio.txt"):
        archivo = open("directorio.txt", "r")
        for linea in archivo:
            datos = linea.strip().split(",")
            if datos[0] == codigo:
                print('\n--------------------------')
                print('LISTADO DE CLIENTES XUANET')
                print('--------------------------')
                print('CODIGO','\t\t','CLIENTES','\t\t','NUMERO DE TELEFONO')
                print(codigo,'\t\t\t',nombre,'\t\t\t',datos[1])
                archivo.close()
                return
        archivo.close()
        print("¡NO SE ENCONTRO EL CLIENTE EN EL ARCHIVO!")
    else:
        print("¡EL ARCHIVO NO EXISTE, VERIFICA SU RUTA!")

def añadirCliente(codigo, telefono):
    archivo = open("directorio.txt", "a")
    archivo.write(codigo + "," + nombre + "," + telefono + "\n")
    archivo.close()
    print("¡CLIENTE AÑADIDO EXITOSAMENTE!")

def eliminarCliente(codigo):
    if os.path.exists("directorio.txt"):
        archivo = open("directorio.txt", "r")
        lineas = archivo.readlines()
        archivo.close()
        encontrado = False
        archivo = open("directorio.txt", "w")
        for linea in lineas:
            datos = linea.strip().split(",")
            if datos[0] != codigo:
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
        codigo = int(input("INGRESE EL CODIGO DEL CLIENTE: "))
        consultarTelefono(codigo)
    elif opcion == 2:
        codigo = int(input("INGRESE EL CODIGO DEL NUEVO CLIENTE: "))
        nombre = input('INGRESE EL NOMBRE DEL CLIENTE: ')
        telefono = input("INGRESE EL NUMERO DE TELEFONO DEL CLIENTE: ")
        añadirCliente(codigo, telefono)
    elif opcion == 3:
        nombre = input("INGRESE EL NOMBRE DEL CLIENTE QUE DESEA ELIMINAR: ")
        eliminarCliente(nombre)
    elif opcion == 4:
        print("¡HA SELECCIONADO SALIR DEL PROGRAMA, VUELVE PRONTO!")
        break
    else:
        print("¡OPCION INVALIDA, INGRESE UNA OPCION DISPONIBLE!")