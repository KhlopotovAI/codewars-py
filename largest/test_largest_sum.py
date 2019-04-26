import random
from unittest import TestCase

from .kata import largest_sum


class TestLargestSum(TestCase):
    def test_largest_sum(self):
        randu78(self)


def randu78(test):
    def lsy87(arr):
        a, b, ar = 0, 0, arr[:]
        for i in ar:
            b += i
            if b < 0: b = 0
            if b > a: a = b
        return a

    for i in range(0, 100):
        res, r = [], random.randrange(4, 100)
        for j in range(r):
            neg = -1 if random.randrange(0, 2) == 0 else 1
            res.append(neg * random.randrange(100, 200))
        exp = lsy87(res)
        test.assertEqual(largest_sum(res), exp)

    i = 10000
    while i <= 1000000:
        res = []
        for j in range(0, i):
            neg = -1 if random.randrange(0, 2) == 0 else 1
            res.append(neg * random.randrange(100, 200))
        exp = lsy87(res)
        test.assertEqual(largest_sum(res), exp)
        i *= 10
