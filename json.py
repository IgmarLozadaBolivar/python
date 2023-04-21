import json

#Estructura de datos (Lista)
#lista = [10, 20, 30, 40, 60]
#diccionario = {'1':'Roy H. Llamas','2':'Igmar L. Bolivar','3':'David V. Duarte','4':'Andres E. Pajaro','5':'Daniel A. Rodriguez'}

#Fase de apertura y creacion
with open('diccionario.json', 'r') as archivo:
    #json.dump(diccionario,archivo)
    diccionario = json.load(archivo)


#Fase de cierroe
archivo.close()

print('\nDiccionario: ', diccionario)
print(diccionario['1'])
print(diccionario['2'])
print(diccionario['3'])
print(diccionario['4'])
print(diccionario['5'])