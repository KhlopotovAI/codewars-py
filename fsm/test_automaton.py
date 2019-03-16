from unittest import TestCase

from .kata import my_automaton


class TestAutomaton(TestCase):
    def test_read_commands(self):
        self.assertTrue(my_automaton.read_commands(["1"]))
        self.assertTrue(my_automaton.read_commands(["1", "0", "0", "1"]))
