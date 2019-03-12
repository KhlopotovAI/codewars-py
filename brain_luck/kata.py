# https://www.codewars.com/kata/my-smallest-code-interpreter-aka-brainf-star-star-k/train/python
class BFInterpreter:

    def __init__(self, code, input):
        self.code = code
        self.memory = [0] * 255
        self.data_pointer = 0
        self.output = []
        self.input_pointer = 0
        self.input = input
        self.l = 0
        self.i = 0

    def next_cell(self):
        self.data_pointer = 0 if self.data_pointer + 1 == 256 else self.data_pointer + 1

    def prev_cell(self):
        self.data_pointer = 255 if self.data_pointer - 1 == -1 else self.data_pointer - 1

    def inc(self):
        self.memory[self.data_pointer] += 1
        if self.memory[self.data_pointer] == 256:
            self.memory[self.data_pointer] = 0

    def dec(self):
        self.memory[self.data_pointer] -= 1
        if self.memory[self.data_pointer] == -1:
            self.memory[self.data_pointer] = 255

    def out(self):
        self.output.append(chr(self.memory[self.data_pointer]))

    def inp(self):
        self.memory[self.data_pointer] = ord(self.input[self.input_pointer])
        self.input_pointer += 1

    def left_bracket(self):
        if self.memory[self.data_pointer] == 0:
            self.i += 1
            while self.l > 0 or self.code[self.i] != "]":
                if self.code[self.i] == '[':
                    self.l += 1
                if self.code[self.i] == ']':
                    self.l -= 1
                self.i += 1

    def right_bracket(self):
        if self.memory[self.data_pointer] != 0:
            self.i -= 1
            while self.l > 0 or self.code[self.i] != "[":
                if self.code[self.i] == ']':
                    self.l += 1
                if self.code[self.i] == '[':
                    self.l -= 1
                self.i -= 1
            self.i -= 1

    def run(self):
        while self.i <= len(self.code) - 1:
            self.interpreter[self.code[self.i]](self)
            self.i += 1
        return "".join(self.output)

    interpreter = {
        ">": next_cell,
        "<": prev_cell,
        "+": inc,
        "-": dec,
        ".": out,
        ",": inp,
        "[": left_bracket,
        "]": right_bracket
    }


def brain_luck(code, input):
    return BFInterpreter(code, input).run()
