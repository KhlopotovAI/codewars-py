# https://www.codewars.com/kata/unique-in-order/train/python
def unique_in_order(iterable):
    res = []
    prev = None
    for e in iterable:
        if e == prev:
            continue
        res.append(e)
        prev = e
    return res
