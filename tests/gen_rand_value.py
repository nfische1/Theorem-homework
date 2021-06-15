import random
import string


def random_string(self, stringLength=10):
    letters = string.ascii_letters
    return ''.join(random.choice(letters) for i in range(stringLength)).lower()


def random_number(self, range=10):
    amount = random.randrange(range)
    if amount < 1:
        amount = amount + 1
    return amount
