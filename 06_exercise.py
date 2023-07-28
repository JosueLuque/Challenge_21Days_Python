'''
    -- Obtén el promedio de los estudiantes --
    En este desafío, deberás calcular el promedio general de una clase, así como el promedio individual de cada estudiante.
    Para ello, se te proporcionará una lista de diccionarios, cada uno de los cuales representará a un estudiante y tendrá 
    las siguientes propiedades:
        "name": El nombre del estudiante
        "grades": Las notas de cada materia del estudiante
    A partir de esta información, debes retornar un nuevo diccionario que tenga la propiedad "class_average" con el promedio de la clase 
    y una lista de "students" con los estudiantes y sus promedios individuales.
    Es importante mencionar que los promedios deben ser calculados con precisión y se deben redondear a dos decimales para que los test 
    pasen sin problema alguno.

'''


def get_student_average(students):
    to_class = {
        "class_average": 0,
        "students": [],
    }
    average_class = 0
    for s in students:
        student = {
            'name': s['name'],
            'average': round(sum(s['grades'])/len(s['grades']), 2)
        }
        average_class += student['average']
        to_class['students'].append(student)

    to_class['class_average'] = round(average_class/len(students), 2)
    return to_class


students = [
    {
        "name": "Pedro",
        "grades": [90, 87, 88, 90],
    },
    {
        "name": "Jose",
        "grades": [99, 71, 88, 96],
    },
    {
        "name": "Maria",
        "grades": [92, 81, 80, 96],
    },
]


result = get_student_average(students)
print(result)
