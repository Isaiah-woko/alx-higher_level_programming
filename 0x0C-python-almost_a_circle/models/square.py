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
        super().__init__(size, size, x, y, id)

    def __str__(self):
        """Returns astring representation"""

        cor_x = self.x
        cor_y = self.y

        result = ("[Square] ({}) {}/{} - {}"
                  .format(self.id, cor_x, cor_y, self.size))

        return result

    @property
    def size(self):
        """size getter"""
        return self.width

    @size.setter
    def size(self, value):
        """size setter"""
        self.width = value
        self.height = value
