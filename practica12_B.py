import json

"""Guarda el contenido (str) en un archivo .json"""
def crearjson():
    book = """
        {
        "book":[
            {"titel":"El Señor de los Anillos",
             "cover":"dura",
             "year":"2002",
             "pages":"124"
             }
            {"titel":"Harry Potter",
             "cover":"blanda",
             "year":"1999",
             "pages":"245"
             }
            {"titel":"La Rueda del Tiempo",
             "cover":"dura",
             "year":"2005",
             "pages":"420"
             }
            {"titel":"The witcher",
             "cover":"dura",
             "year":"1899",
             "pages":"123"
             }
        ]
    """
    with open("book.json",'w') as file:
        json.dump(book,file)

"""Función que muestra por consola el contenido del archivo .json"""
def leerjson():
    with open("book.json",'r') as file:
        result = json.load(file)
        print(result)
