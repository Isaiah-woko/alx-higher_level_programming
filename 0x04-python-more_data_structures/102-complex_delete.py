#!/usr/bin/python3
def complex_delete(a_dictionary, value):
    deleted_value = [key for key, val in a_dictionary.items() if val == value]
    for key in deleted_value:
        del a_dictionary[key]
    return a_dictionary
