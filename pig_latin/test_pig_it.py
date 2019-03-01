from unittest import TestCase

from .kata import pig_it


class TestPigIt(TestCase):
    def test_pig_it(self):
        self.assertEqual('igPay atinlay siay oolcay', pig_it('Pig latin is cool'))
        self.assertEqual('hisTay siay ymay tringsay', pig_it('This is my string'))
