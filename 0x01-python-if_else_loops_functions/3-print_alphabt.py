#!/usr/bin/python3
for alph in range(ord('a'), ord('z')):
    if chr(alph) != 'e' and chr(alph) != 'q':
        print("{}".format(chr(alph)), end="")
