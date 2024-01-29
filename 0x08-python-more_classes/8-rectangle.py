#!/usr/bin/python3

"""This module contains the definition of the class for a Rectangle"""


class Rectangle(object):
    """This class object respresnets the definition for the Rectangle class
        It has several methods thats defines the Area and some other properties
        of the Rectangle class object.
    """
    number_of_instances = 0

    def __init__(self, width=0, height=0):
        if not isinstance(width, int):
            raise TypeError("width must be an integer")
        if width < 0:
            raise ValueError("width must be >= 0")
        if not isinstance(height, int):
            raise TypeError("height must be an integer")
        if height < 0:
            raise ValueError("height must be >= 0")
        self.__height = height
        self.__width = width
        Rectangle.number_of_instances += 1

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError("height must be an integer")

        if value < 0:
            raise ValueError("height must be >= 0")
        else:
            self.__height = value

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, value):
        if not isinstance(value, int):
            raise TypeError("width must be an integer")

        if value < 0:
            raise ValueError("width must be >= 0")
        else:
            self.__width = value

    def area(self):
        return self.__height * self.__width

    def perimeter(self):
        if self.__width == 0 or self.__height == 0:
            return 0
        else:
            return 2 * (self.__height + self.__width)

    print_symbol = '#'

    def __str__(self):
        rect = ""
        if self.__width == 0 or self.__height == 0:
            return rect
        else:
            symb = str(self.print_symbol)
            rect = '\n'.join(symb * self.__width for i in range(self.__height))
            return rect

    def __repr__(self):
        return f"Rectangle{self.__width, self.__height}"

    def __del__(self):
        print("Bye rectangle...")
        Rectangle.number_of_instances -= 1

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        if not isinstance(rect_1, Rectangle):
            raise TypeError("rect_1 must be an instance of Rectangle")

        if not isinstance(rect_2, Rectangle):
            raise TypeError("rect_2 must be an instance of Rectangle")

        area_rect_1 = rect_1.area()
        area_rect_2 = rect_2.area()

        if area_rect_1 == area_rect_2:
            return rect_1
        elif area_rect_1 > area_rect_2:
            return rect_1
        else:
            return rect_2
