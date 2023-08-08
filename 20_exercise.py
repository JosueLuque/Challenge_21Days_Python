'''
    -- Encapsula los datos de los usuarios --
    En este desafío, debes implementar la lógica de la clase "Usuario" que represente un usuario en una red social y utilizar 
    encapsulamiento para proteger sus datos privados.

    La clase debe tener las siguientes variables privadas:
        name
        age
        friends (lista de diccionarios Usuario)
        messages (lista de strings)

    Además, debes proporcionar los siguientes métodos públicos:
        addFriend(friend): agrega un usuario a la lista de amigos del usuario actual.
        sendMessage(message, friend): agrega un mensaje a la lista de mensajes del usuario actual y al amigo especificado.
        showMessages(): devuelve la lista de mensajes del usuario actual.

    También debes tener definidos los getters y setters para acceder a los datos privados como el nombre y la edad, los cuales pueden 
    ser modificados mediante su propio setter.
'''


class User:
    def __init__(self, name, age):
        self._name = name
        self._age = age
        self._friends = []
        self._messages = []

    def addFriend(self, friend):
        self._friends.append(friend)

    def sendMessage(self, message, friend):
        self._messages.append(message)
        friend._messages.append(message)

    def showMessages(self):
        return self._messages

    @property
    def name(self):
        return self._name

    @property
    def age(self):
        return self._age

    @property
    def friends(self):
        return self._friends

    @property
    def messages(self):
        return self._messages

    @name.setter
    def name(self, value):
        self._name = value

    @age.setter
    def age(self, value):
        self._age = value


usuario1 = User("Juan", 20)
usuario1.name = "Pepito"
print(usuario1.name)
