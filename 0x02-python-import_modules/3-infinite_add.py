#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    result = 0

    arguments = sys.argv[1:]
    for i in arguments:
        result += int(i)
    print("{}".format(result))
