from unittest import TestCase

from .kata import permutations


class TestPermutations(TestCase):
    def test_permutations(self):
        self.assertEqual(sorted(permutations('ab')), ['ab', 'ba'])
        self.assertEqual(sorted(permutations('a')), ['a'])
        self.assertEqual(sorted(permutations('aabb')), ['aabb', 'abab', 'abba', 'baab', 'baba', 'bbaa'])
