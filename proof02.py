###IGMAR DE JESUS LOZADA BOLIVAR###
###GROUP W04###
'''Crea una aplicación que contenga todas las siguientes funcionalidades a las cuales se debe 
acceder por medio de un menú:
'''

'''
1.Crea una aplicación que nos calcule el área de un círculo, cuadrado o triangulo.
Pediremos qué figura queremos calcular, su área y según lo introducido pedirá los valores
necesarios para calcular el área. Crea una función por cada figura para calcular cada área,
este devolverá un número real. Muestra el resultado por pantalla
    Circulo: (radio^2)*PI
    Triangulo: (base * altura) / 2
    Cuadrado: lado * lado
'''
    
import math

def calculateAreaCircle():
    radio = float(input("Enter the radius of the circle: "))
    area = math.pi * radio ** 2
    return area
def calculateTriangleArea():
    base = float(input("Enter the base of the triangle: "))
    height= float(input("Enter the height of the triangle: "))
    area = (base * height) / 2
    return area
def calculateSquareArea():
    side = float(input("Enter from the side of the square: "))
    area = side ** 2
    return area

figure = input("¿What shape do you want to calculate the area of?:\n (Circle)\n (Triangle)\n (Square)\n")
if figure == 'Circle':
    area = calculateAreaCircle()
elif figure == 'Triangle':
    area = calculateTriangleArea()
elif figure == 'Square':
    area = calculateSquareArea()
else: 
    print("Select an option")
    area = 0

print(f"The area of {figure} is {area}")

'''
2.Crea una aplicación que nos pida un número por teclado y con una función se lo pasamos
por parámetro para que nos indique si es o no un número primo, debe devolver true si
es primo sino false.
Un número primo es aquel solo puede dividirse entre 1 y si mismo.
Por ejemplo: 25 no es primo, ya que 25 es divisible entre 5, sin embargo, 17 si es primo.
'''

def isPrime(number):
        if number < 2:
            return False
        for i in range(2, int(number ** 0.5) + 1):
            if number % 1 == 0:
                return False
        return True

number = int(input("Enter a number: "))
if isPrime(number):
    print(f"{number} is a prime number")
else:
    print(f"{number} is not a prime number")

'''
3.Crea una aplicación que nos calcule el factorial de un número pedido por teclado, lo
realizara mediante una función al que le pasamos el número como parámetro. Para calcular el
multiplica los números anteriores hasta llegar a uno. Por ejemplo, si introducimos un 5,
realizara esta operación 5*4*3*2*1=120.
'''

'''
4.Crea una aplicación que nos convierta una cantidad de pesos introducida por teclado a otra
moneda, estas pueden ser a dolares, yenes o libras. La función tendrá como parámetros, la
cantidad de pesos y la moneda a pasar que será un texto
'''


def currencyConverter(pesos, currency):
   if currency == 'Dollars':
       exchangeRate = 0.00028
       conversion = pesos * exchangeRate
       return conversion
   elif currency ==  'Yen':
       exchangeRate = 0.030
       conversion = pesos * exchangeRate
   elif currency == 'Pounds':
       exchangeRate = 0.00020
       conversion = pesos * exchangeRate
   else:
       return "Invalid currency"

quantity = float(input("Enter the amount of pesos you want to convert: "))
currencyDestiny = input("Enter the destination currency (Dollars, Yen to Pounds): ")
result = currencyConverter(quantity, currencyDestiny)
if isinstance(result, str):
    print(result)
else:
    print(f"{quantity} pesos equivale a {result} {currencyDestiny}")

'''
5.Crea una aplicación que replique la ecuasión cuadrática, solicitando los valores para
a, b y c, y exponiendo los 2 resultados que esta genera. Tener en cuenta que se debe validar 
si los valores dados por el usuario generan un resultado imaginario, de ser así debe informarse
'''