# 0
numeros = []
while True:
    num = input("Ingrese un número (0 para terminar): ")
    if num == '0':
        break
    try:
        numeros.append(float(num))
    except ValueError:
        print("Error: Ingrese un número válido.")

if numeros:
    cuenta, promedio, sumatoria = len(numeros), sum(numeros) / len(numeros), sum(numeros)
    print(f"Cuenta: {cuenta}\nPromedio: {promedio}\nSumatoria: {sumatoria}")
else:
    print("No se ingresaron números.")

# 1
import math

numeros = []
while True:
    num = input("Ingrese un número entero (0 para terminar): ")
    if not num.isdigit():
        print("Error: Ingrese un número válido.")
        continue
    num = int(num)
    if num == 0:
        break
    numeros.append(num)

if numeros:
    raices = [math.sqrt(num) for num in numeros]
    promedio_raices = sum(raices) / len(raices)
    sumatoria_raices = sum(raices)
    print("Promedio aritmético de las raíces cuadradas:", promedio_raices)
    print("Sumatoria de las raíces cuadradas:", sumatoria_raices)
else:
    print("No se ingresaron números.")
