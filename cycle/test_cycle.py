from unittest import TestCase

from .kata import cycle


class TestCycle(TestCase):
    def test_cycle(self):
        self.assertEqual(cycle(3), 1)
        self.assertEqual(cycle(33), 2)
        self.assertEqual(cycle(18118), -1)
        self.assertEqual(cycle(69), 22)
        self.assertEqual(cycle(197), 98)
        self.assertEqual(cycle(65), -1)
        self.assertEqual(cycle(97), 96)
        self.assertEqual(cycle(19), 18)
        self.assertEqual(cycle(111), 3)
        self.assertEqual(cycle(53), 13)
        self.assertEqual(cycle(59), 58)
        self.assertEqual(cycle(93), 15)
        self.assertEqual(cycle(51), 16)
        self.assertEqual(cycle(159), 13)
        self.assertEqual(cycle(183), 60)
        self.assertEqual(cycle(197), 98)
        self.assertEqual(cycle(167), 166)
        self.assertEqual(cycle(94), -1)
        self.assertEqual(cycle(133), 18)
        self.assertEqual(cycle(218713), 9744)
        self.assertEqual(cycle(38127), 6230)
        self.assertEqual(cycle(431541), 726)
        self.assertEqual(cycle(221193), 3510)
        self.assertEqual(cycle(1234567), 34020)
