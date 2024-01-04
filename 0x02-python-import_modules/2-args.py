#!/usr/bin/python3

if __name__ == "__main__":
    import sys

    arguments = sys.argv[1:]

    if len(arguments) == 0:
        print("{} {}".format(len(sys.argv) - 1, "arguments."))
    elif len(arguments) == 1:
        print("{} {}".format(len(sys.argv) - 1, "argument:"))
    else:
        print("{} {}".format(len(sys.argv) - 1, "arguments:"))

for i in range(1, len(sys.argv)):
    print("{}: {}".format(i, sys.argv[i]))
