# https://www.codewars.com/kata/keep-it-short-with-restrictions/train/python
short = lambda l: {kv: sum(list(x).count(kv) for x in l) for kv in {item for sublist in l for item in sublist}}
