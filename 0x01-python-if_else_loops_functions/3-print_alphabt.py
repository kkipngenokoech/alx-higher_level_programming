#!/usr/bin/python3

for character in range(97, 123):
    if character == 113 or character == 101:
        continue
    print('{}'.format(chr(character)), end="")
