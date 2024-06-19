#!/usr/bin/python3


""" This is the module for the test cases."""


import unittest
from models.base import Base


class TestBaseClass(unittest.TestCase):

    def test_id_not_provided(self):
        obj1 = Base()
        self.assertEqual(obj1.id, 2)

        obj2 = Base()
        self.assertEqual(obj2.id, 2)

    def test_id_provided(self):
        obj3 = Base(id=10)
        self.assertEqual(obj3.id, 10)

    def test_class_attribute_increment(self):
        obj4 = Base()
        obj5 = Base()
        self.assertEqual(obj5.id, obj4.id + 1)
