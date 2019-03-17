# https://www.codewars.com/kata/permutations/train/python
import itertools


def permutations(string):
    return ["".join(p) for p in set(itertools.permutations(string))]
