#!/usr/bin/python3

"""This module contains a class defintion of the Base models class"""


import json


class Base(object):
    """This is the class defition of the base model.

       Attributes:
           id: this represents the id of the class.
    """

    __nb_objects = 0

    def __init__(self, id=None):
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """returns the JSON string representation"""

        if list_dictionaries is None or list_dictionaries == []:
            return "[]"

        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """Saves list_objs as a JSON string representation to a file"""

        filename = cls.__name__ + ".json"
        with open(filename, 'w') as file:
            if list_objs is None:
                file.write("[]")
            else:
                # Convert each object in list_objs to dictionary
                objects_dict = [obj.to_dictionary() for obj in list_objs]
                json_string = Base.to_json_string(objects_dict)
                file.write(json_string)

    @staticmethod
    def from_json_string(json_string):
        """args : (str) my_str"""
        if json_string is None or json_string == []:
            return []
        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """returns an instance with all attributes already set"""
        if dictionary is None or dictionary == {}:
            return
        if cls.__name__ == "Rectangle":
            instance = cls(1, 1)
        else:
            instance = cls(1)
        instance.update(**dictionary)
        return instance

    @classmethod
    def load_from_file(cls):
        """"returns a list of instances"""
        filename = cls.__name__ + ".json"
        result = []
        try:
            with open(filename, "r") as file:
                # load
                load = Base.from_json_string(file.read())
                for lo in load:
                    result.append(cls.create(**lo))
        except IOError:
            result = []
        return result
