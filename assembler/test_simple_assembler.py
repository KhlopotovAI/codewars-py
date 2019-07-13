from unittest import TestCase

from .kata import simple_assembler


class TestSimpleAssembler(TestCase):
    def test_simple_assembler(self):
        code = '''\
        mov a 5
        inc a
        dec a
        dec a
        jnz a -1
        inc a'''
        self.assertEqual(simple_assembler(code.splitlines()), {'a': 1})

        code = '''\
        mov c 12
        mov b 0
        mov a 200
        dec a
        inc b
        jnz a -2
        dec c
        mov a b
        jnz c -5
        jnz 0 1
        mov c a'''
        self.assertEqual(simple_assembler(code.splitlines()), {'a': 409600, 'c': 409600, 'b': 409600})

        code = '''\
                mov a 1
                mov b 1
                mov c 0
                mov d 26
                jnz c 2
                jnz 1 5
                mov c 7
                inc d
                dec c
                jnz c -2
                mov c a
                inc a
                dec b
                jnz b -2
                mov b c
                dec d
                jnz d -6
                mov c 18
                mov d 11
                inc a
                dec d
                jnz d -2
                dec c
                jnz c -5'''
        self.assertEqual(simple_assembler(code.splitlines()), {'a': 318009, 'b': 196418, 'c': 0, 'd': 0})
