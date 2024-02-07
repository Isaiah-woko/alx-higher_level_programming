#!/usr/bin/python3


"""This module contains a class that inherits from int
   class and acts as a rebel.
"""


class MyInt(int):
    "This class acts as a rebel to integer operators"
    def __init__(self, number):
        self.number = number

    def __eq__(self, other):
        return self.number != other

    def __ne__(self, other):
        return self.number == other
