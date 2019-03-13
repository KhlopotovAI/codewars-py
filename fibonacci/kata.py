# https://www.codewars.com/kata/memoized-fibonacci/train/python
from functools import lru_cache


@lru_cache(maxsize=None)
def fibonacci(n):
    if n in [0, 1]:
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)
