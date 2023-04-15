'''
Poblar una lista con 10 valores entregados por el usuario

1. Mostrar la lista recien creada
2. Mostrar los elementos ubicados en las posiciones pares de la lista a partir del indice 0
3. Mostrar los elementos ubicados en las posiciones pares de la lista a partir del indice 1
4. Mostrar los elementos ubicados en las primera y ultima posicion de la lista
5. Invertir y mostrar la lista invertida
'''

list = []


for i in range(10):
    value = int(input('Ingrese un numero: '))
    list.append(value)

print('\n')
print('Mostrar la lista recien creada')
print(list)

print('\n')
print('Mostrar los elementos ubicados en las posiciones pares de la lista a partir del indice 0')
print(list[1:10:2])

print('\n')
print('Mostrar los elementos ubicados en las posiciones impares de la lista a partir del indice 1')
print(list[0:10:2])

print('\n')
print('Mostrar los elementos ubicados en las primera y ultima posicion de la lista')
print(list([0][10]))

print('\n')
print('Invertir y mostrar la lista invertida')
print(list[::-1])