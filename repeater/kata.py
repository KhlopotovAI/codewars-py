# https://www.codewars.com/kata/lazy-repeater/train/python
class make_looper:
    def __init__(self, s):
        def gen(string):
            counter = -1
            while True:
                counter += 1
                if counter >= len(string): counter = 0
                yield string[counter]

        self.gen = gen(s)

    def __call__(self, *args, **kwargs):
        return next(self.gen)
