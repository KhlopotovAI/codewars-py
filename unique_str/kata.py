# https://www.codewars.com/kata/find-the-unique-string/train/python
from functools import lru_cache


def find_uniq(arr):
    if normalize(arr[0]) != normalize(arr[1]):
        if normalize(arr[0]) != normalize(arr[2]):
            return arr[0]
        elif normalize(arr[0]) == normalize(arr[2]):
            return arr[1]
        else:
            return arr[2]
    not_unique = normalize(arr[0])

    for i in range(1, len(arr)):
        if normalize(arr[i]) != not_unique:
            return arr[i]
    raise ArithmeticError("There is no unique string in the list.")


@lru_cache(maxsize=64)
def normalize(s):
    return "".join(set(sorted(map(lambda x: x.lower(), s)))).strip()
