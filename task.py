"""
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
"""

#precio de las boletas
priceValueGeneral = 50
priceValueVip = 75
priceValuePlatinum = 100

#Variables de venta y recaudos
generalQuantity = 0
vipQuantity = 0
platinumQuantity = 0
generalCollection = 0
vipCollection = 0
platinumCollection = 0

#Solicitar la información de las ventas de boletas
while True:
    ballot_Type = input(f"Enter the type of ticket sold:\n 1.General ticket\n 2.VIP ticket\n 3.Platinum ticket\n 4.Press any key to finish\n ")
    if ballot_Type == '':
        break
    elif ballot_Type == '1':
        quantity = int(input("Enter the number of general tickets sold: "))
        generalQuantity += quantity
        generalCollection += quantity * priceValueGeneral
    elif ballot_Type == '2':
        quantity = int(input("Enter the number of VIP tickets sold: "))
        vipQuantity += quantity
        vipCollection += quantity * priceValueVip
    elif ballot_Type == '3':
        quantity = int(input("Enter the number of Platinum tickets sold: "))
        platinumQuantity += quantity
        platinumCollection += quantity * priceValuePlatinum
    else:
        print("¡Invalid ballot type!")

# Imprimir el resumen de ventas por tipo de boleta
print(f"Total tickets sold:\n"
      f"General tickets: {generalQuantity} Tickets sold for a total of {generalCollection}US$\n"
      f"VIP Tickets: {vipQuantity} Tickets sold for a total of {vipCollection}US$\n"
      f"Platinum tickets: {platinumQuantity} Tickets sold for a total of {platinumCollection}US$\n")
