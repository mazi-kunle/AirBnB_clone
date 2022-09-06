#!/usr/bin/python3
"""Test"""

import unittest


class TestChaine(unittest.TestCase):

    def test_reversed(self):
        res = reversed('abcd')
        self.assertEqual('dcba', "".join(res))

    def test_sorted(self):
        res = sorted('dbac')
        self.assertEqual(['a', 'b', 'c', 'd'], res)

    def test_upper(self):
        res = "hello".upper()
        a = 0.0
        # print(type(a))
        self.assertEqual('HELLO', res)

if __name__ == '__main__':
    unittest.main()