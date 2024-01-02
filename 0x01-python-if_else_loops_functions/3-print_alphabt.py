#!/usr/bin/python3
for alph in range(97, 123):
    if chr(alph) not in ['e', 'q']:
        print("{}".format(chr(alph)), end="")
