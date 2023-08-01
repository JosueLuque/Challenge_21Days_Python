'''
    -- Encuentra palabras con dos vocales --
    En este desafío, debes crear la lógica de la función find_words_with_two_vowels que encuentre las palabras que 
    contienen exactamente dos vocales en una lista de palabras. Las vocales pueden ser tanto mayúsculas como minúsculas.
    Recibirás un único parámetro: una lista de palabras. La función debe devolver una nueva lista que contenga todas 
    las palabras de la lista original que cumplan con la condición mencionada anteriormente. En caso de no haber palabras 
    que cumplan con esta condición deberás retornar una lista vacía.
'''


# Sin list comprehension
def find_words_with_two_vowels(words):
    vowels = 'aeiouAEIOU'
    result = []
    for word in words:
        num_vowels = sum(1 for character in word if character in vowels)
        if num_vowels == 2:
            result.append(word)
    return result


# Con list comprehension
def find_words_with_two_vowels_v2(words):
    vowels = 'aeiouAEIOU'
    return [word for word in words if sum(1 for character in word if character in vowels) == 2]


r = find_words_with_two_vowels_v2([
    "hello",
    "Python",
    "world",
    "platzi"
])

print(r)
