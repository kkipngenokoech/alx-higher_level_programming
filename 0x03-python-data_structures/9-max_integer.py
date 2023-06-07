#!/usr/bin/python3
def max_integer(my_list=[]):
    if my_list != []:
        my_list.sort()
        maxInt = my_list[-1]
    else:
        maxInt = None
    return maxInt
