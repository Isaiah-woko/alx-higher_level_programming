#!/usr/bin/python3

"""This module contains the code for file input"""


def append_write(filename="", text=""):

    """
        This is a function for appending text to a file using with
        Args:
        filename: The file to open
        text: the text to write on the file
    """

    with open(filename, "a") as write_file:
        write_file.write(text)

    return len(text)
