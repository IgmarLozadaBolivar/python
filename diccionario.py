import json

diccionario = {'1':'Lapiz','2':'Borrador','3':'Cuaderno','4':'Lapicero'}

with open("./archivo/diccionario.json","w") as archivo:
    json.dump(diccionario,archivo)

archivo.close()