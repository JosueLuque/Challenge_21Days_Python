from pay import Pay

'''
    Sub Class - exercise 19
'''


class Cash(Pay):
    def make_pay(self, quantity):
        return super().make_pay(quantity)
