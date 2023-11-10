from random import randint


def random_number(n):
    minimum = pow(10, n - 1)
    maximum = pow(10, n) - 1
    return randint(minimum, maximum)
