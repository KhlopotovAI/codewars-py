import math
import random
from unittest import TestCase

from .kata import missing


class TestMissing(TestCase):
    def test_missing(self):
        def get_value(s, i, m):
            if i + m > len(s):
                return -1
            value = 0
            for j in range(0, m):
                c = int(s[i + j])
                if c < 0 or c > 9:
                    return -1
                value = value * 10 + c
            return value

        def missing_u8(s):
            for m in range(1, 7):
                n = get_value(s, 0, m)
                if n == -1:
                    break
                missing_no, fail = -1, False
                i = m
                while i != len(s):
                    if missing_no == -1 and get_value(s, i, int(math.log10(n + 2)) + 1) == n + 2:
                        missing_no = n + 1
                        n += 2
                    elif get_value(s, i, int(math.log10(n + 1)) + 1) == n + 1:
                        n += 1
                    else:
                        fail = True
                        break
                    i += int(math.log10(n) + 1)
                if not fail:
                    return missing_no
            return -1

        self.assertEqual(missing("899091939495"), 92)
        self.assertEqual(missing("123567"), 4)
        self.assertEqual(missing("9899101102"), 100)
        self.assertEqual(missing("599600601602"), -1)
        self.assertEqual(missing("8990919395"), -1)
        self.assertEqual(missing("998999100010011003"), 1002)
        self.assertEqual(missing("99991000110002"), 10000)
        self.assertEqual(missing("979899100101102"), -1)
        self.assertEqual(missing("900001900002900004900005900006"), 900003)

        for i in range(0, 100):
            arr1, arr2 = [], []
            seq = random.randrange(1, 975000)
            arr1.append(seq)
            length = random.randrange(8, 12)
            edge = random.randrange(1, 5)
            num = 10 ** edge
            seq2 = num - length + 2
            arr2.append(seq2)
            for j in range(0, length + 1):
                seq += 1
                seq2 += 1
                arr1.append(seq)
                arr2.append(seq2)
            trap = random.randrange(1, 20)
            if trap > 7:
                del arr1[random.randrange(1, len(arr1) - 1)]
                del arr2[random.randrange(1, len(arr2) - 1)]
                checker = random.randrange(0, 20)
                if checker < 5:
                    if arr1[1] % 2 == 0:
                        del arr1[random.randrange(1, len(arr1))]
                    else:
                        del arr2[random.randrange(1, len(arr2))]
                test1 = ''.join(map(str, arr1))
                test2 = ''.join(map(str, arr2))
                expected1 = missing_u8(test1)
                expected2 = missing_u8(test2)
                self.assertEqual(missing(test1), expected1)
                self.assertEqual(missing(test2), expected2)
            else:
                test1 = ''.join(map(str, arr1))
                test2 = ''.join(map(str, arr2))
                expected1 = missing_u8(test1)
                expected2 = missing_u8(test2)
                self.assertEqual(missing(test1), expected1)
                self.assertEqual(missing(test2), expected2)
