# https://www.codewars.com/kata/make-the-deadfish-swim/train/python
class Parser:
    def __init__(self, data):
        self.value = 0
        self.arr = []
        self.data = data

    def plus(self):
        self.value += 1

    def minus(self):
        self.value -= 1

    def square(self):
        self.value **= 2

    def out(self):
        self.arr.append(self.value)

    def nothing(self):
        pass

    def parse(self):
        for d in self.data:
            commands.get(d, Parser.nothing)(self)
        return self.arr


commands = {
    "i": Parser.plus,
    "d": Parser.minus,
    "s": Parser.square,
    "o": Parser.out
}


def parse(data):
    return Parser(data).parse()
