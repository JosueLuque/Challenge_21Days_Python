'''
    -- Averigua si un año es bisiesto --
    En este desafío de Python, debes crear la lógica de la función is_leap_year, que determina si un año es bisiesto o no. 
    Un año es bisiesto si cumple con las siguientes condiciones:
    1. Es divisible por 4, pero no por 100.
    2. Si es divisible por 100 debe serlo por 400 también.

    La función is_leap_year recibe un único parámetro: el año a evaluar. Debe devolver True si el año es bisiesto o False en caso contrario.
    Toma en cuenta que la función debe ser capaz de manejar valores no enteros o negativos.
'''


def is_leap_year(year):
    if year > 0:
        if (year % 4 == 0) and (year % 100 != 0):
            return True
        elif (year % 100 == 0) and (year % 400 == 0):
            return True
        else:
            return False
    else:
        return False


result = is_leap_year(-2004)
print(result)   # False

result = is_leap_year(4000)
print(result)   # True
