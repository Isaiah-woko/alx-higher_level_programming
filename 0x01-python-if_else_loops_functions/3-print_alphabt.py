#!/usr/bin/python3
for alph in range(ord('a'), ord('z')):
    if chr(alph) not in ['e', 'q']:
        print("{}".format(chr(alph)), end="")
