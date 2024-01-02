#!/usr/bin/python3
def uppercase(str):
    result = ""
    for char in str:
        if 'a' <= char <= 'z':
            upper_case = ord(char) - 32
            result += chr(upper_case)
        else:
            result += char
    print("{}".format(result))
