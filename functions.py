#Funcion basica
def saludar():
    print("Hola a todos")

#Funcion con parametros
def verNombreCompleto(nombre, apellido):
    print(nombre, apellido)

def obtenerNombreCompleto(nombre, apellido):
    return nombre + " " + apellido

print("\nFUNCION SIMPLE")
saludar()
print("\nFUNCION PARAMETROS")
verNombreCompleto("Maria Alejandra", "Nuñez Diaz")
print("\nFUNCION SIMPLE Y RETORNO")
nombreCompleto = obtenerNombreCompleto("Maria Luisa", "Nuñez Franco")
print(nombreCompleto)

'''
Para un concierto hay 3 tipos de boletas, desarrollar un programa
que calcule el total de ventas para cada boleta
(cuantas boletas se vendieron de cada tipo y
cuanto se recaudo por boleta).
En cada venta se pueden vender mas de una boleta,
pero solo de un mismo tipo.

    Ubicacion   Valor   US$
1   General     50 
2   Vip         75
3   Platinum    100
'''