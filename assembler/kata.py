# https://www.codewars.com/kata/simple-assembler-interpreter/train/python

class Program:
    register = {}
    counter = 0


def inc(reg):
    Program.register[reg] += 1
    pass


def dec(reg):
    Program.register[reg] -= 1
    pass


def mov(reg, num):
    Program.register[reg] = to_num(num)
    pass


def jnz(reg, num):
    if to_num(reg) != 0:
        Program.counter += to_num(num) - 1 if int(num) >= 0 else to_num(num) - 1
    pass


def to_num(num_or_reg):
    if num_or_reg.isalpha():
        return Program.register[num_or_reg]
    else:
        return int(num_or_reg)


commands = {
    "mov": mov,
    "inc": inc,
    "dec": dec,
    "jnz": jnz,
}


def simple_assembler(program):
    Program.register.clear()
    Program.counter = 0

    prog = list(map(lambda x: x.strip().split(), program))

    while Program.counter < len(program):
        args = prog[Program.counter]
        commands[args[0]](*args[1:])
        Program.counter += 1

    return Program.register
