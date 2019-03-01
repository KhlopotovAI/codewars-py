from unittest import TestCase

from .kata import valid_parentheses


class TestValidParentheses(TestCase):
    def test_valid_parentheses(self):
        self.assertFalse(valid_parentheses("  ("))
        self.assertFalse(valid_parentheses(")test"))
        self.assertTrue(valid_parentheses(""))
        self.assertFalse(valid_parentheses("hi())("))
        self.assertTrue(valid_parentheses("hi(hi)()"))
