# https://www.codewars.com/kata/moving-zeros-to-the-end/train/python


def move_zeros(array):
    new_arr = []
    zeros = 0
    for e in array:
        if isinstance(e, bool) or e != 0:
            new_arr.append(e)
        else:
            zeros += 1
    return new_arr + [0] * zeros
