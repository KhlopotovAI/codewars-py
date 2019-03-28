# https://www.codewars.com/kata/encrypt-this/train/python
def encrypt_this(text):
    return " ".join(map(lambda x: str(ord(x[0])) + (x[-1] + x[2:-1] + x[1] if len(x) > 2 else x[1:]), text.split()))
