# https://www.codewars.com/kata/stop-gninnips-my-sdrow/train/python
from functools import reduce


def spin_words(sentence):
    return reduce(lambda x1, x2: x1 + " " + x2, map(lambda x: x[::-1] if len(x) >= 5 else x, sentence.split()))
