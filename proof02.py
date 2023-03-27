###IGMAR DE JESUS LOZADA BOLIVAR###
###GROUP W04###
'''Crea una aplicación que contenga todas las siguientes funcionalidades a las cuales se debe acceder por medio de un menú:
'''
#Area figures
import math

def calculateAreaCircle(radio):
        area = (radio**2)*3.1416
        return area
def calculateTriangleArea(base, height):
        area = (base * height)/2
        return area
def calculateSquareArea(side):
        area = (side * side)
        return area

#Prime number
def isPrime(num):
    for n in range(2, num):
        if num % n == 0:
            return False
        return True

#Factorial number
def factorialNumber (num):
        if num == 0 or num == 1:
          resultado = 1
        elif num > 1:
             resultado = num*factorialNumber(num-1)
        return resultado

#Currency exchange
def currencyConverter(quantity, currency):
    usd_rate = 3000
    jpy_rate = 28.5
    gbp_rate = 4100

    if currency == "dollars":
        converted_amount = quantity / usd_rate
        return f"${converted_amount:.2f}"
    elif currency == "yen":
        converted_amount = quantity / jpy_rate
        return f"¥{converted_amount:.2f}"
    elif currency == "libras":
        converted_amount = quantity / gbp_rate
        return f"£{converted_amount:.2f}"
    else:
        return "Moneda no soportada"
#
def calculateQuadraticEquation(a, b, c):
    discriminant = b**2 - 4*a*c
    if discriminant < 0:
        print('¡The equation has no real solutions!')
        return None
    else:
        x1 = (-b + math.sqrt(discriminant)) / (2*a)
        x2 = (-b - math.sqrt(discriminant)) / (2*a)
        return x1, x2
    
while True:
    print("MENU")
    print("Select an option: ")
    print("1.Calculate figures")
    print("2.Calculate the prime number")
    print("3.Calculate the factorial number")
    print("4.Convert pesos to another currency")
    print("5.Solving a quadratic equation")
    print("6. Exit")
    option = input()
    
    if option == "1":
        print("Select the figure you want to calculate ")
        print("1.Circle")
        print("2.Triangle")
        print("3.Square")
        figure = input("Ingresa el numero de la figura que deseas realizar: ")
        if figure == "1":
            radio = float(input("Enter the radius of the circle: "))
            print("The area of ​​the circle is: ", calculateAreaCircle(radio))
        elif figure == "2":
            base = int(input("Enter the base of the triangle: "))
            height = int(input("Enter the height of the triangle: "))
            print("The area of ​​the triangle is: ", calculateTriangleArea(base,height))
        else:
            side = int(input("Enter from the side of the square: "))
            print("The area of ​​the square is: ", calculateSquareArea(side))

        options = input("¿Do you want to select another calculator? s/n\n")


    elif option == "2":

        while options.upper() == "S":
            num = int(input("Enter a number: "))
            print("¿Is the entered number prime? ",isPrime(num))

            options = input("¿Do you want to enter another number? s/n\n")

    elif option == "3":
         
        while options.upper() == "S":
            num = int(input("Enter a number: "))
            print("The result of the factorial number is: ", factorialNumber(num))

            options = input("¿Do you want to enter another number? s/n\n")

    elif option == '4':
        quantity = float(input('Enter the amount of pesos: '))
        currency = input('Enter the currency you want to convert to (dollars, yen or pounds): ')
        result = currencyConverter(quantity, currency)
        if result is not None:
            print(f'{quantity} weights is equivalent to {result} {currency}.')
    
    elif option == '5':
        a = float(input('Enter the coefficient a: '))
        b = float(input('Enter the coefficient b: '))
        c = float(input('Enter the coefficient c: '))
        result = calculateQuadraticEquation(a, b, c)
        if result is not None:
            print(f'The results are: {result[0]} y {result[1]}.')
    
    elif option == '6':
        print('¡See you later!')
        break
    
    else:
        print('Invalid option, try again.')
'''
