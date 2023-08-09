'''
    -- Jerarquía de animales usando herencia --
    En este desafío, debes crear una jerarquía de clases mediante el uso de la herencia.

    La clase base será Animal con las propiedades name, age y specie y un método getInfo que devuelve un objeto con la información del animal.

    Luego, debes crear una clase Mammal que herede de Animal y tenga una propiedad adicional hasFur y un método getInfo que sobreescriba al del 
    padre y incluya la información de hasFur.

    Finalmente, debes crear una clase Dog que herede de Mammal y tenga una propiedad adicional breed y un método getInfo que sobreescriba al del 
    padre y incluya la información de breed, al igual que el método bark que devuelva el string "woof!". 
    
    Las propiedades de specie y hasFur deben estar incluídas como "dog" y True respectivamente desde la implementación por lo que no debe ser 
    necesario pasar los valores a la hora de crear la instancia.
'''


class Animal:
    def __init__(self, name, age, specie):
        self.name = name
        self.age = age
        self.specie = specie

    def getInfo(self):
        return {
            'name': self.name,
            'age': self.age,
            'specie': self.specie
        }


class Mammal(Animal):
    def __init__(self, name, age, specie, hasFur):
        super().__init__(name, age, specie)
        self.hasFur = hasFur

    def getInfo(self):
        info = super().getInfo()
        info['hasFur'] = self.hasFur
        return info


class Dog(Mammal):
    def __init__(self, name, age, breed):
        super().__init__(name, age, specie='dog', hasFur=True)
        self.breed = breed

    def getInfo(self):
        info = super().getInfo()
        info['breed'] = self.breed
        return info

    def bark(self):
        return 'woof!'


# checking
bird = Animal("pepe", 1, "bird")
print(bird.getInfo())


hippo = Mammal("bartolo", 3, "hippo", False)
print(hippo.getInfo())


dog = Dog("fido", 4, "pastor aleman")
print(dog.bark())
