# https://www.codewars.com/kata/find-the-parity-outlier/train/python


def find_outlier(integers):
    odd_or_even_arr = list(map(lambda x: x % 2 == 0, integers))
    if odd_or_even_arr.count(True) == 1:
        index = odd_or_even_arr.index(True)
    else:
        index = odd_or_even_arr.index(False)
    return integers[index]
