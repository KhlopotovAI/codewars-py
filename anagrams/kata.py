# https://www.codewars.com/kata/where-my-anagrams-at/train/python
from collections import Counter


def anagrams(word, words):
    word_counter = Counter(word)
    word_len = len(word)
    return list(filter(lambda x: len(x) == word_len and not Counter(x) - word_counter, words))
