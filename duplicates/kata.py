# https://www.codewars.com/kata/counting-duplicates/train/python
from collections import Counter


def duplicate_count(text):
    return sum(v > 1 for k, v in Counter(text.lower()).items())
