#!/usr/bin/python3

"""This module contains a function for formating a text
   Args:
   text: the text to format
"""


def text_indentation(text):

    """This function handles the formating of a tex based
        on each of these characters: . ? and :
    """

    if not isinstance(text, str):
        raise TypeError("text must be a string")

    characters = (".", "?", ":")

    for char in text:
        if char in characters:
            print("{}".format(char), end='')
            print("\n")
        else:
            print("{}".format(char), end='')
