import unittest

from prime_tester import prime_tester


class TestPrimeChecker(unittest.TestCase):
    def test_pass_simple(self):
        x = 2
        res = prime_tester(x)
        self.assertEqual(res, True)

    def test_pass_medium(self):
        x = 53
        res = prime_tester(x)
        self.assertEqual(res, True)

    def test_pass_hard(self):
        x = 17
        res = prime_tester(x)
        self.assertEqual(res, True)


if __name__ == "__main__":
    unittest.main()