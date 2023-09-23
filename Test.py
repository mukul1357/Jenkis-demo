#!/usr/bin/python3

import unittest

from Prog1 import summation


class TestSum(unittest.TestCase):
    
    def test_list_int(self):
        data = [23, 32]
        res = summation(data)
        self.assertEqual(res, 55)

if __name__ == "__main__":
    unittest.main()
