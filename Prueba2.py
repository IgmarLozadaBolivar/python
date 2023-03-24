print("\n\n")

otro = "S"

#Figuras
def proCirculo(radio):
        area = (radio**2)*3.1416
        return area
def proTriangulo(base, altura):
        area = (base * altura)/2
        return area
def proCuadrado(lado):
        area = (lado * lado)
        return area
    

#Numeros primos
def numPrimo (num):
    for n in range(2, num):
        if num % n == 0:
            return False
        return True


#Numero Factorial
def numFactorial (num):
        if num == 0 or num == 1:
          resultado = 1
        elif num > 1:
             resultado = num*numFactorial(num-1)
        return resultado


while otro.upper() == "S":
    print("***********MENU******************")
    print("Seleccione el ejercicio que desea realizar: ")
    print("1. Figuras")
    print("2. Numero primo")
    print("3. Numero factorial")
    print("4. Cambio moneda")
    print("5. Ecuacion cuadratica")
    opcion = input("Ingresa el numero que deseas realizar el ejercicio: ")
    
    if opcion == "1":

        print("Selecione el tipo de la figura que desea calcular ")
        print("1. Circulo")
        print("2. Triangulo")
        print("3. Cuadrado")
        tipoArea = input("Ingresa el numero de la figura que deseas realizar: ")
        if tipoArea == "1":
            radio = float(input("Ingresa el radio del circulo: "))
            print("El area del circulo es: ", proCirculo(radio))
        elif tipoArea == "2":
            base = int(input("Ingresa la base del triangulo: "))
            altura = int(input("Ingresa la altura del triangulo: "))
            print("El area del triangulo es: ", proTriangulo(base,altura))
        else:
            lado = int(input("Ingresa el lado del cuadrado: "))
            print("El area del cuadrado es: ", proCuadrado(lado))

        otro = input("¿Desea ingresar otra figura? s/n\n")
    
    elif opcion == "2":

        while otro.upper() == "S":
            num = int(input("Ingresa un numero: "))
            print("¿Es un numero primo el numero ingresado? ",numPrimo(num))

            otro = input("¿Desea ingresar otro numero? s/n\n")

    elif opcion == "3":
         
        while otro.upper() == "S":
            num = int(input("Ingresa un numero: "))
            print("¿El resultado del numero factorial es: ", numFactorial(num))

            otro = input("¿Desea ingresar otro numero? s/n\n")

    elif opcion == "4":
         
         while otro.upper() == "S":
              print




print("\n\n")

                 



