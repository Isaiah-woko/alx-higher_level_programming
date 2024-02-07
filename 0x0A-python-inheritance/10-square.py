#!/usr/bin/python3

"""This module contains one class and one subclass"""

Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """This class is a defintion of a rectangle class which inherits
       methods of the Retangle class.
    """

    def __init__(self, size):
        self.integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size

    def area(self):
        """implementing the area method"""
        return self.__size ** 2
