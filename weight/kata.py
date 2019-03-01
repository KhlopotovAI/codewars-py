# https://www.codewars.com/kata/weight-for-weight/train/python
from functools import reduce


def order_weight(text):
    return ' '.join(sorted(sorted(text.split()), key=lambda x: reduce(lambda x1, x2: int(x1) + int(x2), list(x), 0)))
