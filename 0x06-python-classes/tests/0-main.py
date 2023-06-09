#!/usr/bin/python3
import sys

sys.path.append('../')
Square = __import__('0-square').Square

my_square = Square()
print(type(my_square))
print(my_square.__dict__)

