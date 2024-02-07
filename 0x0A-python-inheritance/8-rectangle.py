#!/usr/bin/python3

"""This module contains one class and one subclass"""


BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """This class is a defintion of a rectangle class which inherits
       methods of the BaseGeometry class.
    """
    def __init__(self, width, height):
        super().__init__()
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height
