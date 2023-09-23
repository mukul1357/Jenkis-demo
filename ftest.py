import unittest

from prime_tester import prime_tester


class TestPrimeChecker(unittest.TestCase):
    
    def test_fail_simple(self):
        x = 9
        res = prime_tester(x)
        self.assertEqual(res,True)

    def test_fail_medium(self):
        x = 51
        res = prime_tester(x)
        self.assertEqual(res,True)
    def print():
        print("hello")


if __name__ == "__main__":
    unittest.main()
