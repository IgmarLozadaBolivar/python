# Función para registrar a un expert trainer
def registrar_expert_trainer():
    expert_trainer = {}
    expert_trainer["nombre"] = input("Ingrese el nombre del expert trainer: ")
    expert_trainer["edad"] = int(input("Ingrese la edad del expert trainer: "))
    expert_trainer["correo"] = input("Ingrese el correo electrónico del expert trainer: ")
    expert_trainer["telefono"] = input("Ingrese el número de teléfono del expert trainer: ")
    expert_trainer["lenguaje"] = input("Ingrese el lenguaje de programación que enseñará el expert trainer: ")
    return expert_trainer

# Función para agregar un camper a la lista de campers
def agregar_camper(lista_campers):
    camper = {}
    camper["nombre"] = input("Ingrese el nombre del camper: ")
    camper["edad"] = int(input("Ingrese la edad del camper: "))
    camper["correo"] = input("Ingrese el correo electrónico del camper: ")
    camper["telefono"] = input("Ingrese el número de teléfono del camper: ")
    lista_campers.append(camper)

# Función para imprimir la lista de campers y reportar los menores y mayores de edad
def reportar_campers(lista_campers):
    print("Lista de campers:")
    for camper in lista_campers:
        print("- Nombre:", camper["nombre"])
        print("  Edad:", camper["edad"])
        print("  Correo electrónico:", camper["correo"])
        print("  Número de teléfono:", camper["telefono"])
    
    edades = [camper["edad"] for camper in lista_campers]
    mayor_edad = max(edades)
    menor_edad = min(edades)
    campers_mayores_edad = [camper["nombre"] for camper in lista_campers if camper["edad"] == mayor_edad]
    campers_menores_edad = [camper["nombre"] for camper in lista_campers if camper["edad"] == menor_edad]
    
    print("Campers de mayor edad:",
         ", ".join(campers_mayores_edad))
    print("Campers de menor edad:",
         ", ".join(campers_menores_edad))

# Programa principal
expert_trainer = registrar_expert_trainer()
print("Se ha registrado al expert trainer con éxito.")

lista_campers = []
while True:
    opcion = input("Ingrese 1 para agregar un camper a la lista o 2 para salir: ")
    if opcion == "1":
        agregar_camper(lista_campers)
        print("El camper ha sido agregado a la lista con éxito.")
    elif opcion == "2":
        break
    else:
        print("Opción inválida. Intente de nuevo.")

reportar_campers(lista_campers)
