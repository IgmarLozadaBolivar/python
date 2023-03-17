products = []
name = input('Ingrese nombre de articulo: ')
products.append(name)
price = int(input('Ingrese el precio: '))
total = price
products(name,price)
continuar = True
while continuar:
    respuesta = input('¿Desea agg otro producto? Yes/No: ')

    if respuesta == 'Yes':
        name == input('Ingrese el nombre del producto')
        products.append(name)
        price = int(input('Enter the price: '))
        products(name,price)
        total += price
    else:
        continuar = False

print('Los articulos comprados fueron: \n' + str(products))
print('El total de la compra es: ' + str(total))