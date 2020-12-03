from datetime import datetime
from random import randint

import unittest


class RandomFailures(unittest.TestCase):

    def __init__(self, *args, **kwargs):
        super(RandomFailures, self).__init__(*args, **kwargs)
        self.stable = datetime.now().hour % 2

    def test_1(self):
        self._assert_with_stable_condition()

    def test_2(self):
        self._assert_with_stable_condition()

    def test_3(self):
        self._assert_with_stable_condition()

    def test_4(self):
        self._assert_with_stable_condition()

    def test_5(self):
        self._assert_with_stable_condition()

    def test_6(self):
        self._assert_with_stable_condition()

    def test_7(self):
        self._assert_with_stable_condition()

    def test_8(self):
        self._assert_with_stable_condition()

    def test_9(self):
        self._assert_with_stable_condition()

    def test_10_fail_one_out_of_three(self):
        self.assertEqual(1, randint(1, 3))

    def test_11(self):
        self._assert_with_stable_condition()

    def test_12(self):
        self._assert_with_stable_condition()

    def test_13(self):
        self._assert_with_stable_condition()

    def test_14(self):
        self._assert_with_stable_condition()

    def _assert_with_stable_condition(self):
        self.assertEqual(1, 1 if self.stable else randint(1, 3))


if __name__ == "__main__":
    unittest.main()
