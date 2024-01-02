#!/usr/bin/python3
def islower(c):
    for char in c:
        if ord(char) in range(97, 123):
            return True
        else:
            return False
