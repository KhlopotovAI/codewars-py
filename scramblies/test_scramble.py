from unittest import TestCase

from .kata import scramble


class TestScramble(TestCase):
    def test_scramble(self):
        self.assertTrue(scramble('rkqodlw', 'world'))
        self.assertTrue(scramble('cedewaraaossoqqyt', 'codewars'))
        self.assertFalse(scramble('katas', 'steak'))
        self.assertTrue(scramble('scriptjava', 'javascript'))
        self.assertTrue(scramble('scriptingjava', 'javascript'))
