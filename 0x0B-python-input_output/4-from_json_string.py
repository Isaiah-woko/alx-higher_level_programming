#!/usr/bin/python3

"""This is a module for json representation"""

import json


def from_json_string(my_str):

    """This function  returns an object (Python data structure)
       represented by a JSON string

        Args:
        my_str: The object to return JSON representation
    """

    return json.loads(my_str)
