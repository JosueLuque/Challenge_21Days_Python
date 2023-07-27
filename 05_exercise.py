'''
    -- Encuentra a los gatitos más famosos --
    En este desafío, debes encontrar al gatito más famoso con base en su número de seguidores.
    Recibirás una lista de diccionarios que incluirán las siguientes propiedades:
        "name": nombre del gatito.
        "followers": una lista de números, donde cada uno representa los seguidores de cada red social.
    Tu tarea es devolver una lista con los nombres de los gatos que tienen solo el mayor número de seguidores. 
    Si hay dos o más gatos con el mismo número máximo de seguidores, deberás incluirlos en la lista resultante, 
    manteniendo el orden en el que aparecen en la lista de entrada.
'''


def find_famous_cat(cats):
    famous = max(sum(cat['followers']) for cat in cats)
    nameCat = [cat['name'] for cat in cats if famous == sum(cat['followers'])]
    return nameCat


cats = [
    {
        "name": "Luna",
        "followers": [500, 200, 300]
    },
    {
        "name": "Michi",
        "followers": [100, 300]
    },
    {
        "name": "Gizmo",
        "followers": [250, 750]
    },
]


result = find_famous_cat(cats)

print(result)
