from datetime import datetime
from random import randint
from time import sleep

import unittest


class AllRight(unittest.TestCase):

    def __init__(self, *args, **kwargs):
        super(AllRight, self).__init__(*args, **kwargs)
        self.shall_sleep = datetime.now().hour % 2

    def test_1(self):
        self._assert_and_sleep(1)

    def test_2(self):
        self._assert_and_sleep(2)

    def test_3(self):
        self._assert_and_sleep(3)

    def test_4(self):
        self._assert_and_sleep(4)

    def test_5(self):
        self._assert_and_sleep(5)

    def test_6(self):
        self._assert_and_sleep(6)

    def test_7(self):
        self._assert_and_sleep(7)

    def test_8(self):
        self._assert_and_sleep(8)

    def _assert_and_sleep(self, test_number):
        if self.shall_sleep:
            sleep(randint(1, test_number))
        self.assertEqual(test_number, test_number)


if __name__ == "__main__":
    unittest.main()
