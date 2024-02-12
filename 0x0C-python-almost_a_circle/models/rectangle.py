#!/usr/bin/python3

"""This module contains a class defintion of the Base models rectangle"""

from models.base import Base


class Rectangle(Base):
    """This is the class defition of the rectangle model.

       Attributes:
            width: this represents the width of the Rectangle
                        object as a private instance attribute.
            height: this represents the height of the Rectangle
                        object as a private intance attibute.
            x: this represent the x co-ordinate postion of the
                        Rectangle object as a private attribute.
            y: this represent the y co-ordinate postion of the
                    Rectangle object as a private attribute.
    """

    def __init__(self, width, height, x=0, y=0, id=None):
        super().__init__(id=id)

        # validate width attribute.
        if not isinstance(width, int):
            raise TypeError("width must be an intger")
        elif width <= 0:
            raise ValueError("width must be > 0")

        # validate height attribute
        if not isinstance(height, int):
            raise TypeError("height must be an integer")
        elif height <= 0:
            raise ValueError("height must be > 0")

        # validate x-cordinate attribute
        if not isinstance(x, int):
            raise TypeError("x must be an integer")
        elif x < 0:
            raise ValueError("x must be >= 0")

        # validate y-cordinate attribute
        if not isinstance(y, int):
            raise TypeError("y must be an integer")
        elif y < 0:
            raise ValueError("y must be >= 0")

        self.__width = width
        self.__height = height
        self.__x = x
        self.__y = y

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, value):
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        elif value <= 0:
            raise ValueError("width must be > 0")
        else:
            self.__width = value

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        elif value <= 0:
            raise ValueError("height must be > 0")
        else:
            self.__height = value

    @property
    def x(self):
        return self.__x

    @x.setter
    def x(self, value):
        if not isinstance(value, int):
            raise TypeError("x must be an integer")
        elif value < 0:
            raise ValueError("x must be >= 0")
        else:
            self.__x = value

    @property
    def y(self):
        return self.__y

    @y.setter
    def y(self, value):
        if not isinstance(value, int):
            raise TypeError("y must be an integer")
        elif value < 0:
            raise ValueError("y must be >= 0")
        else:
            self.__y = value

    def area(self):
        """Rectangle area method"""
        return (self.width * self.height)

    def display(self):
        """Prints a rectangle"""
        rectangle = ""

        # Add vertical space before the rectangle
        rectangle += '\n' * self.__y

        for _ in range(self.__height):
            # Add horizontal space (indentation) before drawing the row
            rectangle += ' ' * self.__x
            # Add the row of '#' characters representing the rectangle's width
            rectangle += '#' * self.__width + '\n'

        # Print the constructed rectangle
        print(rectangle, end='')

    def __str__(self):
        """Returns astring representation"""

        cor_x = self.__x
        cor_y = self.y
        rect_height = self.__height
        rect_width = self.__width

        result = ("[Rectangle] ({}) {}/{} - {}/{}"
                  .format(self.id, cor_x, cor_y, rect_width, rect_height))

        return result

    def update(self, *args, **kwargs):
        """An Update method"""
        attributes = ['id', 'width', 'height', 'x', 'y']
        for i, arg in enumerate(args):
            setattr(self, attributes[i], arg)

        if not args:
            if 'id' in kwargs:
                self.id = kwargs['id']
            if 'width' in kwargs:
                self.__width = kwargs['width']
            if 'height' in kwargs:
                self.__height = kwargs['height']
            if 'x' in kwargs:
                self.__x = kwargs['x']
            if 'y' in kwargs:
                self.__y = kwargs['y']
