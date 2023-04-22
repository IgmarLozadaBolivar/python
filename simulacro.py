'''
Elabore un programa Python para gestionar el CRUD del archivo de datos 
Biblioteca.json con las siguientes funcionalidades:

Mostrar en pantalla todos los libros
Crear Nuevo libro con la posibilidad de múltiples autores por Libro
Mostrar los datos de un libro consultado por título
Actualizar los datos de un libro consultado por título
Eliminar un Libro de la biblioteca
'''

import json
import os

biblioteca = 'Biblioteca.json'

def readJSON():
    if not os.path.exists('Biblioteca.json'):
        with open(biblioteca, 'r') as archivo:
            datos = json.load(archivo)
        return datos

def escribirJSON(datos):
    if not os.path.exists('Biblioteca.json'):
        with open(biblioteca, 'w') as archivo:
            json.dump(datos, archivo, indent = 4)

def verLibros():
    datos = readJSON()
    for libro in datos['bookstore']['book']:
        print(f'Título: {libro["title"]["__text"]}')
        print(f'Autor(es): {", ".join(libro["author"])}')
        print(f'Año: {libro["year"]}')
        print(f'Precio: {libro["price"]}')
        print(f'Categoría: {libro["_category"]}')
        print()

def crearNuevoLibro():
    datos = readJSON()
    nuevoLibro = {
        "title": {
            "_lang": "en",
            "__text": input('Ingresa el titulo del libro: ')
        },
        "author": [author for author in input('Ingresa el nombre del autor o autores separado por comas: ').split(',')],
        "year": input('Ingresa el año de publicacion del libro: '),
        "price": input('Ingresa el precio del libro: '),
        "_category": input('Ingresa la categoría del libro: ')
    }
    datos['bookstore']['book'].append(nuevoLibro)
    escribirJSON(datos)
    print('¡EL NUEVO LIBRO HA SIDO ALMACENADO EN LA BIBLIOTECA CON EXITO!')

def verLibroTitulo(Titulo):
    datos = readJSON()
    for libro in datos['bookstore']['book']:
        if libro['title']['__text'] == Titulo:
            print(f'Título: {libro["title"]["__text"]}')
            print(f'Autor(es): {", ".join(libro["author"])}')
            print(f'Año: {libro["year"]}')
            print(f'Precio: {libro["price"]}')
            print(f'Categoría: {libro["_category"]}')
            return
    print('¡NO SE HA ENCONTRADO EN LA BIBLIOTECA, UN LIBRO CON ESTE TITULO!')

def actualizarLibro(Titulo):
    datos = readJSON()
    for libro in datos['bookstore']['book']:
        if libro['title']['__text'] == Titulo:
            libro['title']['__text'] = input('Ingresa el nuevo título del libro (pulsa enter para mantener el título original): ') \
                or libro['title']['__text']
            libro['author'] = [author for author in input('Ingresa el nombre de los autor(es) separados por comas: ').split(',')]
            libro['year'] = input('Ingresa el nuevo año de publicacion (pulsa enter para mantener el año original): ') \
                or libro['year']
            libro['price'] = input('Ingresa el nuevo precio del libro (pulsa enter para mantener el precio original): ') \
                or libro['price']
            libro['_category'] = input('Ingresa la nueva categoría del libro (pulsa enter para mantener la categoría original): ') \
                or libro['_category']
            escribirJSON(datos)
            print('¡LOS DATOS DEL LIBRO SE HAN ACTUALIZADO CON EXITO!')
            return
    print('¡NO SE HA ENCONTRADO NI UN LIBRO CON ESE TITULO!')

def eliminarLibro(Titulo):
    datos = readJSON()
    for libro in datos['bookstore']['book']:
        if libro['title']['__text'] == Titulo:
            datos['bookstore']['book'].remove(libro)
            escribirJSON(datos)
            print('¡EL LIBRO HA SIDO ELIMINADO DE LA BIBLIOTECA CON EXITO!')
            return
    print('¡NO SE HA ENCONTRADO EN LA BIBLIOTECA, UN LIBRO CON ESTE TITULO!')

flag = True
while flag:
    #readJSON()
    print('''\nBIBLIOTECA DE LIBROS
1. CONSULTAR LIBROS DE LA BIBLIOTECA
2. CREAR NUEVO LIBRO EN LA BIBLIOTECA
3. CONSULTAR LIBRO DE LA BIBLIOTECA
4. ACTUALIZAR LIBRO EXISTENTE DE LA BIBLIOTECA
5. ELIMINAR LIBRO EXISTENTE DE LA BIBLIOTECA
6. SALIR DEL PROGRAMA''')
    opcion = int(input("SELECCIONE UNA DE LAS SIGUIENTES OPCIONES: "))

    if opcion == 1:
        verLibros()
    elif opcion == 2:
        crearNuevoLibro()
    elif opcion == 3:
        Titulo = input('INGRESE EL TITULO DEL LIBRO QUE DESEA VER: ')
        verLibroTitulo(Titulo)
    elif opcion == 4:
        titulo = input('INGRESE EL TITULO DEL LIBRO A ACTUALIZAR DE LA BIBLIOTECA: ')
        actualizarLibro(Titulo)
    elif opcion == 5:
        titulo = input("INGRESE EL TITULO DEL LIBRO QUE DESEA ELIMINAR DE LA BIBLIOTECA: ")
        eliminarLibro(Titulo)
    elif opcion == 0:
        break
    else:
        print("¡OPCION INVALIDA, INGRESE UNA OPCION DISPONIBLE!")
        