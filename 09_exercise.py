'''
    -- Encuentra el mayor palíndromo --
    En este desafío, debes crear una función que encuentre el palíndromo más largo en una lista de palabras.
    Recibirás un único parámetro: una lista de palabras. Si no hay ningún palíndromo en la lista, la función debe devolver None. 
    Si hay más de un palíndromo con la misma longitud máxima, debes devolver el primer palíndromo encontrado en la lista.
'''


def find_largest_palindrome(words):
    palindromes = [word for word in words if word == word[::-1]]
    # key de la función max() -> especificar una función de ordenación
    # max() comparará las cadenas en la lista palindromes según su longitud y devolvera el mas largo, en caso de que la lista este vacia retornara None.
    return max(palindromes, key=len, default=None)


palindromes = ["radar", "racecar", "level", "world", "hello"]

result = find_largest_palindrome(palindromes)
print(result)
