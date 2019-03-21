from unittest import TestCase

from .kata import solution


class TestSolution(TestCase):
    def test_solution(self):
        # -*- coding: utf-8 -*-
        self.assertEqual(solution("apples, pears # and bananas\ngrapes\nbananas !apples", ["#", "!"]),
                         "apples, pears\ngrapes\nbananas")
        self.assertEqual(solution("a #b\nc\nd $e f g", ["#", "$"]), "a\nc\nd")
