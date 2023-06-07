#!/usr/bin/python3
def multiple_returns(sentence):
    length = len(sentence)
    if length >= 1:
        firstA = sentence[0]
    else:
        firstA = 'None'
    tupleReturn = (length, firstA)
    return tupleReturn
