from Node import PatientNode
'''
    -- Implementación de una singly linked list --
    En este desafío, vamos a implementar una lista enlazada simple para almacenar información sobre pacientes de un hospital.
    Cada nodo de la lista representará a un paciente y tendrá los siguientes campos:

    Nombre del paciente (cadena de texto)
    Edad del paciente (número)
    Número de cama asignada al paciente (número)
    La lista enlazada deberá tener los siguientes métodos:

    :) addPatient(name, age): agrega un nuevo paciente a la lista, asignándole la próxima cama disponible. Si no hay camas disponibles,
    debe lanzar un error con el mensaje "No hay camas disponibles".

    :) removePatient(name): remueve al paciente con el nombre especificado de la lista y libera su cama. Si el paciente no se encuentra
    en la lista, debe lanzar un error con el mensaje "Paciente no encontrado".

    :) getPatient(name): retorna la información del paciente con el nombre especificado en el siguiente formato {name, age, bedNumber}.
    Si el paciente no se encuentra en la lista, debe lanzar un error con el mensaje "Paciente no encontrado".

    :) getPatientList(): retorna una lista con la información de todos los pacientes en la lista, cada paciente deberá tener el siguiente
    formato {name, age, bedNumber}.

    :) getAvailableBeds(): retorna un número con el total de camas disponibles.
'''


class PatientList:
    def __init__(self, max_beds):
        self.head = None
        self.tail = None
        self.length = 0
        self.max_beds = max_beds

    def addPatient(self, name, age):
        if self.getAvailableBeds() != 0:
            newNode = PatientNode(name, age, self.length + 1)
            if self.head is None:
                self.head = newNode
                self.tail = newNode
            else:
                self.tail.next = newNode
                self.tail = newNode
            self.length += 1
        else:
            raise Exception("No hay camas disponibles")

    def removePatient(self, name):
        if self.head is None:
            return

        if self.head.name == name:
            self.head = self.head.next
            self.length -= 1
            return

        current_node = self.head
        while current_node.next:
            if current_node.next.name == name:
                current_node.next = current_node.next.next
                self.length -= 1
                return
            current_node = current_node.next

    def getPatient(self, name):
        if self.head is None:
            raise Exception("Paciente no encontrado")
        current = self.head
        while current:
            if current.name == name:
                return {
                    "name": current.name,
                    "age": current.age,
                    "bedNumber": current.bed_number
                }
            current = current.next
        raise Exception("Paciente no encontrado")

    def getPatientList(self):
        patients = []
        current = self.head
        while current:
            patients.append({
                'name': current.name,
                'age': current.age,
                'bedNumber': current.bed_number
            })
            current = current.next
        return patients

    def getAvailableBeds(self):
        return self.max_beds - self.length


# Checking
list = PatientList(3)
list.addPatient("Paciente 1", 20)
list.addPatient("Paciente 2", 30)
list.addPatient("Paciente 3", 19)

r = list.getPatientList()
print(r)

re = list.getPatient("Paciente 3")
print(re)

list.removePatient("Paciente 1")
list.removePatient("Paciente 3")
res = list.getPatientList()
print(res)
