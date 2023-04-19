
pacientes = []

def crearPaciente():
    print('----------------------------------------')
    print('SISTEMA DE INGRESO DE DATOS DEL PACIENTE')
    print('----------------------------------------\n')
    codigo = input('Ingresa el código del paciente: ')
    nombre = input('Ingresa el nombre del paciente: ')
    fechaNac = input('Ingresa la fecha de nacimiento del paciente (DD/MM/AAAA): ')
    peso = float(input('Ingresa el peso del paciente (KG): '))
    sexo = input('Ingresa el sexo del paciente (M/F): ')
    pacientes.append({'codigo': codigo, 'nombre': nombre, 'fechaNac': fechaNac, 'peso': peso, 'sexo': sexo})
    print('¡PACIENTE AGREGADO EXITOSAMENTE!')

def editarPaciente():
    print('----------------------------------------------')
    print('SISTEMA DE ACTUALIZACION DE DATOS DEL PACIENTE')
    print('----------------------------------------------\n')
    codigo = int(input('Ingresa el código del paciente que deseas editar: '))
    for paciente in pacientes:
        if paciente['codigo'] == codigo:
            paciente['nombre'] = input('Ingresa el nuevo nombre del paciente: ')
            paciente['fechaNac'] = input('Ingresa la nueva fecha de nacimiento del paciente (DD/MM/AAAA): ')
            paciente['peso'] = float(input('Ingresa el nuevo peso del paciente (KG): '))
            paciente['sexo'] = input('Ingresa el nuevo sexo del paciente (M/F): ')
            print('¡PACIENTE ACTUALIZADO EXITOSAMENTE!')
            return
    print('¡NO SE HA ENCONTRADO NINGUN PACIENTE CON EL CODIGO INGRESADO, VERIFIQUE EL CODIGO!')

def borrarPaciente():
    print('--------------------------------------------')
    print('SISTEMA DE ELIMINACION DE DATOS DEL PACIENTE')
    print('--------------------------------------------\n')
    codigo = input('INGRESA EL CODIGO DEL ESTUDIANTE A BORRAR: ')
    for paciente in pacientes:
        if paciente['codigo'] == codigo:
            pacientes.remove(paciente)
            print('PROCESO DEL SISTEMA')
            print('-------------------')
            print('¡EL PACIENTE HA SIDO BORRADO DE MANERA SASTIFACTORIA!')
            return
    print('¡NO SE HA ENCONTRADO NINGUN PACIENTE CON EL CODIGO INGRESADO, VERIFIQUE EL CODIGO!')

def listarPacientes():
    print('------------------')
    print('LISTA DE PACIENTES')
    print('------------------\n')
    print('LISTA DE PACIENTES QUE EXISTEN:')
    for paciente in pacientes:
        print('Codigo:', paciente['codigo'])
        print('Nombre:', paciente['nombre'])
        print('Fecha de nacimiento:', paciente['fechaNac'])
        print('Peso:', paciente['peso'],'KG')
        print('Sexo:', paciente['sexo'])
        print('\n')

def verMenu():
    flag = True
    while flag:
        print('\n--------------------')
        print('''MENU DE PACIENTES
--------------------\n
SELECCIONE UNA DE LAS SIGUIENTES OPCIONES EN PANTALLA:
1. CREAR NUEVO PACIENTE
2. EDITAR PACIENTE EXISTENTE
3. BORRAR PACIENTE
4. LISTA DE PACIENTES DISPONIBLES
5. SALIR\n''')
        opc = int(input('SELECCION DE OPCION: '))
        if opc == 1:
            crearPaciente()
        elif opc == 2:
            editarPaciente()
        elif opc == 3:
            borrarPaciente()
        elif opc == 4:
            listarPacientes()
        elif opc == 5:
            print("¡HAS SELECCIONADO FINALIZAR EL PROGRAMA!")
            break
        else:
            print("¡OPCION INVALIDA, ESCOGE UNA OPCION DISPONIBLE!")

verMenu()

