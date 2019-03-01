# https://www.codewars.com/kata/calculating-with-functions/train/python


def calc(**kwargs):
    arg = kwargs.get("arg")
    if arg == ():
        return kwargs.get("current")
    if len(arg[0]) == 2:
        return int(eval(kwargs.get("current") + arg[0]))
    else:
        return kwargs.get("current") + arg[0]


def zero(*args):  # your code here
    return calc(arg=args, current="0")


def one(*args):  # your code here
    return calc(arg=args, current="1")


def two(*args):  # your code here
    return calc(arg=args, current="2")


def three(*args):  # your code here
    return calc(arg=args, current="3")


def four(*args):  # your code here
    return calc(arg=args, current="4")


def five(*args):  # your code here
    return calc(arg=args, current="5")


def six(*args):  # your code here
    return calc(arg=args, current="6")


def seven(*args):  # your code here
    return calc(arg=args, current="7")


def eight(*args):  # your code here
    return calc(arg=args, current="8")


def nine(*args):  # your code here
    return calc(arg=args, current="9")


def plus(*args):  # your code here
    return calc(arg=args, current="+")


def minus(*args):  # your code here
    return calc(arg=args, current="-")


def times(*args):  # your code here
    return calc(arg=args, current="*")


def divided_by(*args):  # your code here
    return calc(arg=args, current="/")
