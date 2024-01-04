#!/usr/bin/python3

if __name__ == "__main__":
    from sys import argv

    arguments = argv[0:]

    if len(arguments) == 0:
        print("{} {}".format(len(argv) - 1, "arguments."))
    elif len(arguments) == 1:
        print("{} {}".format(len(argv) - 1, "argument:"))
    else:
        print("{} {}".format(len(argv) - 1, "arguments:"))

for i in range(1, len(arguments)):
    print("{}: {}".format(i, arguments[i]))
