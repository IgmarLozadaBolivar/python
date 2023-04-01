import json

lista = [10, 20, 30, 40, 60]

with open("./archivo/lista.json","w") as archivo:
    json.dump(lista,archivo)

archivo.close()