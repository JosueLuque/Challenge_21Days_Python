from node_mail import Mail

'''
    -- Implementación de un queue --
    En este ejercicio, debes implementar la lógica para procesar correos electrónicos en una empresa utilizando una 
    queue, donde los correos más antiguos tienen prioridad. Para ello, deberás crear una clase llamada Queue para 
    representar la cola de correos electrónicos. La clase debe tener los siguientes métodos:

    :) enqueue(from, to, body, subject): Agrega un correo electrónico al final de la cola.

    :) dequeue(): Elimina y devuelve un objeto con las siguientes propiedades: { from, to, body, subject } del correo 
    electrónico más antiguo de la cola.

    :) peek(): Devuelve el correo electrónico más antiguo de la cola sin eliminarlo.

    :) size(): Devuelve la cantidad de correos electrónicos en la cola.

    Tendrás una clase Mail ya construida para usarla dentro del desarrollo de tu solución que simulará ser un nodo dentro de la queue.
'''


class Queue:
    def __init__(self):
        self.first = None
        self.last = None
        self.length = 0

    def enqueue(self, from_email, to, body, subject):
        new_mail = Mail(from_email, to, body, subject)
        if self.is_empty():
            self.first = new_mail
            self.last = new_mail
        else:
            self.last.next = new_mail
            self.last = new_mail
        self.length += 1

    def dequeue(self):
        if self.is_empty():
            raise IndexError("La queue está vacía")
        removed_mail = self.first
        if self.first == self.last:
            self.last = None
        self.first = self.first.next
        self.length -= 1
        return removed_mail

    def peek(self):
        if self.length == 0:
            raise IndexError("No se encontraron correos, queue vacia")
        return self.first

    def is_empty(self):
        return self.length == 0

    def size(self):
        return self.length


# Checking
emailQueue = Queue()

emailQueue.enqueue(
    'caro@ejemplo.com',
    'support@ejemplo.com',
    'No puedo iniciar sesión en mi cuenta',
    'Problema de inicio de sesión'
)

emailQueue.enqueue(
    'josue@ejemplo.com',
    'support@ejemplo.com',
    'Mi pedido no ha llegado todavía',
    'Estado del pedido'
)

email = emailQueue.dequeue()
print(email.from_email)
