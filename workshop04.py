#Dictionary list to store the information of purchased items (Dictionary's)
articles = {1:"Pencil", 2:"Notebooks", 3:"Draft", 4:"Calculator", 5:"Square"}
values = {1:2500, 2:3800, 3:1200, 4:35000, 5:3700}

#Dictionary list to store the information of purchased items (list)
purchase = []

#Cycle to capture data from purchased items (Loop while, function append, break and conditionals)
while True:
    itemCode = int(input("Enter the item code, to finish enter 0: "))
    if itemCode == 0:
        break
    quantity = int(input("Enter the number of units purchased: "))
    name = articles[itemCode]
    unitValue = values[itemCode]
    totalValue = quantity * unitValue
    articles = {"itemCode": itemCode, "Name": name, "Quantity": quantity, "unitValue": unitValue, "totalValue": totalValue}
    purchase.append(articles)

#Printing the information of the purchased items (Print's, loop for)
print("Purchase made:")
for articles in purchase:
    print("Item Code:", articles["itemCode"])
    print("Name:", articles["Name"])
    print("Quantity:", articles["Quantity"])
    print("Unit Value:", articles["unitValue"])
    print("Total Value:", articles["totalValue"])
    print()

#Calculation of the total purchase value (Print)
totalPurchaseValue = sum(articles["totalValue"] for articles in purchase)
print("Total Purchase Value:", totalPurchaseValue)
