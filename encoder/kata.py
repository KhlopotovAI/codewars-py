# https://www.codewars.com/kata/duplicate-encoder/train/python


def duplicate_encode(word):
    word_in_lower = word.lower()
    return "".join(map(lambda x: ")" if word_in_lower.count(x) >= 2 else '(', list(word_in_lower)))
