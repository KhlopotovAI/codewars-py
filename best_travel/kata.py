# https://www.codewars.com/kata/best-travel/train/python
import itertools


def choose_best_sum(t, k, ls):
    return max(filter(lambda x: x <= t, map(lambda y: sum(y), itertools.combinations(ls, k))), default=None)
