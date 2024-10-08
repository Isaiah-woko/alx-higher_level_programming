#!/usr/bin/python3
"""Creates a Class Square with size, method of area and getters & setters"""


class Square:
    """Class - Square"""

    def __init__(self, size=0):
        """A Constructor of a Square with the size"""
        if (type(size) is not int):
            raise (TypeError("size must be an integer"))
        elif (size < 0):
            raise (ValueError("size must be >= 0"))
        else:
            self.__size = size

    def area(self):
        """A Method to get the area of the Square"""
        return (self.__size ** 2)

    @property
    def size(self):
        """The Getter of the private attribute size"""
        return (self.__size)

    @size.setter
    def size(self, value):
        """The Setter for the size private attribute"""
        if (type(value) is not int):
            raise (TypeError("size must be an integer"))
        elif (value < 0):
            raise (ValueError("size must be >= 0"))
        else:
            self.__size = value
