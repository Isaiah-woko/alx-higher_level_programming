#!/usr/bin/python3
"""
Create a Class Square with:
- size, position private propreties
- method of area and method of print_square
- getters & setters.
"""


class Square:
    """A Class - Square"""

    def __init__(self, size=0, position=(0, 0)):
        """A Constructor of a Square with the size and position"""
        self.size = size
        self.position = position

    def area(self):
        """A Method to get the area of the Square"""
        return (self.__size ** 2)

    def my_print(self):
        """A Method to print a Square with spaces"""
        if (self.__size == 0):
            print()
        else:
            for blank in range(self.position[1]):
                print()
            for rows in range(self.__size):
                print(" " * self.position[0], end='')
                print("#" * self.__size)

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

    @property
    def position(self):
        """Getter of Position"""
        return (self.__position)

    @position.setter
    def position(self, value):
        """Setter of position"""
        if (len(value) != 2) or (type(value) is not tuple) \
                or (type(value[0]) is not int) \
                or (type(value[1]) is not int) \
                or (value[0] < 0) or (value[1] < 0):
            raise TypeError("position must be a tuple of 2 positive integers")
        else:
            self.__position = value
