# https://www.codewars.com/kata/valid-parentheses/train/python


def valid_parentheses(string):
    accumulator = []
    for char in string:
        if char == '(':
            accumulator.append(0)
        if char == ')':
            try:
                accumulator.pop()
            except IndexError:
                return False
    return len(accumulator) == 0
