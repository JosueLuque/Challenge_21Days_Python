'''
    --Dibuja un triangulo usando bucles--
    En este desafío, debes dibujar un triángulo equilatero usando bucles.

    Recibirás dos parámetros: size y character, que definen el número de filas que tendrá y el carácter 
    con el que se debe construir el triángulo, respectivamente. Además, el triángulo debe estar alineado 
    al centro, lo que significa que la misma cantidad de caracteres debe haber en ambos lados.

    Recuerda que para hacer el salto de línea debes usar "\n", no olvides removerla de la última parte, debes retornar todo esto en una variable.
'''


def print_triangle(size, character):
    triangle = ''
    for s in range(size):
        triangle += ' '*(size - s - 1)
        triangle += character * (2*s + 1)
        if s != size - 1:
            triangle += '\n'
    return triangle


result = print_triangle(7, '#')
print(result)
