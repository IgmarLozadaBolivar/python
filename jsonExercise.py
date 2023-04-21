empresa = {
    'personas' : [
        {
            'ID': 1,
            'Nombre': 'Pedro',
            'Edad': '20',
            'numdoc': 123456789
        },
        {
            'ID': 2,
            'Nombre': 'Ofelia',
            'Edad': '30',
            'numdoc': 123456788
        },
        {
            'ID': 3,
            'Nombre': 'Ruth',
            'Edad': '17',
            'numdoc': 123456787
        }
    ]
}

import json

def crearJson():
        with open('empresa.json','w') as archivo:
            json.dump(empresa, archivo)
        archivo.close()

def cargarJson():
        with open('empresa.json','r') as archivo:
            empresa = json.load(archivo)
        archivo.close()
"""         print('EMPRESA: ', empresa)
        for i in range(len(empresa)):
            print(empresa[i]) """
