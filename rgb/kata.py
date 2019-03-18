# https://www.codewars.com/kata/rgb-to-hex-conversion/train/python
def rgb(r, g, b):
    normalize = lambda x: max(min(x, 255), 0)
    return hex((normalize(r) << 16) + (normalize(g) << 8) + normalize(b))[2:].zfill(6).upper()
