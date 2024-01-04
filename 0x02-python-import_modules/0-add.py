#!/usr/bin/python3
import add_0


def add_number():
    a = 1
    b = 2

    print("{} + {} = {}".format(a, b, add_0.add(a, b)))


if __name__ == "__main__":
    add_number()
