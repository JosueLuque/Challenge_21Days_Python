'''
    -- Calcula la cantidad de letras en una oración --
    En este desafío deberás implementar la lógica de una función que cuente la cantidad de ocurrencias de cada 
    letra en una cadena de texto y lo almacene en un diccionario.
    Es importante mencionar que la función debe ser sensible a mayúsculas y minúsculas, es decir, las letras 
    mayúsculas y minúsculas deben considerarse diferentes.
'''


def count_letters(phrase):
    return {letter: phrase.count(letter) for letter in phrase}


result = count_letters(input('Ingrese una oracion: '))
print(result)
