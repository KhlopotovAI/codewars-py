# https://www.codewars.com/kata/tribonacci-sequence/train/python


def tribonacci(signature, n):
    if len(signature) >= n:
        return signature[0:n]

    while len(signature) != n:
        curlen = len(signature) - 1
        signature.append(signature[curlen] + signature[curlen - 1] + signature[curlen - 2])

    return signature
