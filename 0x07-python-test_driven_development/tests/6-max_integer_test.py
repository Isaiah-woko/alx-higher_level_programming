"""This module contains testing for max integers"""

import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):
    """This class handles all test cases for max_integer"""

    def test_instances(self):
        self.assertIsInstance(max_integer([12, 2.6, 3, 5]), (int, float))

    def test_not_instances(self):
        self.assertNotIsInstance(max_integer(['i', 'c', 'k']), (int, float))

    def test_positive(self):
        self.assertEqual(max_integer([3, 5, 7]), 7)

    def test_negative(self):
        self.assertEqual(max_integer([-4, -8, -2]), -2)

    def test_biggest_element(self):
        self.assertEqual(max_integer([20, 80, 120]), 120)

    def test_wrong_argument(self):
        self.assertRaises(TypeError, max_integer((20, 10, 30)))

    def test_empty_list(self):
        self.assertIsNone(max_integer([]), None)

    def test_not_none(self):
        self.assertIsNotNone(max_integer([22]), None)

    def test_is_object(self):
        self.assertIs(max_integer([20, 30, 50]), max_integer([20, 30, 50]))

    def test_is_not_object(self):
        self.assertIsNot(max_integer([50, 26]), max_integer([72, 44]))

    def test_error_assertion(self):
        self.assertRaises(TypeError, max_integer(['i']))
