# https://www.codewars.com/kata/integers-recreation-one/train/python
from functools import reduce

from math import sqrt

mem = {
    0: None,
    1: [1, 1]
}


def list_squared(m, n):
    res = []

    for i in range(m, n):
        if i in mem and mem[i]:
            res.append(mem[i])
            continue

        s = sum(map(lambda x: x ** 2, divisors_list(i)))
        if sqrt(s).is_integer():
            res.append([i, s])
        else:
            mem[i] = None

    return res


def divisors_list(n):
    res = set(reduce(list.__add__, ([i, n // i] for i in range(1, int(n ** 0.5) + 1) if n % i == 0)))
    res.add(n)
    return res
