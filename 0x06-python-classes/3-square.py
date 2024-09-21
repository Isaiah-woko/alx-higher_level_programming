#!/usr/bin/python3
"""Creates a Class Square with size and method of area"""


class Square:
    """A Class - Square"""

    def __init__(self, size=0):
        """Constructor of a Square with the size"""
        if (type(size) is not int):
            raise (TypeError("size must be an integer"))
        elif (size < 0):
            raise (ValueError("size must be >= 0"))
        else:
            self.__size = size

    def area(self):
        """A Method to get the area of the Square"""
        return (self.__size ** 2)
