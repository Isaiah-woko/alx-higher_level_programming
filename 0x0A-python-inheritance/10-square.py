#!/usr/bin/python3

"""This module contains one class and one subclass"""


class BaseGeometry:
    """This class respresnets the definition for the BaseGeometry class
        It has several methods thats defines the Area and some other properties
        of the BaseGeometry class object.
    """

    def area(self):
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):

        if not isinstance(value, int):
            raise TypeError(f"{name} must be an integer")

        if value <= 0:
            raise ValueError(f"{name} must be greater than 0")

        if not isinstance(name, str):
            raise TypeError("{} must be a string".format(name))


class Rectangle(BaseGeometry):
    """This class is a defintion of a rectangle class which inherits
       methods of the BaseGeometry class.
    """
    def __init__(self, width, height):

        self.integer_validator("width", width)
        self.integer_validator("height", height)

        self.__height = height
        self.__width = width

    def __str__(self):
        return "[Rectangle] {}/{}".format(self.__width, self.__height)

    def area(self):
        return self.__width * self.__height


class Square(Rectangle):
    """This class is a defintion of a rectangle class which inherits
       methods of the Retangle class.
    """

    def __init__(self, size):
        super().__init__(size, size)
        self.integer_validator("size", size)

    def area(self):
        return super().area()
