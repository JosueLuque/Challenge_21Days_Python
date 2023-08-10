from pay import Pay

'''
    Sub Class - exercise 19
'''


class Card(Pay):
    def __init__(self, card_number):
        super().__init__()
        self._card_number = card_number

    def make_pay(self, quantity):
        if len(self._card_number) != 16:
            raise Exception('El numero de tarjeta no es valido')
        else:
            info_pay = super().make_pay(quantity)
            info_pay['last_card_numbers'] = self._card_number[-4:]
            return info_pay

    # Decorators (access a private attribute as if it were a public property)
    @property
    def card_number(self):
        return self._card_number

    @card_number.setter
    def card_number(self, card_number):
        self._card_number = card_number
