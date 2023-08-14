'''
    -- Hash table para contactos --
    En este desafío, debes construir una lista de contactos mediante una hash table.
    Tu objetivo será implementar la lógica de la clase ContactList para agregar contactos y realizar las operaciones correspondientes.

    La hash table (ContactList) deberá tener los siguientes métodos:

        :) insert(name, phone): este método recibirá el nombre y el número de teléfono de un contacto y agregará este último a la hash table.
        :) get(name): este método recibirá el nombre de un contacto y devolverá su número de teléfono. Si el contacto no existe, retornará None.
        :) retrieveAll(): este método devolverá una lista con todos los buckets utilizados en la hash table.
        :) delete(name): este método recibirá el nombre de un contacto y eliminará dicho contacto de la hash table. En caso de no encontrar el nombre, debe retornar None.
'''


class ContactList:
    def __init__(self, size):
        self.size = size
        self.buckets = [[] for _ in range(size)]

    def hash(self, key):
        return hash(key) % self.size

    def insert(self, name, phone):
        index = self.hash(name)
        self.buckets[index].append((name, phone))

    def get(self, name):
        index = self.hash(name)
        for contact in self.buckets[index]:
            if contact[0] == name:
                return contact[1]
        return None

    def retrieveAll(self):
        all_values = []
        for bucket in self.buckets:
            for key, value in bucket:
                all_values.append([key, value])
        return all_values

    def delete(self, name):
        index = self.hash(name)
        for i, contact in enumerate(self.buckets[index]):
            if contact[0] == name:
                del self.buckets[index][i]
                return
        return None

    def showTable(self):
        return self.buckets


# Checking
contactList = ContactList(10)
contactList.insert("Mr michi", "123-456-7890")
contactList.delete("Mr michi")

r = contactList.get("Mr Michi")
print(r)

contactList = ContactList(10)
contactList.insert("Mr michi", "123-456-7890")

re = contactList.get("Mr michi")
print(re)

contactList = ContactList(10)
contactList.insert("Mr michi", "123-456-7890")

res = contactList.retrieveAll()
print(res)

contactList.insert("Mr dog", "123-456-8923")

resu = contactList.showTable()
print(resu)
