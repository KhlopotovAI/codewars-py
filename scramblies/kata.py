# https://www.codewars.com/kata/scramblies/train/python
from collections import Counter


def scramble(s1, s2):
    s1_counter = Counter(s2)
    s2_counter = Counter(s1)

    for k in s1_counter:
        if s2_counter.get(k, 0) < s1_counter.get(k):
            return False

    return True
