#!/usr/bin/python3
import add_0


def add_number():
    a = 1
    b = 2

    result = add_0.add(a, b)
    print("{} + {} = {}".format(a, b, result))


if __name__ == "__main__":
    add_number()
