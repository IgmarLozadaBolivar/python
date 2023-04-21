empresa = {
    'personas' : [
        {
            'ID': 1,
            'Nombre': 'Pedro',
            'Edad': '20',
            'numdoc': 123456789
        },
        {
            'ID': 2,
            'Nombre': 'Ofelia',
            'Edad': '30',
            'numdoc': 123456788
        },
        {
            'ID': 3,
            'Nombre': 'Ruth',
            'Edad': '17',
            'numdoc': 123456787
        }
    ]
}

import json

def crearJson():
    with open('empresa.json', 'w') as archivo:
        json.dump(empresa, archivo)

def cargarJson():
    with open('empresa.json', 'r') as archivo:
        empresa = json.load(archivo)

def consultarPersonas():
    for persona in empresa['personas']:
        print(f"ID: {persona['ID']} - Nombre: {persona['Nombre']} - Edad: {persona['Edad']} - Num. Doc.: {persona['numdoc']}")

def anadirPersonas(ID, nombre, edad, numdoc):
    persona_nueva = {
            'ID': ID,
            'Nombre': nombre,
            'Edad': edad,
            'numdoc': numdoc
        }
    empresa['personas'].append(persona_nueva)

def eliminarPersonas(ID):
    for i in range(len(empresa['personas'])):
        if empresa['personas'][i]['ID'] == ID:
            del empresa['personas'][i]
            break

# Ejemplo 
anadirPersonas(4, 'Juan', '25', 123456786)
print("Listado de personas:")
consultarPersonas()
eliminarPersonas(2)
print("Listado de personas actualizado:")
consultarPersonas()

with open('empresa.json', 'w') as archivo:
    json.dump(empresa, archivo)


validador = True
while validador:
    crearJson()
    print('''\nLISTADO DE EMPLEADOS
1. CONSULTAR NUMERO DE TELEFONO
2. AÑADIR CLIENTE A LA BASE DE DATOS
3. ELIMINAR CLIENTE DE LA BASE DE DATOS
4. SALIR DEL PROGRAMA''')
    opcion = int(input("SELECCIONE UNA DE LAS SIGUIENTES OPCIONES DISPONIBLES: "))
    if opcion == 1:
        nombre = input("INGRESE EL NOMBRE DEL EMPLEADO: ")
        consultarPersonas()
    elif opcion == 2:
        nombre = input("INGRESE EL NOMBRE DEL NUEVO CLIENTE: ")
        cedula = input("INGRESE EL NUMERO DE LA CEDULA DEL EMPLEADO: ")
        edad = input("INGRESE LA EDAD DEL EMPLEADO: ")
        anadirPersonas(nombre, cedula, edad)
    elif opcion == 3:
        nombre = input("INGRESE EL NOMBRE DEL EMPLEADO QUE DESEA ELIMINAR: ")
        eliminarPersonas(nombre)
    elif opcion == 4:
        print("¡HA SELECCIONADO SALIR DEL PROGRAMA, VUELVE PRONTO!")
        break
    else:
        print("¡OPCION INVALIDA, INGRESE UNA OPCION DISPONIBLE!")