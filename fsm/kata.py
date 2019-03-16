# https://www.codewars.com/kata/design-a-simple-automaton-finite-state-machine/train/python
class State:
    def __init__(self, a):
        self.a = a

    def execute(self, command):
        pass

    def res(self):
        return False


class Q1State(State):
    def execute(self, command):
        if command == "1":
            self.a.cur_state = self.a.q2


class Q2State(State):
    def execute(self, command):
        if command == "0":
            self.a.cur_state = self.a.q3

    def res(self):
        return True


class Q3State(State):
    def execute(self, command):
        self.a.cur_state = self.a.q2


class Automaton(object):
    def __init__(self):
        self.q1 = Q1State(self)
        self.q2 = Q2State(self)
        self.q3 = Q3State(self)
        self.cur_state = self.q1

    def read_commands(self, commands):
        for c in commands:
            self.cur_state.execute(c)
        return self.cur_state.res()


my_automaton = Automaton()
