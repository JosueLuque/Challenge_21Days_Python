'''
    -- Implementa un sistema de pagos --
    En este desafío, tendrás que implementar un sistema de pagos utilizando polimorfismo.

    Debes crear una clase base llamada Pay que contenga un único método llamado make_pay. Este método recibirá la cantidad a pagar y 
    devolverá un objeto con dos propiedades

    realized: true
    quantity: $cantidadAPagar
    Además, deberás crear también las clases PayPal, Card y Cash, donde cada una debe heredar de la clase Pay.

    La clase PayPal debe recibir un email en el constructor y el método make_pay debe agregar las propiedades:

    platform: "PayPal"
    email: $EmailRecibido.
    La clase Card recibirá un número de tarjeta de 16 dígitos. Al momento de acceder al método make_pay, se validará si la tarjeta en 
    cuestión tiene esa longitud. En caso de no tener los 16 dígitos, se debe lanzar una Exception. En caso contrario, al método que 
    proviene de Pay, se le agregará la propiedad de last_card_numbers: donde se devolverán los últimos 4 dígitos de la tarjeta.

    La clase Cash simplemente nos devolverá lo mismo que la clase base.

    Por último se debe implementar la lógica de la función process_pay la cual recibirá un método de pago y la cantidad, para poder 
    devolver el objeto llamando al método make_pay de cada entidad recibida.
'''

from paypal import PayPal
from cash import Cash
from card import Card


def process_pay(payment_method, amount):
    return payment_method.make_pay(amount)


# Checkingv Card
card = Card("4913478952471122")
result = process_pay(card, 100)
print(result)
print(card.card_number)

card.card_number = "8372872832399232"
print(card.card_number)
result_v2 = process_pay(card, 100)
print(result_v2)

# Checkin PayPal
paypal = PayPal("test@gmail.com")
result_2 = process_pay(paypal, 240)
print(result_2)
print(paypal.email)

paypal.email = "josue@gmail.com"
print(paypal.email)
result_2_v1 = process_pay(paypal, 240)
print(result_2_v1)

# Checking Cash
cash = Cash()
result_3 = process_pay(cash, 400)
print(result_3)
