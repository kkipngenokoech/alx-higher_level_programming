#!/usr/bin/python3
def multiply_list_map(my_list=[], number=0):
    new_list = my_list.copy()
    for index, element in enumerate(new_list):
        new_list[index] = element * number
    return new_list
