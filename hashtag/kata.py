# https://www.codewars.com/kata/the-hashtag-generator/train/python
import re
from functools import reduce


def generate_hashtag(s):
    hashtag = reduce(lambda x1, x2: x1 + x2, map(lambda x: x.capitalize(), filter(None, re.split("\W", s))), "#")
    return hashtag if len(hashtag) <= 140 and hashtag != "#" else False
