from unittest import TestCase

from .kata import xp_to_target_lvl


class TestXpToTargetLvl(TestCase):
    def test_xp_to_target_lvl(self):
        self.assertEqual(1808, xp_to_target_lvl(0, 5))
        self.assertEqual(29535, xp_to_target_lvl(12345, 17))
        self.assertEqual(1, xp_to_target_lvl(313, 2))
        self.assertEqual(769000000000000, xp_to_target_lvl(832696988485, 170))
        self.assertEqual("Input is invalid.", xp_to_target_lvl())
        self.assertEqual("Input is invalid.", xp_to_target_lvl(31428, '47'))
        self.assertEqual("Input is invalid.", xp_to_target_lvl(7392984749, 900))
        self.assertEqual("Input is invalid.", xp_to_target_lvl(123, 0))
        self.assertEqual("Input is invalid.", xp_to_target_lvl(-987654321, 99))
        self.assertEqual("Input is invalid.", xp_to_target_lvl(999999, [101]))
        self.assertEqual('You have already reached level 1.', xp_to_target_lvl(0, 1))
        self.assertEqual("You have already reached level 4.", xp_to_target_lvl(2017, 4))
        self.assertEqual('You have already reached level 170.', xp_to_target_lvl(769832696988485, 170))
