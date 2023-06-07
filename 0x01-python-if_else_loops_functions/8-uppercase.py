#!/usr/bin/python3
def uppercase(str):
    charString = list(str)
    for index, character in enumerate(charString):
        if ord(character) in range(97,123):
            ascii = ord(character) - 32
            character = chr(ascii)
            charString[index] = character
    sentence = "".join(charString)
    print("{}".format(sentence))

