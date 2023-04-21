import json

empresa = {
    'Personas' : [
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

def crearJson():
    with open('empresa.json', 'w') as archivo:
        json.dump(empresa, archivo, indent=4)

def cargarJson():
    with open('empresa.json', 'r') as archivo:
        empresa = json.load(archivo,indent=4)

def consultarPersonas():
    for persona in empresa['Personas']:
        print(f"ID: {persona['ID']} - Nombre: {persona['Nombre']} - Edad: {persona['Edad']} - Num. Doc.: {persona['numdoc']}")

def anadirPersonas(nombre, numdoc, edad):
    persona_nueva = {
            'ID': len(empresa['Personas']) + 1,
            'Nombre': nombre,
            'Edad': edad,
            'numdoc': numdoc
        }
    empresa['Personas'].append(persona_nueva)

def eliminarPersonas(nombre):
    for i in range(len(empresa['Personas'])):
        if empresa['Personas'][i]['Nombre'] == nombre:
            del empresa['Personas'][i]
            break

validador = True
while validador:
    crearJson()
    print('''\nLISTADO DE EMPLEADOS DE LA EMPRESA
1. CONSULTAR LISTA DE EMPLEADOS
2. AÑADIR EMPLEADO A LA BASE DE DATOS DE LA EMPRESA
3. ELIMINAR EMPLEADO DE LA BASE DE DATOS DE LA EMPRESA
4. SALIR DEL PROGRAMA''')
    opcion = int(input("SELECCIONE UNA DE LAS SIGUIENTES OPCIONES DISPONIBLES: "))
    if opcion == 1:
        consultarPersonas()
    elif opcion == 2:
        nombre = input("INGRESE EL NOMBRE DEL NUEVO EMPLEADO: ")
        cedula = input("INGRESE EL NUMERO DE CEDULA DEL EMPLEADO: ")
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
