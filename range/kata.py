# https://www.codewars.com/kata/range-extraction/train/python
def solution(args):
    next_guess = args[0]
    res = ""
    seq = []
    for e in args:
        if e == next_guess:
            seq.append(e)
        else:
            res += seq_to_string(seq) + ","
            seq = [e]
            next_guess = e
        next_guess += 1
    if len(seq) > 0:
        res += (seq_to_string(seq))
    return res


def seq_to_string(seq):
    if len(seq) == 1:
        return str(seq[0])
    elif len(seq) == 2:
        return str(seq[0]) + "," + str(seq[1])
    else:
        return str(seq[0]) + "-" + str(seq[-1])
