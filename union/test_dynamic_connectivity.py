from unittest import TestCase

from .kata import DynamicConnectivity


class TestDynamicConnectivity(TestCase):
    def test_union(self):
        results1 = DynamicConnectivity(10)
        results1.union(4, 3)
        results1.union(3, 8)
        results1.union(6, 5)
        results1.union(9, 4)
        results1.union(2, 1)
        self.assertFalse(results1.connected(0, 7))
        self.assertTrue(results1.connected(8, 9))
        results1.union(5, 0)
        results1.union(7, 2)
        results1.union(6, 1)
        results1.union(1, 0)
        self.assertTrue(results1.connected(0, 7))

        results2 = DynamicConnectivity(36)
        results2.union(6, 12)
        results2.union(12, 18)
        results2.union(18, 24)
        results2.union(24, 30)
        results2.union(30, 29)
        results2.union(29, 28)
        results2.union(28, 22)
        results2.union(22, 16)
        results2.union(16, 10)
        results2.union(10, 9)
        results2.union(9, 8)
        results2.union(8, 7)
        results2.union(13, 7)
        results2.union(19, 13)
        results2.union(19, 25)
        results2.union(25, 26)
        results2.union(32, 27)
        self.assertFalse(results2.connected(6, 32))
        self.assertFalse(results2.connected(11, 9))
        results2.union(32, 26)
        self.assertTrue(results2.connected(6, 32))
