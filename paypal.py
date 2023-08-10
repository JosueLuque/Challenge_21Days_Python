from pay import Pay
'''
    Sub Class - exercise 19
'''


class PayPal(Pay):
    def __init__(self, email):
        super().__init__()
        self._email = email

    def make_pay(self, quantity):
        info = super().make_pay(quantity)
        info['platform'] = "Paypal"
        info['email'] = self._email
        return info

    # Decorators (access a private attribute as if it were a public property)
    @property
    def email(self):
        return self._email

    @email.setter
    def email(self, value):
        self._email = value
