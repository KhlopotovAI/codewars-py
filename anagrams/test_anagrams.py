from unittest import TestCase

from .kata import anagrams


class TestAnagrams(TestCase):
    def test_anagrams(self):
        self.assertEqual(['aabb', 'bbaa'], anagrams('abba', ['aabb', 'abcd', 'bbaa', 'dada']))
        self.assertEqual(['carer', 'racer'], anagrams('racer', ['crazer', 'carer', 'racar', 'caers', 'racer']))
