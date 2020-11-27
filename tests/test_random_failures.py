from random import randint

import unittest


class RandomFailures(unittest.TestCase):

    def test_1(self):
        self.assertEqual(1, randint(1, 3))

    def test_2(self):
        self.assertEqual(1, randint(1, 3))

    def test_3(self):
        self.assertEqual(1, randint(1, 3))

    def test_4(self):
        self.assertEqual(1, randint(1, 3))

    def test_5(self):
        self.assertEqual(1, randint(1, 3))

    def test_6(self):
        self.assertEqual(1, randint(1, 3))

    def test_7(self):
        self.assertEqual(1, randint(1, 3))

    def test_8(self):
        self.assertEqual(1, randint(1, 3))

    def test_9(self):
        self.assertEqual(1, randint(1, 3))

    def test_10(self):
        self.assertEqual(1, randint(1, 3))


if __name__ == "__main__":
    unittest.main()
