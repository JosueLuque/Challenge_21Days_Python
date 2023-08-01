'''
    -- Calcula la longitud de las palabras --
    En este desafío, debes crear una función llamada count_words_by_length que recibe una lista de palabras 
    y devuelve un diccionario que mapea la longitud de las palabras a la cantidad de palabras que tienen esa longitud.
'''


def count_words_by_length(words):
    list_len_word = [len(word) for word in words]
    return {len_word: list_len_word.count(len_word) for len_word in list_len_word}


result = count_words_by_length([
    "apple",
    "banana",
    "orange",
    "grapefruit",
    "pear",
    "kiwi"
])

print(result)
