#!/usr/bin/python3
import json

"""This is a module for json representation"""


def to_json_string(object):

    """This function returns the JSON
        representation of an object (string)

        Args:
        my_obj: The object to return JSON representation
    """

    return (json.dumps(object))
