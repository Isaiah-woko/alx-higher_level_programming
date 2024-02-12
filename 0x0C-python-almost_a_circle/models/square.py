#!/usr/bin/python3

"""This module contains a class defintion of the Base models rectangle"""

from models.rectangle import Rectangle


class Square(Rectangle):
    """This is the class defition of the square model.

       Attributes:
            width: this represents the width of the Square
                        object as a private instance attribute.
            height: this represents the height of the Square
                        object as a private intance attibute.
            x: this represent the x co-ordinate postion of the
                        Square object as a private attribute.
            y: this represent the y co-ordinate postion of the
                    Square object as a private attribute.
    """

    def __init__(self, size, x=0, y=0, id=None):
        super().__init__(id=id, height=size, width=size, x=x, y=y)
        self.__size = size
