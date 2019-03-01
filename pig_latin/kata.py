# https://www.codewars.com/kata/simple-pig-latin/train/python
import string


def pig_it(text):
    return " ".join(map(lambda x: x[1:len(x)] + x[0] + "ay" if x not in string.punctuation else x, text.split()))
