'''
    -- Crea tu propia Lista en Python --
    Tu objetivo es crear una clase llamada MyList que simule el comportamiento de una Lista nativa en Python, sin utilizar 
    los métodos ya existentes. Implementarás la lógica de los siguientes métodos:

    map(func): itera sobre cada elemento de nuestra estructura aplicando la función func a cada uno de ellos y devuelve una 
    nueva lista (que será una instancia de MyList).

    filter(func): itera sobre cada elemento de nuestra estructura filtrándolos según lo que indique la función func y devuelve 
    una lista con los elementos filtrados (también una instancia de MyList).

    join(character): concatena todos los elementos de nuestra estructura de datos en un string, separándolos por el carácter 
    indicado (character). Si no se proporciona un carácter, el separador por defecto será una coma ",".

    append(item): agrega un elemento item al final de la lista y aumenta la longitud (length).

    pop(): elimina el último elemento de la lista y lo retorna, disminuyendo también la longitud (length).

    shift(): elimina el primer elemento de la lista y lo retorna, disminuyendo la longitud (length).

    unshift(item): agrega un elemento item al inicio de la lista y aumenta la longitud (length).

    Además, deberás almacenar los elementos dentro de la propiedad data y el número de elementos dentro de la propiedad length, 
    para que puedan ser consultados desde las pruebas.
'''


class MyList:
    def __init__(self):
        self.data = {}
        self.lenght = 0

    def append(self, item):
        self.data[self.lenght] = item
        self.lenght += 1

    def pop(self):
        self.lenght -= 1
        element = self.data[self.lenght]
        del self.data[self.lenght]
        return element

    def shift(self):
        self.lenght -= 1
        element = self.data[0]
        del self.data[0]
        self.data = {item - 1: value for item, value in self.data.items()}
        return element

    def unshift(self, item):
        if self.data != {}:
            aux = dict()
            aux[0] = item
            for item_index, value in self.data.items():
                aux[item_index + 1] = value
            self.data = aux
            self.lenght += 1

    def map(self, func):
        data_with_map = MyList()
        item_index = 0
        while item_index < self.length:
            data_with_map.append(func(self.data[item_index]))
            item_index += 1
        return data_with_map

    def filter(self, func):
        data_with_filter = MyList()
        item_index = 0
        while item_index < self.length:
            if func(self.data[item_index]):
                data_with_filter.append(self.data[item_index])
            item_index += 1
        return data_with_filter

    def join(self, character=','):
        result = ""
        for item_index in range(len(self.data)):
            if result == "":
                result += str(self.data[item_index])
            else:
                result += character + str(self.data[item_index])
        return result


# Checking
objeto = MyList()
objeto.append("Platzinauta")

objeto.unshift("Hola!")

print(objeto.data)
print(objeto.lenght)

myList = MyList()
myList.append("a")
myList.append("b")
myList.append("c")
r = myList.join()
print(r)
print(myList.data)
