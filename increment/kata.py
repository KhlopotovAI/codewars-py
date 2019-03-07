# https://www.codewars.com/kata/string-incrementer/train/python
import re


def increment_string(s):
    split = re.split("(\\d+$)", s)
    return split[0] + "1" if len(split) == 1 else split[0] + str(int(split[1]) + 1).zfill(len(split[1]))
