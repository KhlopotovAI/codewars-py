# https://www.codewars.com/kata/simple-number-sequence/train/python
def missing(s):
    return int(SequenceFinder().missing_number(s))


class SequenceFinder:
    def missing_number(self, sequence):
        for i in range(1, len(sequence) // 2):
            res = None
            splitter = Splitter(sequence, i)
            next_guess = splitter.first()
            while splitter.has_next():
                n = splitter.next()
                if n == next_guess:
                    pass
                elif n == self.inc(next_guess):
                    if res:
                        res = None
                        break
                    res = next_guess
                    next_guess = self.inc(next_guess)
                else:
                    res = None
                    break
                next_guess = self.inc(next_guess)
            if res:
                return res
        return -1

    @staticmethod
    def inc(num):
        return str(int(num) + 1)


class Splitter:
    def __init__(self, s, step):
        self.s = s
        self.step = step
        self.counter = 0

    def first(self):
        return self.s[0:self.step]

    def has_next(self):
        return self.counter < len(self.s)

    def next(self):
        if not self.has_next():
            return None
        num = self.s[self.counter:self.counter + self.step]
        self.counter += self.step
        self.inc_step_if_overflowing(num)
        return num

    def inc_step_if_overflowing(self, num):
        if len(str(int(num) + 2)) > len(num) and self.s[self.counter:self.counter + self.step] != str(int(num) + 1):
            self.step += 1
        pass
