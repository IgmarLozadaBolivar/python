
my_list = []
letter = input('\nIngrese una palabra: ')

for i in letter:
    my_list.append(i)

print('\n')
print('Existe esta cantidad de (A): ',my_list.count('a'))
print('Existe esta cantidad de (O): ',my_list.count('e'))
print('Existe esta cantidad de (I): ',my_list.count('i'))
print('Existe esta cantidad de (O): ',my_list.count('o'))
print('Existe esta cantidad de (U): ',my_list.count('u'))
print('\nPalabra ingresada: ',letter,'\n')


dicCategorias={1:25000,2:30000,3:40000,4:45000,5:60000}
totalHonorarios = 0

print('\n------------------------------')
print('CENTRO DE ENTRENAMIENTO CAMPUS')
print('------------------------------\n')

print('\n--------------------')
print('CANTIDAD DE TRAINERS')
print('--------------------')
nTrainers = int(input('\nIngrese el numero de Trainers: '))

for i in range(nTrainers):
    print('\n----------------------------')
    print('INGRESO DE DATOS DEL TRAINER')
    print('----------------------------')
    print('\nNOMBRE DEL TRAINER')
    print('------------------')
    nombre = input('Ingrese el nombre del Trainer: ')
    print('\nCEDULA DEL TRAINER')
    print('------------------')
    cedula = int(input('Ingrese la C.C del Trainer: '))
    print('\nCATEGORIA DEL TRAINER')
    print('---------------------')
    categoria = int(input('Ingrese la categoria del Trainer (1-5): '))
    print('HORAS LABORADAS DEL TRAINER')
    print('---------------------------')
    horasLaboradas = float(input('Ingrese el numero de hrs laboradas al mes: '))

valorHorasTrabajadas = dicCategorias[categoria]
honorarios = horasLaboradas * valorHorasTrabajadas

print('NOMBRE\t\tC.C\t\tCATEGORIA')
print(nombre,'\t\t',cedula,'\t\t',categoria)
print('\n-------------------')
print('VALOR DEL HONORARIO')
print('-------------------')
print(honorarios,'\n')

totalHonorarios += honorarios

print('\n-------------------------------')
print('TOTAL DEL HONORARIO DEL TRAINER')
print('-------------------------------')
print(totalHonorarios)