from unittest import TestCase

from .kata import spin_words


class TestSpinWords(TestCase):
    def test_spin_words(self):
        self.assertEqual("emocleW", spin_words("Welcome"))
