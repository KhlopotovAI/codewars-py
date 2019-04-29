# https://www.codewars.com/kata/1-slash-n-cycle/train/python
def cycle(n):
    if n % 2 == 0 or n % 5 == 0:
        return -1

    mod_val = 10 % n
    curr_mod = mod_val
    k = 1
    while curr_mod != 1:
        curr_mod = (curr_mod * mod_val) % n
        k += 1

    return k
