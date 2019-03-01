# https://www.codewars.com/kata/human-readable-time/train/python


def make_readable(seconds):
    h = append_0(str(seconds // 60 // 60))
    m = append_0(str(seconds // 60 % 60))
    s = append_0(str(seconds % 60))
    return h + ":" + m + ":" + s


def append_0(x):
    return x if len(x) >= 2 else "0" + x
