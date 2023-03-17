print("\n\n\n")
product = ""
valor = ""
other = ""
amount = ""
total = ""
print("********** PURCHASE AND SALE LIST *********")

opction = print("Do you want to create a shopping list or calculate total sales?\n 1.Shopping\n 2.Sales\n")

if opction == "1":
    product += "\n" + input("\nEnter the product")
    valor = int(input("Enter the valor: "))
    product += "\t\t\t$" +str(valor)
    total += valor
    amount += 1
    other = input("\n¿Do you want to add another product? s/n\n")
    if other == "S" or other == "s":
        product += "\n" + input("\nEnter the product: ")
        valor = int(input("Enter the valor: $"))
        product += "\t\t\t$" + str(valor)
        total += valor
        amount += 1
print("********** SHOPPING *********")
print("\nPRODUCT\t\tVALOR")
print(product)
print("\nWere bought " + str(amount) + " products")
print("\nTOTAL: $" + str(total))
print("\n\n\n")